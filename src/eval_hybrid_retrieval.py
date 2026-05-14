from pathlib import Path
import sys
from collections import Counter


CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from rag_engineered import EngineeredRAG


OUTPUT_PATH = PROJECT_ROOT / "outputs" / "hybrid_retrieval_eval.md"


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
        "name": "Logits-related methods",
        "question": "Which methods use logits for AI-generated text detection?",
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


def deduplicate_docs(docs):
    seen = set()
    unique_docs = []

    for doc in docs:
        key = doc_key(doc)
        if key in seen:
            continue

        seen.add(key)
        unique_docs.append(doc)

    return unique_docs


def deduplicate_doc_score_pairs(pairs):
    seen = set()
    unique_pairs = []

    for doc, score in pairs:
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
    return Counter(doc.metadata.get("source", "unknown") for doc in docs)


def count_noisy_chunks(docs):
    return sum(
        1
        for doc in docs
        if doc.metadata.get("chunk_type", "unknown") in NOISY_CHUNK_TYPES
    )


def safe_decide_mode(rag, query, candidates):
    """
    Compatible with either:
    decide_retrieval_mode(query, candidates)
    or
    decide_retrieval_mode(candidates)
    """
    try:
        return rag.decide_retrieval_mode(query=query, candidates=candidates)
    except TypeError:
        return rag.decide_retrieval_mode(candidates)


def get_candidate_and_selected_papers(rag, query, paper_k=4):
    candidates = rag.retrieve_candidate_papers(query=query, k=paper_k)
    mode = safe_decide_mode(rag, query, candidates)

    if mode == "specific" and candidates:
        selected = candidates[:1]
    else:
        selected = candidates

    retrieval_info = {
        "mode": mode,
        "candidate_papers": [
            {
                "source": p.get("source"),
                "title": p.get("title"),
                "score": p.get("score"),
            }
            for p in candidates
        ],
        "selected_papers": [
            {
                "source": p.get("source"),
                "title": p.get("title"),
                "score": p.get("score"),
            }
            for p in selected
        ],
    }

    return candidates, selected, retrieval_info


def retrieve_dense_from_source(rag, query, source, k=8):
    chroma_filter = rag.build_chunk_filter(
        source=source,
        chunk_type="main",
    )

    pairs = rag.chunk_store.similarity_search_with_score(
        query,
        k=k,
        filter=chroma_filter,
    )

    pairs = deduplicate_doc_score_pairs(pairs)

    docs = []

    for doc, score in pairs[:k]:
        doc.metadata["dense_score"] = float(score)
        doc.metadata["vector_score"] = float(score)
        doc.metadata.pop("bm25_score", None)
        doc.metadata.pop("reranker_score", None)
        docs.append(doc)

    return docs


def retrieve_dense_global(
    rag,
    query,
    selected_papers,
    total_k=8,
    per_paper_k=10,
    max_per_source=3,
):
    all_pairs = []

    for paper in selected_papers:
        source = paper.get("source")

        if not source:
            continue

        chroma_filter = rag.build_chunk_filter(
            source=source,
            chunk_type="main",
        )

        try:
            pairs = rag.chunk_store.similarity_search_with_score(
                query,
                k=per_paper_k,
                filter=chroma_filter,
            )
            all_pairs.extend(pairs)

        except Exception as e:
            print(f"Dense retrieval failed for {source}: {e}")

    all_pairs = deduplicate_doc_score_pairs(all_pairs)

    # Chroma score is usually distance: smaller means more similar.
    all_pairs = sorted(all_pairs, key=lambda x: x[1])

    selected_docs = []
    source_counter = {}

    for doc, score in all_pairs:
        source = doc.metadata.get("source", "unknown")

        if source_counter.get(source, 0) >= max_per_source:
            continue

        doc.metadata["dense_score"] = float(score)
        doc.metadata["vector_score"] = float(score)
        doc.metadata.pop("bm25_score", None)
        doc.metadata.pop("reranker_score", None)

        selected_docs.append(doc)
        source_counter[source] = source_counter.get(source, 0) + 1

        if len(selected_docs) >= total_k:
            break

    return selected_docs


def retrieve_dense_only(rag, query, paper_k=4, chunk_k=8):
    candidates, selected_papers, retrieval_info = get_candidate_and_selected_papers(
        rag=rag,
        query=query,
        paper_k=paper_k,
    )

    if retrieval_info["mode"] == "specific" and selected_papers:
        docs = retrieve_dense_from_source(
            rag=rag,
            query=query,
            source=selected_papers[0]["source"],
            k=chunk_k,
        )
    else:
        docs = retrieve_dense_global(
            rag=rag,
            query=query,
            selected_papers=selected_papers,
            total_k=chunk_k,
            per_paper_k=10,
            max_per_source=3,
        )

    return docs, retrieval_info


def retrieve_bm25_from_source(rag, query, source, k=8):
    docs = rag.bm25_retriever.search(
        query=query,
        k=k,
        source_filter=source,
    )

    for doc in docs:
        doc.metadata.pop("dense_score", None)
        doc.metadata.pop("vector_score", None)
        doc.metadata.pop("reranker_score", None)

    return docs


