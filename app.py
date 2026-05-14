import sys
from pathlib import Path

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from rag_engineered import EngineeredRAG


st.set_page_config(
    page_title="Paper RAG Assistant",
    page_icon="📚",
    layout="wide",
)


@st.cache_resource
def load_rag_engine():
    """
    Cache the RAG engine so that embedding model, vectorstores,
    BM25 index, and reranker are loaded only once.
    """
    return EngineeredRAG()


def format_score(value):
    if isinstance(value, float):
        return f"{value:.4f}"

    return str(value)


def show_candidate_papers(retrieval_info):
    candidate_papers = retrieval_info.get("candidate_papers", [])

    if not candidate_papers:
        st.info("No candidate papers found.")
        return

    for i, paper in enumerate(candidate_papers, start=1):
        source = paper.get("source", "unknown")
        title = paper.get("title", "unknown")
        score = paper.get("score", "unknown")

        with st.expander(f"Candidate Paper {i}: {source}", expanded=(i == 1)):
            st.write(f"**Title:** {title}")
            st.write(f"**Paper-level score:** `{format_score(score)}`")


def show_selected_papers(retrieval_info):
    selected_papers = retrieval_info.get("selected_papers", [])

    if not selected_papers:
        st.info("No selected papers.")
        return

    for i, paper in enumerate(selected_papers, start=1):
        source = paper.get("source", "unknown")
        title = paper.get("title", "unknown")
        score = paper.get("score", "unknown")

        st.markdown(
            f"""
**{i}. {source}**

- Title: `{title}`
- Paper-level score: `{format_score(score)}`
"""
        )


def show_retrieved_chunks(docs):
    if not docs:
        st.warning("No retrieved chunks.")
        return

    for i, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "unknown")
        page = doc.metadata.get("page", "unknown")
        chunk_id = doc.metadata.get("chunk_id", "unknown")
        chunk_type = doc.metadata.get("chunk_type", "unknown")

        vector_score = doc.metadata.get("vector_score", "unknown")
        bm25_score = doc.metadata.get("bm25_score", "unknown")
        reranker_score = doc.metadata.get("reranker_score", "unknown")

        title = (
            f"Source {i}: {source} | "
            f"page {page} | chunk {chunk_id} | type {chunk_type}"
        )

        with st.expander(title, expanded=(i <= 2)):
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Vector score", format_score(vector_score))

            with col2:
                st.metric("BM25 score", format_score(bm25_score))

            with col3:
                st.metric("Reranker score", format_score(reranker_score))

            st.markdown("**Content preview:**")
            st.write(doc.page_content)


def main():
    st.title("📚 Paper RAG Assistant")
    st.caption(
        "Engineered RAG with paper-level routing, hybrid retrieval, reranking, and source-grounded answers."
    )

    with st.sidebar:
        st.header("Settings")

        paper_k = st.slider(
            "Number of candidate papers",
            min_value=1,
            max_value=10,
            value=4,
            step=1,
        )

        chunk_k = st.slider(
            "Number of final chunks",
            min_value=3,
            max_value=15,
            value=8,
            step=1,
        )

        show_debug = st.checkbox(
            "Show retrieval details",
            value=True,
        )

        st.markdown("---")
        st.markdown(
            """
### Example questions

- What AI-generated text detection methods are discussed in these papers?
- How does AdaDetectGPT work?
- How does DetectGPT detect machine-generated text?
- Which methods provide statistical guarantees?
- What is the difference between DetectGPT and AdaDetectGPT?
"""
        )

    with st.spinner("Loading RAG engine..."):
        rag = load_rag_engine()

    question = st.text_area(
        "Enter your question",
        value="What AI-generated text detection methods are discussed in these papers?",
        height=100,
    )

    run_button = st.button("Run RAG", type="primary")

    if run_button:
        if not question.strip():
            st.warning("Please enter a question.")
            return

        with st.spinner("Retrieving evidence and generating answer..."):
            answer, docs, retrieval_info = rag.answer_question(
                question=question.strip(),
                paper_k=paper_k,
                chunk_k=chunk_k,
                show_debug=False,
            )

        st.markdown("## Answer")
        st.write(answer)

        st.markdown("---")

        mode = retrieval_info.get("mode", "unknown")
        query_route = retrieval_info.get("query_route", {})

        st.markdown("## Retrieval Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Final retrieval mode", mode)

        with col2:
            st.metric("Retrieved chunks", len(docs))

        with col3:
            unique_sources = {
                doc.metadata.get("source", "unknown")
                for doc in docs
            }
            st.metric("Unique sources", len(unique_sources))

        if query_route:
            st.markdown("### Query Route")
            st.json(query_route)

        if show_debug:
            tab1, tab2, tab3 = st.tabs(
                [
                    "Candidate Papers",
                    "Selected Papers",
                    "Retrieved Chunks",
                ]
            )

            with tab1:
                show_candidate_papers(retrieval_info)

            with tab2:
                show_selected_papers(retrieval_info)

            with tab3:
                show_retrieved_chunks(docs)


if __name__ == "__main__":
    main()