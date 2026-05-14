import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = PROJECT_ROOT / ".env"

CHROMA_DIR = PROJECT_ROOT / "chroma_db"
COLLECTION_NAME = "paper_rag_week1"

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

load_dotenv(dotenv_path=ENV_PATH)


class PaperRAG:
    def __init__(self):
        self.client, self.model = self._load_llm_client()
        self.vectorstore = self._load_vectorstore()

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

    def _load_vectorstore(self):
        print("Loading embedding model and Chroma vectorstore...")

        embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            encode_kwargs={"normalize_embeddings": True},
        )

        vectorstore = Chroma(
            persist_directory=str(CHROMA_DIR),
            embedding_function=embeddings,
            collection_name=COLLECTION_NAME,
        )

        print("Vectorstore loaded.")

        return vectorstore

    def list_sources(self):
        """
        Get all unique PDF source names from Chroma metadata.
        """
        data = self.vectorstore.get(include=["metadatas"])
        metadatas = data.get("metadatas", [])

        sources = set()

        for meta in metadatas:
            if not meta:
                continue

            source = meta.get("source")
            if source:
                sources.add(source)

        return sorted(list(sources))

    def choose_source_interactive(self):
        """
        Let the user choose one paper from all indexed PDF files.
        """
        sources = self.list_sources()

        if not sources:
            raise ValueError("No source files found in the vectorstore metadata.")

        print("=" * 80)
        print("Available papers:")
        print("=" * 80)

        for i, source in enumerate(sources, start=1):
            print(f"[{i}] {source}")

        print("=" * 80)

        while True:
            choice = input("Choose a paper number: ").strip()

            if not choice.isdigit():
                print("Please enter a valid number.")
                continue

            idx = int(choice)

            if 1 <= idx <= len(sources):
                selected_source = sources[idx - 1]
                print(f"Selected paper: {selected_source}")
                return selected_source

            print(f"Please enter a number between 1 and {len(sources)}.")

    def retrieve(self, query, k=5, source_filter=None):
        """
        Retrieve relevant chunks.

        If source_filter is given, only retrieve chunks from that PDF.
        """
        if source_filter:
            docs = self.vectorstore.similarity_search(
                query,
                k=k,
                filter={"source": source_filter},
            )
        else:
            docs = self.vectorstore.similarity_search(
                query,
                k=k,
            )

        return docs

    @staticmethod
    def format_context(docs):
        context_blocks = []

        for i, doc in enumerate(docs, start=1):
            source = doc.metadata.get("source", "unknown")
            page = doc.metadata.get("page", "unknown")
            chunk_id = doc.metadata.get("chunk_id", "unknown")

            block = f"""
[Source {i}]
File: {source}
Page: {page}
Chunk ID: {chunk_id}

Content:
{doc.page_content}
"""
            context_blocks.append(block)

        return "\n\n".join(context_blocks)

    @staticmethod
    def print_retrieved_chunks(docs, preview_chars=500):
        print("=" * 80)
        print("Retrieved Chunk Preview:")
        print("=" * 80)

        for i, doc in enumerate(docs, start=1):
            source = doc.metadata.get("source", "unknown")
            page = doc.metadata.get("page", "unknown")
            chunk_id = doc.metadata.get("chunk_id", "unknown")

            preview = doc.page_content[:preview_chars].replace("\n", " ")

            print(f"[Source {i}] {source}, page {page}, chunk {chunk_id}")
            print(f"Preview: {preview}")
            print("-" * 80)

    def answer_question(self, question, k=5, source_filter=None, show_chunks=True):
        """
        Full RAG-QA pipeline.
        """
        retrieval_query = (
            question
            + "\nFocus on the abstract, introduction, method overview, contribution statements, "
            + "and experimental conclusions if relevant."
        )

        docs = self.retrieve(
            retrieval_query,
            k=k,
            source_filter=source_filter,
        )

        if show_chunks:
            self.print_retrieved_chunks(docs)

        context = self.format_context(docs)

        selected_paper_text = (
            f"\nSelected paper: {source_filter}\n"
            if source_filter
            else "\nSelected paper: not specified. The retrieval may search across all papers.\n"
        )

        prompt = f"""
You are a research assistant helping a statistics PhD student read scientific papers.

Answer the question using only the provided context.

{selected_paper_text}

If the context is insufficient, say:
"The provided context is insufficient."

Question:
{question}

Context:
{context}

Please provide your answer in the following format:

Answer:
A concise answer to the question.

Explanation:
A short explanation grounded in the retrieved context.

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
                        "You must answer only based on the provided context. "
                        "Do not invent facts that are not supported by the sources."
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

        return answer, docs


_rag_engine = None


def get_rag_engine():
    global _rag_engine

    if _rag_engine is None:
        _rag_engine = PaperRAG()

    return _rag_engine


def answer_question(question, k=5, source_filter=None, show_chunks=True):
    rag_engine = get_rag_engine()
    return rag_engine.answer_question(
        question=question,
        k=k,
        source_filter=source_filter,
        show_chunks=show_chunks,
    )


def main():
    rag_engine = get_rag_engine()

    print("=" * 80)
    print("Week 2 RAG-QA with Paper-Level Source Filter")
    print("=" * 80)

    selected_source = rag_engine.choose_source_interactive()

    print("=" * 80)
    print("Enter your question.")
    print("Example:")
    print("What is the main contribution of this paper?")
    print("=" * 80)

    question = input("Question: ").strip()

    if not question:
        question = "What is the main contribution of this paper?"

    top_k_input = input("Top-k retrieval number, default is 5: ").strip()

    if top_k_input.isdigit():
        k = int(top_k_input)
    else:
        k = 5

    answer, docs = rag_engine.answer_question(
        question=question,
        k=k,
        source_filter=selected_source,
        show_chunks=True,
    )

    print("=" * 80)
    print("Question:")
    print(question)

    print("=" * 80)
    print("Selected Paper:")
    print(selected_source)

    print("=" * 80)
    print("Answer:")
    print(answer)

    print("=" * 80)
    print("Retrieved Sources:")
    for i, doc in enumerate(docs, start=1):
        print(
            f"[Source {i}] "
            f"{doc.metadata.get('source')}, "
            f"page {doc.metadata.get('page')}, "
            f"chunk {doc.metadata.get('chunk_id')}"
        )


if __name__ == "__main__":
    main()