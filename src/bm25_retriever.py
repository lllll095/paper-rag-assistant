import re
from typing import List, Optional

from langchain_core.documents import Document
from rank_bm25 import BM25Okapi


class BM25ChunkRetriever:
    """
    BM25 retriever over chunk-level documents.

    It loads documents from the existing Chroma vectorstore, builds a BM25 index
    in memory, and retrieves chunks by lexical keyword matching.

    This complements dense embedding retrieval.
    """

    def __init__(self, chunk_store, has_chunk_type: bool = True):
        self.chunk_store = chunk_store
        self.has_chunk_type = has_chunk_type

        self.documents: List[Document] = []
        self.tokenized_corpus = []
        self.bm25 = None

        self._build_index()

    @staticmethod
    def tokenize(text: str):
        """
        Simple tokenizer for English academic text.

        It keeps words, numbers, and method names such as DetectGPT, GPT-2,
        AUROC, FNR, etc.
        """
        if text is None:
            return []

        if not isinstance(text, str):
            text = str(text)

        text = text.lower()

        tokens = re.findall(r"[a-z0-9][a-z0-9_\-]*", text)

        return tokens

    def _build_index(self):
        """
        Load all chunk documents from Chroma and build a BM25 index.
        """
        print("Building BM25 chunk index from Chroma documents...")

        data = self.chunk_store.get(
            include=["documents", "metadatas"]
        )

        texts = data.get("documents", [])
        metadatas = data.get("metadatas", [])

        documents = []

        for text, metadata in zip(texts, metadatas):
            if not text:
                continue

            metadata = metadata or {}

            if self.has_chunk_type:
                chunk_type = metadata.get("chunk_type", "unknown")
                if chunk_type != "main":
                    continue

            documents.append(
                Document(
                    page_content=text,
                    metadata=dict(metadata),
                )
            )

        if not documents:
            print("Warning: no documents found for BM25 index.")
            self.documents = []
            self.tokenized_corpus = []
            self.bm25 = None
            return

        self.documents = documents
        self.tokenized_corpus = [
            self.tokenize(doc.page_content)
            for doc in self.documents
        ]

        self.bm25 = BM25Okapi(self.tokenized_corpus)

        print(f"BM25 index built. Number of chunks: {len(self.documents)}")

    def search(
        self,
        query: str,
        k: int = 10,
        source_filter: Optional[str] = None,
    ):
        """
        Search BM25 top-k chunks.

        Parameters
        ----------
        query:
            User query.
        k:
            Number of chunks to return.
        source_filter:
            If provided, only return chunks from this PDF source.

        Returns
        -------
        list[Document]
            BM25-ranked documents. Each doc has metadata["bm25_score"].
        """
        if self.bm25 is None or not self.documents:
            return []

        query_tokens = self.tokenize(query)

        if not query_tokens:
            return []

        scores = self.bm25.get_scores(query_tokens)

        candidates = []

        for doc, score in zip(self.documents, scores):
            if source_filter:
                if doc.metadata.get("source") != source_filter:
                    continue

            if score <= 0:
                continue

            # Copy metadata to avoid polluting shared Document objects.
            new_doc = Document(
                page_content=doc.page_content,
                metadata=dict(doc.metadata),
            )
            new_doc.metadata["bm25_score"] = float(score)

            candidates.append((new_doc, float(score)))

        candidates = sorted(
            candidates,
            key=lambda x: x[1],
            reverse=True,
        )

        return [doc for doc, score in candidates[:k]]