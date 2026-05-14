from sentence_transformers.cross_encoder import CrossEncoder


class CrossEncoderReranker:
    """
    A simple cross-encoder reranker.

    It takes a query and a list of LangChain Document objects,
    scores each query-document pair, and returns documents sorted
    by reranker score.
    """

    def __init__(self, model_name="cross-encoder/ms-marco-MiniLM-L6-v2"):
        print(f"Loading reranker model: {model_name}")
        self.model = CrossEncoder(model_name)

    @staticmethod
    def truncate_text(text, max_chars=1800):
        """
        Avoid feeding extremely long chunks into the reranker.
        """
        if text is None:
            return ""

        if not isinstance(text, str):
            text = str(text)

        return text[:max_chars]

    def rerank(self, query, docs, top_k=8):
        """
        Rerank retrieved documents.

        Parameters
        ----------
        query : str
            User question.
        docs : list[Document]
            Candidate chunks returned by vector search.
        top_k : int
            Number of final chunks to keep.

        Returns
        -------
        list[Document]
            Reranked documents with reranker_score stored in metadata.
        """
        if not docs:
            return []

        pairs = []

        for doc in docs:
            text = self.truncate_text(doc.page_content)
            pairs.append([query, text])

        scores = self.model.predict(pairs)

        scored_docs = []

        for doc, score in zip(docs, scores):
            doc.metadata["reranker_score"] = float(score)
            scored_docs.append((doc, float(score)))

        scored_docs = sorted(
            scored_docs,
            key=lambda x: x[1],
            reverse=True,
        )

        return [doc for doc, score in scored_docs[:top_k]]