def retrieve_bm25_global(
    rag,
    query,
    selected_papers,
    total_k=8,
    per_paper_k=10,
    max_per_source=3,
):
    all_docs = []

    for paper in selected_papers:
        source = paper.get("source")

        if not source:
            continue

        try:
            docs = rag.bm25_retriever.search(
                query=query,
                k=per_paper_k,
                source_filter=source,
            )
            all_docs.extend(docs)

        except Exception as e:
            print(f"BM25 retrieval failed for {source}: {e}")

    all_docs = deduplicate_docs(all_docs)

    # BM25 score: larger means more relevant.
    all_docs = sorted(
        all_docs,
        key=lambda doc: doc.metadata.get("bm25_score", 0.0),
        reverse=True,
    )

    selected_docs = []
    source_counter = {}

    for doc in all_docs:
        source = doc.metadata.get("source", "unknown")

        if source_counter.get(source, 0) >= max_per_source:
            continue

        selected_docs.append(doc)
        source_counter[source] = source_counter.get(source, 0) + 1

        if len(selected_docs) >= total_k:
            break

    return selected_docs


def retrieve_bm25_only(rag, query, paper_k=4, chunk_k=8):
    candidates, selected_papers, retrieval_info = get_candidate_and_selected_papers(
        rag=rag,
        query=query,
        paper_k=paper_k,
    )

    if retrieval_info["mode"] == "specific" and selected_papers:
        docs = retrieve_bm25_from_source(
            rag=rag,
            query=query,
            source=selected_papers[0]["source"],
            k=chunk_k,
        )
    else:
        docs = retrieve_bm25_global(
            rag=rag,
            query=query,
            selected_papers=selected_papers,
            total_k=chunk_k,
            per_paper_k=10,
            max_per_source=3,
        )

    return docs, retrieval_info


