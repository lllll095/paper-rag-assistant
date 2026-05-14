from pathlib import Path
import sys
from collections import Counter


CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from rag_engineered import EngineeredRAG


OUTPUT_PATH = PROJECT_ROOT / "outputs" / "reranker_ablation.md"


TEST_CASES = [
    {
        "name": "Broad overview of AI-generated text detection",
        "question": "What AI-generated text detection methods are discussed in these papers?",
    },
    {
        "name": "Specific AdaDetectGPT query",
        "question": "How does AdaDetectGPT work?",
    },
    {
        "name": "Specific DetectGPT query",
        "question": "How does DetectGPT detect machine-generated text?",
    },
    {
        "name": "Statistical guarantee query",
        "question": "Which methods provide statistical guarantees for AI-generated text detection?",
    },
    {
        "name": "Comparison between DetectGPT and AdaDetectGPT",
        "question": "What is the difference between DetectGPT and AdaDetectGPT?",
    },
]


NOISY_CHUNK_TYPES = {"checklist", "references", "appendix"}


def doc_key(doc):
    return (
        doc.metadata.get("source", "unknown"),
        doc.metadata.get("page", "unknown"),
        doc.metadata.get("chunk_id", "unknown"),
    )


def deduplicate_docs_with_scores(doc_score_pairs):
    seen = set()
    unique_pairs = []

    for doc, score in doc_score_pairs:
        key = doc_key(doc)

        if key in seen:
            continue

        seen.add(key)
        unique_pairs.append((doc, score))

    return unique_pairs


def unique_sources(docs):
    seen = set()
    sources = []

    for doc in docs:
        source = doc.metadata.get("source", "unknown")

        if source not in seen:
            seen.add(source)
            sources.append(source)

    return sources


def source_distribution(docs):
    counter = Counter(doc.metadata.get("source", "unknown") for doc in docs)
    return counter


def count_noisy_chunks(docs):
    count = 0

    for doc in docs:
        chunk_type = doc.metadata.get("chunk_type", "unknown")
        if chunk_type in NOISY_CHUNK_TYPES:
            count += 1

    return count


def retrieve_chunks_from_source_vector_only(rag, query, source, k=8):
    """
    Vector-only chunk retrieval from one source.

    This bypasses the reranker and uses Chroma similarity search directly.
    """
    chroma_filter = rag.build_chunk_filter(
        source=source,
        chunk_type="main",
    )

    docs_scores = rag.chunk_store.similarity_search_with_score(
        query,
        k=k,
        filter=chroma_filter,
    )

    docs_scores = deduplicate_docs_with_scores(docs_scores)

    docs = []

    for doc, score in docs_scores[:k]:
        doc.metadata["vector_score"] = float(score)
        doc.metadata.pop("reranker_score", None)
        docs.append(doc)

    return docs


def retrieve_chunks_global_vector_only(
    rag,
    query,
    candidate_papers,
    total_k=8,
    per_paper_k=10,
    max_per_source=3,
):
    """
    Vector-only retrieval from multiple candidate papers.

    It retrieves candidates from each paper, merges them by vector distance,
    and keeps at most max_per_source chunks per paper.
    """
    all_pairs = []

    for paper in candidate_papers:
        source = paper.get("source")

        if not source:
            continue

        chroma_filter = rag.build_chunk_filter(
            source=source,
            chunk_type="main",
        )

        try:
            docs_scores = rag.chunk_store.similarity_search_with_score(
                query,
                k=per_paper_k,
                filter=chroma_filter,
            )

            all_pairs.extend(docs_scores)

        except Exception as e:
            print(f"Vector-only retrieval failed for {source}: {e}")

    all_pairs = deduplicate_docs_with_scores(all_pairs)

    # Chroma score is usually distance: smaller means more similar.
    all_pairs = sorted(all_pairs, key=lambda x: x[1])

    selected_docs = []
    source_counter = {}

    for doc, score in all_pairs:
        source = doc.metadata.get("source", "unknown")

        if source_counter.get(source, 0) >= max_per_source:
            continue

        doc.metadata["vector_score"] = float(score)
        doc.metadata.pop("reranker_score", None)

        selected_docs.append(doc)
        source_counter[source] = source_counter.get(source, 0) + 1

        if len(selected_docs) >= total_k:
            break

    return selected_docs


