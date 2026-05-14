from pathlib import Path
import sys
from dataclasses import asdict
from collections import Counter


CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from query_router import QueryRouter
from rag_engineered import EngineeredRAG


OUTPUT_PATH = PROJECT_ROOT / "outputs" / "query_router_eval.md"


TEST_CASES = [
    {
        "name": "Specific method question: AdaDetectGPT",
        "question": "How does AdaDetectGPT work?",
        "expected_query_type": "method",
        "expected_retrieval_mode": "auto",
        "expected_source_keywords": ["AdaDetectGPT"],
        "min_unique_sources": 1,
    },
    {
        "name": "Specific method question: DetectGPT",
        "question": "How does DetectGPT detect machine-generated text?",
        "expected_query_type": "method",
        "expected_retrieval_mode": "auto",
        "expected_source_keywords": ["DetectGPT"],
        "min_unique_sources": 1,
    },
    {
        "name": "Survey question",
        "question": "What AI-generated text detection methods are discussed in these papers?",
        "expected_query_type": "survey",
        "expected_retrieval_mode": "global",
        "expected_source_keywords": [],
        "min_unique_sources": 2,
    },
    {
        "name": "Comparison question",
        "question": "What is the difference between DetectGPT and AdaDetectGPT?",
        "expected_query_type": "comparison",
        "expected_retrieval_mode": "global",
        "expected_source_keywords": ["DetectGPT", "AdaDetectGPT"],
        "min_unique_sources": 2,
    },
    {
        "name": "Evidence / statistical guarantee question",
        "question": "Which methods provide statistical guarantees for AI-generated text detection?",
        "expected_query_type": "evidence",
        "expected_retrieval_mode": "global",
        "expected_source_keywords": [],
        "min_unique_sources": 1,
    },
    {
        "name": "Experiment question",
        "question": "What datasets and evaluation metrics are used in these papers?",
        "expected_query_type": "experiment",
        "expected_retrieval_mode": "global",
        "expected_source_keywords": [],
        "min_unique_sources": 2,
    },
    {
        "name": "Logits question",
        "question": "Which methods use logits for AI-generated text detection?",
        "expected_query_type": "general",
        "expected_retrieval_mode": "auto",
        "expected_source_keywords": [],
        "min_unique_sources": 1,
    },
    {
        "name": "Chinese survey question",
        "question": "这些论文里有哪些 AI 生成文本检测方法？",
        "expected_query_type": "survey",
        "expected_retrieval_mode": "global",
        "expected_source_keywords": [],
        "min_unique_sources": 2,
    },
    {
        "name": "Chinese comparison question",
        "question": "DetectGPT 和 AdaDetectGPT 有什么区别？",
        "expected_query_type": "comparison",
        "expected_retrieval_mode": "global",
        "expected_source_keywords": ["DetectGPT", "AdaDetectGPT"],
        "min_unique_sources": 2,
    },
]


NOISY_CHUNK_TYPES = {"checklist", "references", "appendix"}


def doc_key(doc):
    return (
        doc.metadata.get("source", "unknown"),
        doc.metadata.get("page", "unknown"),
        doc.metadata.get("chunk_id", "unknown"),
    )


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


def check_query_type(actual, expected):
    if actual == expected:
        return "Pass"

    return f"Needs inspection. Expected `{expected}`, got `{actual}`."


def check_retrieval_mode(actual, expected):
    """
    This checks the router's intended retrieval mode, not the final RAG mode.

    For expected_retrieval_mode = auto, the final RAG mode can become
    specific or global depending on paper-level retrieval scores.
    """
    if actual == expected:
        return "Pass"

    return f"Needs inspection. Expected `{expected}`, got `{actual}`."


def check_expected_sources(docs, expected_keywords):
    if not expected_keywords:
        return "Not required"

    sources = unique_sources(docs)
    missing = []

    for keyword in expected_keywords:
        found = any(keyword.lower() in source.lower() for source in sources)
        if not found:
            missing.append(keyword)

    if not missing:
        return "Pass"

    return f"Needs inspection. Missing source keyword(s): {missing}"