def retrieve_hybrid_reranker(rag, query, paper_k=4, chunk_k=8):
    """
    Current engineered RAG pipeline:
    paper routing + dense retrieval + BM25 retrieval + merge + reranker.
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

        dense_score = doc.metadata.get("dense_score", "unknown")
        vector_score = doc.metadata.get("vector_score", "unknown")
        bm25_score = doc.metadata.get("bm25_score", "unknown")
        reranker_score = doc.metadata.get("reranker_score", "unknown")

        preview = doc.page_content[:max_chars].replace("\n", " ")

        lines.append(f"### Retrieved Chunk {i}")
        lines.append("")
        lines.append(f"- Source: `{source}`")
        lines.append(f"- Page: `{page}`")
        lines.append(f"- Chunk ID: `{chunk_id}`")
        lines.append(f"- Chunk Type: `{chunk_type}`")
        lines.append(f"- Dense Score: `{dense_score}`")
        lines.append(f"- Vector Score: `{vector_score}`")
        lines.append(f"- BM25 Score: `{bm25_score}`")
        lines.append(f"- Reranker Score: `{reranker_score}`")
        lines.append("")
        lines.append("```text")
        lines.append(preview)
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def compare_overlap(docs_a, docs_b):
    keys_a = {doc_key(doc) for doc in docs_a}
    keys_b = {doc_key(doc) for doc in docs_b}

    return len(keys_a & keys_b)


def write_method_summary_table(f, dense_docs, bm25_docs, hybrid_docs):
    dense_sources = unique_sources(dense_docs)
    bm25_sources = unique_sources(bm25_docs)
    hybrid_sources = unique_sources(hybrid_docs)

    dense_noisy = count_noisy_chunks(dense_docs)
    bm25_noisy = count_noisy_chunks(bm25_docs)
    hybrid_noisy = count_noisy_chunks(hybrid_docs)

    f.write("### Summary Statistics\n\n")
    f.write("| Metric | Dense only | BM25 only | Hybrid + reranker |\n")
    f.write("|---|---:|---:|---:|\n")
    f.write(f"| Retrieved chunks | {len(dense_docs)} | {len(bm25_docs)} | {len(hybrid_docs)} |\n")
    f.write(f"| Unique sources | {len(dense_sources)} | {len(bm25_sources)} | {len(hybrid_sources)} |\n")
    f.write(f"| Noisy chunks | {dense_noisy} | {bm25_noisy} | {hybrid_noisy} |\n")
    f.write(
        f"| Overlap with hybrid | "
        f"{compare_overlap(dense_docs, hybrid_docs)} | "
        f"{compare_overlap(bm25_docs, hybrid_docs)} | "
        f"{len({doc_key(doc) for doc in hybrid_docs})} |\n\n"
    )


def write_case_report(
    f,
    case,
    dense_docs,
    dense_info,
    bm25_docs,
    bm25_info,
    hybrid_docs,
    hybrid_info,
):
    question = case["question"]

    f.write(f"## {case['name']}\n\n")

    f.write("### Question\n\n")
    f.write(f"{question}\n\n")

    f.write("### Retrieval Modes\n\n")
    f.write(f"- Dense-only mode: `{dense_info.get('mode', 'unknown')}`\n")
    f.write(f"- BM25-only mode: `{bm25_info.get('mode', 'unknown')}`\n")
    f.write(f"- Hybrid mode: `{hybrid_info.get('mode', 'unknown')}`\n\n")

    f.write("### Candidate Papers\n\n")
    f.write("These should usually be similar because all three settings use the same paper-level routing.\n\n")

    f.write("#### Hybrid Candidate Papers\n\n")
    f.write(format_candidate_papers(hybrid_info))
    f.write("\n\n")

    f.write("### Selected Papers\n\n")

    f.write("#### Dense-only Selected Papers\n\n")
    f.write(format_selected_papers(dense_info))
    f.write("\n\n")

    f.write("#### BM25-only Selected Papers\n\n")
    f.write(format_selected_papers(bm25_info))
    f.write("\n\n")

    f.write("#### Hybrid Selected Papers\n\n")
    f.write(format_selected_papers(hybrid_info))
    f.write("\n\n")

    write_method_summary_table(
        f=f,
        dense_docs=dense_docs,
        bm25_docs=bm25_docs,
        hybrid_docs=hybrid_docs,
    )

    f.write("### Source Distribution\n\n")

    f.write("#### Dense only\n\n")
    f.write(format_source_distribution(dense_docs))
    f.write("\n\n")

    f.write("#### BM25 only\n\n")
    f.write(format_source_distribution(bm25_docs))
    f.write("\n\n")

    f.write("#### Hybrid + reranker\n\n")
    f.write(format_source_distribution(hybrid_docs))
    f.write("\n\n")

    f.write("### Dense-only Retrieved Chunks\n\n")
    f.write(format_docs(dense_docs))
    f.write("\n\n")

    f.write("### BM25-only Retrieved Chunks\n\n")
    f.write(format_docs(bm25_docs))
    f.write("\n\n")

    f.write("### Hybrid + Reranker Retrieved Chunks\n\n")
    f.write(format_docs(hybrid_docs))
    f.write("\n\n")

    f.write("### Manual Judgment\n\n")
    f.write("Please inspect the retrieved chunks and fill in:\n\n")
    f.write("- Which setting retrieves the most useful chunks?\n")
    f.write("- Does BM25 help with method names, abbreviations, or technical terms?\n")
    f.write("- Does dense retrieval help with semantic but non-exact matches?\n")
    f.write("- Does hybrid + reranker combine the advantages of both?\n")
    f.write("- Does hybrid retrieval reduce or increase noise?\n")
    f.write("- Overall winner: Dense only / BM25 only / Hybrid + reranker / Tie\n\n")

    f.write("---\n\n")


def main():
    rag = EngineeredRAG()

    OUTPUT_PATH.parent.mkdir(exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("# Hybrid Retrieval Evaluation\n\n")
        f.write("This report compares three retrieval settings:\n\n")
        f.write("1. **Dense only**: paper routing + embedding-based chunk retrieval.\n")
        f.write("2. **BM25 only**: paper routing + keyword-based chunk retrieval.\n")
        f.write("3. **Hybrid + reranker**: paper routing + dense retrieval + BM25 retrieval + cross-encoder reranking.\n\n")
        f.write("The goal is to understand whether hybrid retrieval improves recall and chunk relevance.\n\n")
        f.write("---\n\n")

        for case in TEST_CASES:
            print("=" * 80)
            print(f"Running case: {case['name']}")
            print(f"Question: {case['question']}")

            dense_docs, dense_info = retrieve_dense_only(
                rag=rag,
                query=case["question"],
                paper_k=4,
                chunk_k=8,
            )

            bm25_docs, bm25_info = retrieve_bm25_only(
                rag=rag,
                query=case["question"],
                paper_k=4,
                chunk_k=8,
            )

            hybrid_docs, hybrid_info = retrieve_hybrid_reranker(
                rag=rag,
                query=case["question"],
                paper_k=4,
                chunk_k=8,
            )

            write_case_report(
                f=f,
                case=case,
                dense_docs=dense_docs,
                dense_info=dense_info,
                bm25_docs=bm25_docs,
                bm25_info=bm25_info,
                hybrid_docs=hybrid_docs,
                hybrid_info=hybrid_info,
            )

        f.write("# Overall Notes\n\n")
        f.write("Use this report to decide whether hybrid retrieval improves your RAG system.\n\n")
        f.write("Typical patterns:\n\n")
        f.write("- If BM25 performs well on exact method names, keep it for keyword recall.\n")
        f.write("- If dense retrieval performs better on conceptual questions, keep dense retrieval for semantic recall.\n")
        f.write("- If hybrid + reranker consistently ranks better chunks near the top, it should be the default retrieval pipeline.\n")
        f.write("- If hybrid retrieval loses source diversity, adjust `max_per_source`.\n")
        f.write("- If all methods retrieve poor chunks, improve paper catalog, chunking, or chunk_type labeling.\n")

    print("=" * 80)
    print(f"Hybrid retrieval evaluation saved to: {OUTPUT_PATH}")
    print("=" * 80)


if __name__ == "__main__":
    main()