def retrieve_vector_only(rag, query, paper_k=4, chunk_k=8):
    """
    Full hierarchical retrieval without reranker.

    This uses the same paper-level routing as EngineeredRAG, but bypasses
    cross-encoder reranking at the chunk stage.
    """
    candidate_papers = rag.retrieve_candidate_papers(
        query=query,
        k=paper_k,
    )

    mode = rag.decide_retrieval_mode(
        query=query,
        candidates=candidate_papers,
    )

    if mode == "specific" and candidate_papers:
        selected_papers = candidate_papers[:1]

        docs = retrieve_chunks_from_source_vector_only(
            rag=rag,
            query=query,
            source=selected_papers[0]["source"],
            k=chunk_k,
        )

    else:
        selected_papers = candidate_papers

        docs = retrieve_chunks_global_vector_only(
            rag=rag,
            query=query,
            candidate_papers=selected_papers,
            total_k=chunk_k,
            per_paper_k=10,
            max_per_source=3,
        )

    retrieval_info = {
        "mode": mode,
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


def retrieve_with_reranker(rag, query, paper_k=4, chunk_k=8):
    """
    Full hierarchical retrieval with reranker.

    This calls the current engineered RAG retrieval pipeline.
    """
    docs, retrieval_info = rag.retrieve(
        query=query,
        paper_k=paper_k,
        chunk_k=chunk_k,
    )

    return docs, retrieval_info


def format_candidate_papers(retrieval_info):
    candidates = retrieval_info.get("candidate_papers", [])

    if not candidates:
        return "No candidate papers.\n"

    lines = []

    for i, paper in enumerate(candidates, start=1):
        lines.append(f"{i}. `{paper.get('source', 'unknown')}`")
        lines.append(f"   - Title: {paper.get('title', 'unknown')}")
        lines.append(f"   - Paper score: `{paper.get('score', 'unknown')}`")
        lines.append("")

    return "\n".join(lines)


def format_selected_papers(retrieval_info):
    selected = retrieval_info.get("selected_papers", [])

    if not selected:
        return "No selected papers.\n"

    lines = []

    for i, paper in enumerate(selected, start=1):
        lines.append(f"{i}. `{paper.get('source', 'unknown')}`")
        lines.append(f"   - Title: {paper.get('title', 'unknown')}")
        lines.append(f"   - Paper score: `{paper.get('score', 'unknown')}`")
        lines.append("")

    return "\n".join(lines)


def format_source_distribution(docs):
    counter = source_distribution(docs)

    if not counter:
        return "No retrieved sources.\n"

    lines = []

    for source, count in counter.most_common():
        lines.append(f"- `{source}`: {count} chunks")

    return "\n".join(lines)


def format_docs(docs, max_chars=900):
    if not docs:
        return "No chunks retrieved.\n"

    lines = []

    for i, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "unknown")
        page = doc.metadata.get("page", "unknown")
        chunk_id = doc.metadata.get("chunk_id", "unknown")
        chunk_type = doc.metadata.get("chunk_type", "unknown")
        vector_score = doc.metadata.get("vector_score", "unknown")
        reranker_score = doc.metadata.get("reranker_score", "unknown")

        preview = doc.page_content[:max_chars].replace("\n", " ")

        lines.append(f"### Retrieved Chunk {i}")
        lines.append("")
        lines.append(f"- Source: `{source}`")
        lines.append(f"- Page: `{page}`")
        lines.append(f"- Chunk ID: `{chunk_id}`")
        lines.append(f"- Chunk Type: `{chunk_type}`")
        lines.append(f"- Vector Score: `{vector_score}`")
        lines.append(f"- Reranker Score: `{reranker_score}`")
        lines.append("")
        lines.append("```text")
        lines.append(preview)
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def compare_doc_overlap(vector_docs, reranker_docs):
    vector_keys = {doc_key(doc) for doc in vector_docs}
    reranker_keys = {doc_key(doc) for doc in reranker_docs}

    overlap = vector_keys & reranker_keys

    return {
        "vector_count": len(vector_keys),
        "reranker_count": len(reranker_keys),
        "overlap_count": len(overlap),
    }