def check_source_diversity(docs, min_unique_sources):
    sources = unique_sources(docs)

    if len(sources) >= min_unique_sources:
        return "Pass"

    return (
        f"Needs inspection. Unique sources = {len(sources)}, "
        f"expected at least {min_unique_sources}."
    )


def check_noise(docs):
    noisy = count_noisy_chunks(docs)

    if noisy == 0:
        return "Pass"

    return f"Needs inspection. Noisy chunks = {noisy}."


def format_route(route):
    route_dict = asdict(route)

    lines = []

    for key, value in route_dict.items():
        lines.append(f"- {key}: `{value}`")

    return "\n".join(lines)


def format_candidate_papers(retrieval_info):
    candidates = retrieval_info.get("candidate_papers", [])

    if not candidates:
        return "No candidate papers.\n"

    lines = []

    for i, paper in enumerate(candidates, start=1):
        lines.append(f"{i}. `{paper.get('source', 'unknown')}`")
        lines.append(f"   - Title: {paper.get('title', 'unknown')}")
        lines.append(f"   - Score: `{paper.get('score', 'unknown')}`")
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
        lines.append(f"   - Score: `{paper.get('score', 'unknown')}`")
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
        dense_score = doc.metadata.get("dense_score", "unknown")
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


def evaluate_one_case(router, rag, case):
    question = case["question"]

    route = router.route(question)

    docs, retrieval_info = rag.retrieve(
        query=question,
        paper_k=route.paper_k,
        chunk_k=route.chunk_k,
    )

    actual_query_type = route.query_type
    actual_router_mode = route.retrieval_mode
    actual_rag_mode = retrieval_info.get("mode", "unknown")

    query_type_check = check_query_type(
        actual=actual_query_type,
        expected=case["expected_query_type"],
    )

    router_mode_check = check_retrieval_mode(
        actual=actual_router_mode,
        expected=case["expected_retrieval_mode"],
    )

    source_check = check_expected_sources(
        docs=docs,
        expected_keywords=case.get("expected_source_keywords", []),
    )

    diversity_check = check_source_diversity(
        docs=docs,
        min_unique_sources=case.get("min_unique_sources", 1),
    )

    noise_check = check_noise(docs)

    return {
        "case": case,
        "route": route,
        "docs": docs,
        "retrieval_info": retrieval_info,
        "actual_query_type": actual_query_type,
        "actual_router_mode": actual_router_mode,
        "actual_rag_mode": actual_rag_mode,
        "query_type_check": query_type_check,
        "router_mode_check": router_mode_check,
        "source_check": source_check,
        "diversity_check": diversity_check,
        "noise_check": noise_check,
    }


