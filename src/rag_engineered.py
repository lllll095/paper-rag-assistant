import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_chroma import Chroma

# Make sure local imports work when running:
# python src/rag_engineered.py
CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from reranker import CrossEncoderReranker
from bm25_retriever import BM25ChunkRetriever

from query_router import QueryRouter

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = PROJECT_ROOT / ".env"

CHUNK_DB_DIR = PROJECT_ROOT / "chroma_db"
CHUNK_COLLECTION_NAME = "paper_rag_week1"

CATALOG_DB_DIR = PROJECT_ROOT / "paper_catalog_db"
CATALOG_COLLECTION_NAME = "paper_catalog_week2"

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

load_dotenv(dotenv_path=ENV_PATH)


class EngineeredRAG:
    """
    Engineered hierarchical RAG system.

    Pipeline:
        user query
            -> paper-level retrieval
            -> decide specific/global mode
            -> chunk-level candidate retrieval
            -> cross-encoder reranking
            -> LLM answer generation
    """

    def __init__(self):
        self.client, self.model = self._load_llm_client()
        self.embeddings = self._load_embeddings()
        self.chunk_store = self._load_chunk_store()
        self.catalog_store = self._load_catalog_store()

        self.has_chunk_type = self._has_chunk_type_metadata()
        print(f"Has chunk_type metadata: {self.has_chunk_type}")

        self.reranker = CrossEncoderReranker()

        self.bm25_retriever = BM25ChunkRetriever(
            chunk_store=self.chunk_store,
            has_chunk_type=self.has_chunk_type,
        )
        self.query_router = QueryRouter()
    # ------------------------------------------------------------------
    # Loading components
    # ------------------------------------------------------------------

    def _load_llm_client(self):
        api_key = os.getenv("DASHSCOPE_API_KEY")
        base_url = os.getenv("LLM_BASE_URL")
        model = os.getenv("LLM_MODEL", "qwen-plus")

        if not api_key:
            raise ValueError("DASHSCOPE_API_KEY is not set. Please check your .env file.")

        if not base_url:
            raise ValueError("LLM_BASE_URL is not set. Please check your .env file.")

        client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )

        return client, model

    def _load_embeddings(self):
        print("Loading embedding model...")

        embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            encode_kwargs={"normalize_embeddings": True},
        )

        return embeddings

    def _load_chunk_store(self):
        print("Loading chunk-level vectorstore...")

        return Chroma(
            persist_directory=str(CHUNK_DB_DIR),
            embedding_function=self.embeddings,
            collection_name=CHUNK_COLLECTION_NAME,
        )

    def _load_catalog_store(self):
        print("Loading paper-level catalog vectorstore...")

        return Chroma(
            persist_directory=str(CATALOG_DB_DIR),
            embedding_function=self.embeddings,
            collection_name=CATALOG_COLLECTION_NAME,
        )

    def _has_chunk_type_metadata(self):
        """
        Check whether the chunk-level vectorstore has chunk_type metadata.
        This makes the code compatible with old indexes.
        """
        try:
            data = self.chunk_store.get(include=["metadatas"], limit=30)
            metadatas = data.get("metadatas", [])

            for meta in metadatas:
                if meta and "chunk_type" in meta:
                    return True

            return False

        except Exception:
            return False

    # ------------------------------------------------------------------
    # Paper-level retrieval
    # ------------------------------------------------------------------

    def retrieve_candidate_papers(self, query, k=4):
        """
        Retrieve candidate papers from the paper-level catalog.

        The paper catalog should contain one document per paper, including
        title, source filename, abstract, and first-page excerpt.
        """
        results = self.catalog_store.similarity_search_with_score(
            query,
            k=k,
        )

        candidates = []

        for doc, score in results:
            source = doc.metadata.get("source")
            title = doc.metadata.get("title", source)

            if not source:
                continue

            candidates.append(
                {
                    "source": source,
                    "title": title,
                    "score": float(score),
                    "content": doc.page_content,
                }
            )

        return candidates

    @staticmethod
    def _query_looks_broad(query):
        """
        Heuristic detector for broad / comparison / survey-style questions.
        These should usually retrieve from multiple papers.
        """
        q = query.lower()

        broad_patterns = [
            "what methods",
            "which methods",
            "what are the methods",
            "what approaches",
            "which approaches",
            "discussed in these papers",
            "in these papers",
            "across these papers",
            "compare",
            "comparison",
            "difference between",
            "differences between",
            "survey",
            "overview",
            "summarize the methods",
            "all methods",
            "有哪些",
            "哪些方法",
            "比较",
            "区别",
            "综述",
        ]

        return any(pattern in q for pattern in broad_patterns)

    def decide_retrieval_mode(self, query, candidates, gap_threshold=0.15):
        """
        Decide whether to retrieve from one dominant paper or multiple papers.

        Chroma scores are distances: smaller means more similar.

        If the query looks broad, force global mode.
        Otherwise, if the best paper is clearly better than the second-best,
        use specific mode.
        """
        if not candidates:
            return "global"

        if self._query_looks_broad(query):
            return "global"

        if len(candidates) == 1:
            return "specific"

        best = candidates[0]["score"]
        second = candidates[1]["score"]
        gap = second - best

        if gap >= gap_threshold:
            return "specific"

        return "global"

    # ------------------------------------------------------------------
    # Chunk-level retrieval and filters
    # ------------------------------------------------------------------

    def build_chunk_filter(self, source=None, chunk_type="main"):
        """
        Build Chroma metadata filter.

        If chunk_type metadata does not exist in the current index,
        do not use chunk_type filtering.
        """
        conditions = []

        if source:
            conditions.append({"source": source})

        if chunk_type and self.has_chunk_type:
            conditions.append({"chunk_type": chunk_type})

        if len(conditions) == 0:
            return None

        if len(conditions) == 1:
            return conditions[0]

        return {"$and": conditions}

    @staticmethod
    def _deduplicate_docs(docs):
        """
        Remove duplicate chunks.
        """
        seen = set()
        unique_docs = []

        for doc in docs:
            key = (
                doc.metadata.get("source"),
                doc.metadata.get("page"),
                doc.metadata.get("chunk_id"),
            )

            if key in seen:
                continue

            seen.add(key)
            unique_docs.append(doc)

        return unique_docs

    @staticmethod
    def _merge_candidate_docs(*doc_lists):
        """
        Merge dense and BM25 candidates.

        If the same chunk appears in multiple retrieval results, merge metadata
        such as vector_score, bm25_score, and reranker_score.
        """
        merged = {}

        for docs in doc_lists:
            for doc in docs:
                key = (
                    doc.metadata.get("source"),
                    doc.metadata.get("page"),
                    doc.metadata.get("chunk_id"),
                )

                if key not in merged:
                    merged[key] = Document(
                        page_content=doc.page_content,
                        metadata=dict(doc.metadata),
                    )
                else:
                    merged[key].metadata.update(doc.metadata)

        return list(merged.values())

    def retrieve_chunks_from_source(self, query, source, k=4, fetch_k=20):
        """
        Hybrid retrieval from one candidate paper.

        Dense retrieval gets semantic candidates.
        BM25 retrieval gets keyword candidates.
        Then both are merged and reranked by the cross-encoder.
        """
        chroma_filter = self.build_chunk_filter(
            source=source,
            chunk_type="main",
        )

        dense_docs_scores = self.chunk_store.similarity_search_with_score(
            query,
            k=fetch_k,
            filter=chroma_filter,
        )

        dense_docs = []

        for doc, score in dense_docs_scores:
            doc.metadata["vector_score"] = float(score)
            dense_docs.append(doc)

        bm25_docs = self.bm25_retriever.search(
            query=query,
            k=fetch_k,
            source_filter=source,
        )

        candidate_docs = self._merge_candidate_docs(
            dense_docs,
            bm25_docs,
        )

        if not candidate_docs:
            return []

        reranked_docs = self.reranker.rerank(
            query=query,
            docs=candidate_docs,
            top_k=k,
        )

        return reranked_docs

    def retrieve_chunks_global(
        self,
        query,
        candidate_papers,
        total_k=8,
        per_paper_fetch_k=10,
        max_per_source=3,
    ):
        """
        Hybrid retrieval from multiple candidate papers.

        For each candidate paper:
            dense retrieval + BM25 retrieval

        Then:
            merge all candidates
            global rerank
            keep at most max_per_source chunks from each paper
        """
        all_candidate_docs = []

        for paper in candidate_papers:
            source = paper.get("source")

            if not source:
                continue

            chroma_filter = self.build_chunk_filter(
                source=source,
                chunk_type="main",
            )

            dense_docs_scores = self.chunk_store.similarity_search_with_score(
                query,
                k=per_paper_fetch_k,
                filter=chroma_filter,
            )

            dense_docs = []

            for doc, score in dense_docs_scores:
                doc.metadata["vector_score"] = float(score)
                dense_docs.append(doc)

            bm25_docs = self.bm25_retriever.search(
                query=query,
                k=per_paper_fetch_k,
                source_filter=source,
            )

            merged_docs = self._merge_candidate_docs(
                dense_docs,
                bm25_docs,
            )

            all_candidate_docs.extend(merged_docs)

        all_candidate_docs = self._deduplicate_docs(all_candidate_docs)

        if not all_candidate_docs:
            return []

        reranked_docs = self.reranker.rerank(
            query=query,
            docs=all_candidate_docs,
            top_k=len(all_candidate_docs),
        )

        selected_docs = []
        source_counter = {}

        for doc in reranked_docs:
            source = doc.metadata.get("source", "unknown")

            if source_counter.get(source, 0) >= max_per_source:
                continue

            selected_docs.append(doc)
            source_counter[source] = source_counter.get(source, 0) + 1

            if len(selected_docs) >= total_k:
                break

        return selected_docs

    # ------------------------------------------------------------------
    # Full retrieval
    # ------------------------------------------------------------------

    def retrieve(self, query, paper_k=None, chunk_k=None):
        """
        Full hierarchical retrieval.

        Step 1: retrieve candidate papers.
        Step 2: decide specific-paper vs global retrieval.
        Step 3: retrieve chunks from selected candidate papers.
        Step 4: rerank chunks.
        """
        route = self.query_router.route(query)

        if paper_k is None:
            paper_k = route.paper_k

        if chunk_k is None:
            chunk_k = route.chunk_k

        candidate_papers = self.retrieve_candidate_papers(
            query=query,
            k=paper_k,
        )

        if route.retrieval_mode == "global":
            mode = "global"
        else:
            mode = self.decide_retrieval_mode(
                query=query,
                candidates=candidate_papers,
            )

        if mode == "specific" and candidate_papers:
            selected_papers = candidate_papers[:1]

            docs = self.retrieve_chunks_from_source(
                query=query,
                source=selected_papers[0]["source"],
                k=chunk_k,
                fetch_k=max(20, chunk_k * 4),
            )

        else:
            selected_papers = candidate_papers

            docs = self.retrieve_chunks_global(
                query=query,
                candidate_papers=selected_papers,
                total_k=chunk_k,
                per_paper_fetch_k=10,
                max_per_source=route.max_per_source,
            )

        retrieval_info = {
            "mode": mode,
            "query_route": {
                "query_type": route.query_type,
                "retrieval_mode": route.retrieval_mode,
                "paper_k": route.paper_k,
                "chunk_k": route.chunk_k,
                "max_per_source": route.max_per_source,
                "reason": route.reason,
                },
            "candidate_papers": [
                {
                    "source": p["source"],
                    "title": p["title"],
                    "score": p["score"],
                }
                for p in candidate_papers
            ],
            "selected_papers": [
                {
                    "source": p["source"],
                    "title": p["title"],
                    "score": p["score"],
                }
                for p in selected_papers
            ],
        }

        return docs, retrieval_info

    # ------------------------------------------------------------------
    # Formatting and debug
    # ------------------------------------------------------------------

    @staticmethod
    def format_context(docs):
        blocks = []

        for i, doc in enumerate(docs, start=1):
            source = doc.metadata.get("source", "unknown")
            page = doc.metadata.get("page", "unknown")
            chunk_id = doc.metadata.get("chunk_id", "unknown")
            chunk_type = doc.metadata.get("chunk_type", "unknown")
            reranker_score = doc.metadata.get("reranker_score", "unknown")
            vector_score = doc.metadata.get("vector_score", "unknown")
            bm25_score = doc.metadata.get("bm25_score", "unknown")

            block = f"""
[Source {i}]
File: {source}
Page: {page}
Chunk ID: {chunk_id}
Chunk Type: {chunk_type}
Vector Score: {vector_score}
BM25 Score: {bm25_score}
Reranker Score: {reranker_score}

Content:
{doc.page_content}
"""
            blocks.append(block)

        return "\n\n".join(blocks)

    @staticmethod
    def _format_score(score):
        if isinstance(score, (int, float)):
            return f"{score:.4f}"

        return str(score)

    def print_retrieval_debug(self, docs, retrieval_info, preview_chars=500):
        print("=" * 80)
        print("Retrieval Mode:")
        print(retrieval_info["mode"])

        print("=" * 80)
        print("Query Route:")
        print(retrieval_info.get("query_route", {}))

        print("=" * 80)
        print("Candidate Papers:")

        if not retrieval_info["candidate_papers"]:
            print("No candidate papers found.")
        else:
            for i, paper in enumerate(retrieval_info["candidate_papers"], start=1):
                score_text = self._format_score(paper.get("score"))
                print(f"[{i}] score={score_text}")
                print(f"    {paper.get('source')}")

        print("=" * 80)
        print("Selected Papers:")

        if not retrieval_info["selected_papers"]:
            print("No selected papers.")
        else:
            for i, paper in enumerate(retrieval_info["selected_papers"], start=1):
                print(f"[{i}] {paper.get('source')}")

        print("=" * 80)
        print("Retrieved Chunks:")

        if not docs:
            print("No chunks retrieved.")
            return

        for i, doc in enumerate(docs, start=1):
            source = doc.metadata.get("source", "unknown")
            page = doc.metadata.get("page", "unknown")
            chunk_id = doc.metadata.get("chunk_id", "unknown")
            chunk_type = doc.metadata.get("chunk_type", "unknown")
            reranker_score = doc.metadata.get("reranker_score", "unknown")
            vector_score = doc.metadata.get("vector_score", "unknown")
            bm25_score = doc.metadata.get("bm25_score", "unknown")
            preview = doc.page_content[:preview_chars].replace("\n", " ")

            print("-" * 80)
            print(
                f"[Source {i}] {source}, page {page}, chunk {chunk_id}, "
                f"type={chunk_type}, "
                f"vector_score={vector_score}, "
                f"bm25_score={bm25_score}, "
                f"reranker_score={reranker_score}"
            )
            print(preview)

    # ------------------------------------------------------------------
    # Answer generation
    # ------------------------------------------------------------------

    def answer_question(self, question, paper_k=None, chunk_k=None, show_debug=True):
        docs, retrieval_info = self.retrieve(
            query=question,
            paper_k=paper_k,
            chunk_k=chunk_k,
        )

        if show_debug:
            self.print_retrieval_debug(docs, retrieval_info)

        context = self.format_context(docs)

        if retrieval_info["mode"] == "specific":
            retrieval_description = (
                "The retriever identified one dominant candidate paper and retrieved "
                "main-text chunks from that paper, then reranked the chunks."
            )
        else:
            retrieval_description = (
                "The retriever treated the query as a broad multi-paper question, "
                "retrieved chunks from several candidate papers, then reranked them."
            )

        prompt = f"""
You are a careful research assistant helping a statistics PhD student read scientific papers.

Answer the question using only the provided context.

Retrieval strategy:
{retrieval_description}

Question:
{question}

Context:
{context}

If the context is insufficient, say:
"The provided context is insufficient."

Please provide your answer in the following format:

Answer:
A concise answer.

Explanation:
A grounded explanation based on the retrieved sources.

Sources:
List the source numbers you used, such as [Source 1], [Source 3].
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a careful research assistant. "
                        "Use only the retrieved context. "
                        "Do not invent unsupported claims."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.2,
        )

        answer = response.choices[0].message.content

        return answer, docs, retrieval_info


def main():
    rag = EngineeredRAG()

    print("=" * 80)
    print("Engineered Hierarchical RAG + Reranker")
    print("=" * 80)
    print("Ask a question directly. No manual paper selection is required.")
    print("Examples:")
    print("- What AI-generated text detection methods are discussed in these papers?")
    print("- How does AdaDetectGPT work?")
    print("- Which methods provide statistical guarantees?")
    print("- What is the difference between DetectGPT and AdaDetectGPT?")
    print("=" * 80)

    question = input("Question: ").strip()

    if not question:
        question = "What AI-generated text detection methods are discussed in these papers?"

    answer, docs, retrieval_info = rag.answer_question(
        question=question,
        show_debug=True,
    )

    print("=" * 80)
    print("Question:")
    print(question)

    print("=" * 80)
    print("Answer:")
    print(answer)

    print("=" * 80)
    print("Final Sources:")
    for i, doc in enumerate(docs, start=1):
        print(
            f"[Source {i}] "
            f"{doc.metadata.get('source')}, "
            f"page {doc.metadata.get('page')}, "
            f"chunk {doc.metadata.get('chunk_id')}, "
            f"type={doc.metadata.get('chunk_type', 'unknown')}, "
            f"reranker_score={doc.metadata.get('reranker_score', 'unknown')}"
        )


if __name__ == "__main__":
    main()