def write_one_case_report(
    f,
    case,
    vector_docs,
    vector_info,
    reranker_docs,
    reranker_info,
):
    question = case["question"]

    vector_sources = unique_sources(vector_docs)
    reranker_sources = unique_sources(reranker_docs)

    vector_noisy = count_noisy_chunks(vector_docs)
    reranker_noisy = count_noisy_chunks(reranker_docs)

    overlap_info = compare_doc_overlap(vector_docs, reranker_docs)

    f.write(f"## {case['name']}\n\n")

    f.write("### Question\n\n")
    f.write(f"{question}\n\n")

    f.write("### Retrieval Mode\n\n")
    f.write(f"- Vector-only mode: `{vector_info.get('mode', 'unknown')}`\n")
    f.write(f"- Reranker mode: `{reranker_info.get('mode', 'unknown')}`\n\n")

    f.write("### Candidate Papers\n\n")
    f.write("The candidate papers should be the same or very similar, because both settings use the same paper-level retrieval.\n\n")

    f.write("#### Vector-only Candidate Papers\n\n")
    f.write(format_candidate_papers(vector_info))
    f.write("\n\n")

    f.write("#### Reranker Candidate Papers\n\n")
    f.write(format_candidate_papers(reranker_info))
    f.write("\n\n")

    f.write("### Selected Papers\n\n")

    f.write("#### Vector-only Selected Papers\n\n")
    f.write(format_selected_papers(vector_info))
    f.write("\n\n")

    f.write("#### Reranker Selected Papers\n\n")
    f.write(format_selected_papers(reranker_info))
    f.write("\n\n")

    f.write("### Summary Statistics\n\n")
    f.write("| Metric | Vector-only | With reranker |\n")
    f.write("|---|---:|---:|\n")
    f.write(f"| Retrieved chunks | {len(vector_docs)} | {len(reranker_docs)} |\n")
    f.write(f"| Unique sources | {len(vector_sources)} | {len(reranker_sources)} |\n")
    f.write(f"| Noisy chunks | {vector_noisy} | {reranker_noisy} |\n")
    f.write(f"| Overlap chunks | {overlap_info['overlap_count']} | {overlap_info['overlap_count']} |\n\n")

    f.write("### Source Distribution\n\n")

    f.write("#### Vector-only\n\n")
    f.write(format_source_distribution(vector_docs))
    f.write("\n\n")

    f.write("#### With reranker\n\n")
    f.write(format_source_distribution(reranker_docs))
    f.write("\n\n")

    f.write("### Vector-only Retrieved Chunks\n\n")
    f.write(format_docs(vector_docs))
    f.write("\n\n")

    f.write("### Reranker Retrieved Chunks\n\n")
    f.write(format_docs(reranker_docs))
    f.write("\n\n")

    f.write("### Manual Judgment\n\n")
    f.write("Please inspect the retrieved chunks and fill in:\n\n")
    f.write("- Which setting retrieves more useful chunks?\n")
    f.write("- Does the reranker move more relevant chunks to the top?\n")
    f.write("- Does the reranker reduce checklist / references / appendix noise?\n")
    f.write("- Does the reranker hurt source diversity for broad questions?\n")
    f.write("- Overall winner: Vector-only / Reranker / Tie\n\n")

    f.write("---\n\n")


def main():
    rag = EngineeredRAG()

    OUTPUT_PATH.parent.mkdir(exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("# Reranker Ablation Study\n\n")
        f.write("This report compares two retrieval settings:\n\n")
        f.write("1. **Vector-only retrieval**: paper-level routing + chunk vector search.\n")
        f.write("2. **Reranker retrieval**: paper-level routing + chunk vector search + cross-encoder reranking.\n\n")
        f.write("The goal is to check whether the reranker improves chunk relevance.\n\n")
        f.write("---\n\n")

        for case in TEST_CASES:
            print("=" * 80)
            print(f"Running case: {case['name']}")
            print(f"Question: {case['question']}")

            vector_docs, vector_info = retrieve_vector_only(
                rag=rag,
                query=case["question"],
                paper_k=4,
                chunk_k=8,
            )

            reranker_docs, reranker_info = retrieve_with_reranker(
                rag=rag,
                query=case["question"],
                paper_k=4,
                chunk_k=8,
            )

            write_one_case_report(
                f=f,
                case=case,
                vector_docs=vector_docs,
                vector_info=vector_info,
                reranker_docs=reranker_docs,
                reranker_info=reranker_info,
            )

        f.write("# Overall Notes\n\n")
        f.write("Use this report to decide whether the reranker is actually improving retrieval.\n\n")
        f.write("Common outcomes:\n\n")
        f.write("- If the paper-level candidate papers are wrong, improve `build_paper_catalog.py`.\n")
        f.write("- If candidate papers are right but chunks are poor, improve the reranker or chunking.\n")
        f.write("- If broad queries lose diversity, adjust `max_per_source` or retrieve more candidate papers.\n")
        f.write("- If noisy chunks remain, improve `chunk_type` labeling in `build_index.py`.\n")

    print("=" * 80)
    print(f"Reranker ablation report saved to: {OUTPUT_PATH}")
    print("=" * 80)


if __name__ == "__main__":
    main()