def write_case_report(f, result):
    case = result["case"]
    docs = result["docs"]
    retrieval_info = result["retrieval_info"]

    f.write(f"## {case['name']}\n\n")

    f.write("### Question\n\n")
    f.write(f"{case['question']}\n\n")

    f.write("### Expected\n\n")
    f.write(f"- Expected query type: `{case['expected_query_type']}`\n")
    f.write(f"- Expected router retrieval mode: `{case['expected_retrieval_mode']}`\n")
    f.write(f"- Expected source keywords: `{case.get('expected_source_keywords', [])}`\n")
    f.write(f"- Expected minimum unique sources: `{case.get('min_unique_sources', 1)}`\n\n")

    f.write("### Router Output\n\n")
    f.write(format_route(result["route"]))
    f.write("\n\n")

    f.write("### Actual Retrieval Summary\n\n")
    f.write(f"- Actual query type: `{result['actual_query_type']}`\n")
    f.write(f"- Actual router retrieval mode: `{result['actual_router_mode']}`\n")
    f.write(f"- Actual final RAG mode: `{result['actual_rag_mode']}`\n")
    f.write(f"- Number of retrieved chunks: `{len(docs)}`\n")
    f.write(f"- Number of unique sources: `{len(unique_sources(docs))}`\n")
    f.write(f"- Number of noisy chunks: `{count_noisy_chunks(docs)}`\n\n")

    f.write("### Checks\n\n")
    f.write(f"- Query type check: **{result['query_type_check']}**\n")
    f.write(f"- Router mode check: **{result['router_mode_check']}**\n")
    f.write(f"- Expected source check: **{result['source_check']}**\n")
    f.write(f"- Source diversity check: **{result['diversity_check']}**\n")
    f.write(f"- Noise check: **{result['noise_check']}**\n\n")

    f.write("### Candidate Papers\n\n")
    f.write(format_candidate_papers(retrieval_info))
    f.write("\n\n")

    f.write("### Selected Papers\n\n")
    f.write(format_selected_papers(retrieval_info))
    f.write("\n\n")

    f.write("### Source Distribution\n\n")
    f.write(format_source_distribution(docs))
    f.write("\n\n")

    f.write("### Retrieved Chunks\n\n")
    f.write(format_docs(docs))
    f.write("\n\n")

    f.write("### Manual Observation\n\n")
    f.write("- Is the router classification reasonable?\n")
    f.write("- Did the route choose suitable retrieval parameters?\n")
    f.write("- Are the selected papers appropriate?\n")
    f.write("- Are the retrieved chunks useful for answering the question?\n")
    f.write("- Overall quality: Good / Medium / Poor\n\n")

    f.write("---\n\n")


def main():
    router = QueryRouter()
    rag = EngineeredRAG()

    OUTPUT_PATH.parent.mkdir(exist_ok=True)

    all_results = []

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("# Query Router Evaluation\n\n")
        f.write("This report evaluates the query router and its effect on retrieval.\n\n")
        f.write("The evaluation checks:\n\n")
        f.write("1. whether the query type is classified correctly;\n")
        f.write("2. whether the router chooses the intended retrieval mode;\n")
        f.write("3. whether the retrieved sources match the question;\n")
        f.write("4. whether broad queries retrieve from multiple papers;\n")
        f.write("5. whether noisy chunks are avoided.\n\n")
        f.write("---\n\n")

        for case in TEST_CASES:
            print("=" * 80)
            print(f"Running case: {case['name']}")
            print(f"Question: {case['question']}")

            result = evaluate_one_case(
                router=router,
                rag=rag,
                case=case,
            )

            all_results.append(result)
            write_case_report(f, result)

        total = len(all_results)

        query_type_pass = sum(
            1 for r in all_results if r["query_type_check"] == "Pass"
        )
        router_mode_pass = sum(
            1 for r in all_results if r["router_mode_check"] == "Pass"
        )
        source_pass = sum(
            1 for r in all_results if r["source_check"] in ["Pass", "Not required"]
        )
        diversity_pass = sum(
            1 for r in all_results if r["diversity_check"] == "Pass"
        )
        noise_pass = sum(
            1 for r in all_results if r["noise_check"] == "Pass"
        )

        f.write("# Overall Summary\n\n")
        f.write(f"- Total cases: `{total}`\n")
        f.write(f"- Query type check pass: `{query_type_pass}/{total}`\n")
        f.write(f"- Router mode check pass: `{router_mode_pass}/{total}`\n")
        f.write(f"- Source check pass: `{source_pass}/{total}`\n")
        f.write(f"- Source diversity check pass: `{diversity_pass}/{total}`\n")
        f.write(f"- Noise check pass: `{noise_pass}/{total}`\n\n")

        f.write("## Interpretation\n\n")
        f.write("- If query type checks fail, improve `query_router.py` patterns.\n")
        f.write("- If source checks fail, improve paper catalog or named-paper routing.\n")
        f.write("- If diversity checks fail, tune `paper_k`, `chunk_k`, and `max_per_source`.\n")
        f.write("- If noise checks fail, improve `chunk_type` labeling or filters.\n")

    print("=" * 80)
    print(f"Query router evaluation saved to: {OUTPUT_PATH}")
    print("=" * 80)


if __name__ == "__main__":
    main()