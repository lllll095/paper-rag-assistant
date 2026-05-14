from pathlib import Path
import sys
from collections import Counter
from reranker import CrossEncoderReranker

# Make sure we can import rag_engineered.py when running from project root.
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from rag_engineered import EngineeredRAG


OUTPUT_PATH = PROJECT_ROOT / "outputs" / "engineered_rag_eval.md"


TEST_CASES = [
    {
        "name": "Broad overview of AI-generated text detection",
        "question": "What AI-generated text detection methods are discussed in these papers?",
        "expected_behavior": "global",
        "expected_source_keywords": [],
        "min_unique_sources": 2,
    },
    {
        "name": "Specific AdaDetectGPT query",
        "question": "How does AdaDetectGPT work?",
        "expected_behavior": "specific",
        "expected_source_keywords": ["AdaDetectGPT"],
        "min_unique_sources": 1,
    },
    {
        "name": "Specific DetectGPT query",
        "question": "How does DetectGPT detect machine-generated text?",
        "expected_behavior": "specific",
        "expected_source_keywords": ["DetectGPT"],
        "min_unique_sources": 1,
    },
    {
        "name": "Statistical guarantee query",
        "question": "Which methods provide statistical guarantees for AI-generated text detection?",
        "expected_behavior": "global_or_specific",
        "expected_source_keywords": [],
        "min_unique_sources": 1,
    },
    {
        "name": "Comparison between DetectGPT and AdaDetectGPT",
        "question": "What is the difference between DetectGPT and AdaDetectGPT?",
        "expected_behavior": "global",
        "expected_source_keywords": ["DetectGPT", "AdaDetectGPT"],
        "min_unique_sources": 2,
    },
]


NOISY_CHUNK_TYPES = {"checklist", "references", "appendix"}


def get_doc_key(doc):
    return (
        doc.metadata.get("source", "unknown"),
        doc.metadata.get("page", "unknown"),
        doc.metadata.get("chunk_id", "unknown"),
    )


def unique_sources(docs):
    sources = []
    seen = set()

    for doc in docs:
        source = doc.metadata.get("source", "unknown")
        if source not in seen:
            seen.add(source)
            sources.append(source)

    return sources


def count_noisy_chunks(docs):
    count = 0

    for doc in docs:
        chunk_type = doc.metadata.get("chunk_type", "unknown")
        if chunk_type in NOISY_CHUNK_TYPES:
            count += 1

    return count


def source_contains_keywords(source, keywords):
    source_lower = source.lower()

    for keyword in keywords:
        if keyword.lower() in source_lower:
            return True

    return False


def check_expected_sources(docs, expected_keywords):
    """
    Check whether retrieved sources contain expected paper keywords.

    Example:
    expected_keywords = ["AdaDetectGPT"]
    passes if at least one retrieved source filename contains AdaDetectGPT.
    """
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

    return f"Needs inspection. Missing: {missing}"


def check_behavior(actual_mode, expected_behavior):
    """
    Do not make the evaluation too rigid.

    Some questions can reasonably be global or specific depending on the catalog
    and score gap. This function gives a soft check.
    """
    if expected_behavior == "global_or_specific":
        return "Pass"

    if actual_mode == expected_behavior:
        return "Pass"

    return "Needs inspection"


def format_candidate_papers(retrieval_info):
    lines = []

    candidates = retrieval_info.get("candidate_papers", [])

    if not candidates:
        return "No candidate papers returned.\n"

    for i, paper in enumerate(candidates, start=1):
        source = paper.get("source", "unknown")
        title = paper.get("title", "unknown")
        score = paper.get("score", "unknown")

        lines.append(f"{i}. `{source}`")
        lines.append(f"   - Title: {title}")
        lines.append(f"   - Score: `{score}`")
        lines.append("")

    return "\n".join(lines)


def format_selected_papers(retrieval_info):
    lines = []

    selected = retrieval_info.get("selected_papers", [])

    if not selected:
        return "No selected papers returned.\n"

    for i, paper in enumerate(selected, start=1):
        source = paper.get("source", "unknown")
        title = paper.get("title", "unknown")
        score = paper.get("score", "unknown")

        lines.append(f"{i}. `{source}`")
        lines.append(f"   - Title: {title}")
        lines.append(f"   - Score: `{score}`")
        lines.append("")

    return "\n".join(lines)


def format_retrieved_chunks(docs, max_chars=800):
    lines = []

    if not docs:
        return "No chunks retrieved.\n"

    for i, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "unknown")
        page = doc.metadata.get("page", "unknown")
        chunk_id = doc.metadata.get("chunk_id", "unknown")
        chunk_type = doc.metadata.get("chunk_type", "unknown")

        preview = doc.page_content[:max_chars].replace("\n", " ")

        lines.append(f"### Retrieved Chunk {i}")
        lines.append("")
        lines.append(f"- Source: `{source}`")
        lines.append(f"- Page: `{page}`")
        lines.append(f"- Chunk ID: `{chunk_id}`")
        lines.append(f"- Chunk Type: `{chunk_type}`")
        lines.append("")
        lines.append("```text")
        lines.append(preview)
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def summarize_sources(docs):
    sources = [doc.metadata.get("source", "unknown") for doc in docs]
    counter = Counter(sources)

    lines = []

    for source, count in counter.most_common():
        lines.append(f"- `{source}`: {count} chunks")

    return "\n".join(lines)


def evaluate_one_case(rag, case, paper_k=4, chunk_k=8):
    question = case["question"]

    docs, retrieval_info = rag.retrieve(
        query=question,
        paper_k=paper_k,
        chunk_k=chunk_k,
    )

    actual_mode = retrieval_info.get("mode", "unknown")
    expected_behavior = case["expected_behavior"]

    sources = unique_sources(docs)
    noisy_count = count_noisy_chunks(docs)

    behavior_check = check_behavior(actual_mode, expected_behavior)
    source_check = check_expected_sources(
        docs,
        case.get("expected_source_keywords", []),
    )

    min_unique_sources = case.get("min_unique_sources", 1)

    if len(sources) >= min_unique_sources:
        diversity_check = "Pass"
    else:
        diversity_check = (
            f"Needs inspection. Unique sources = {len(sources)}, "
            f"expected at least {min_unique_sources}."
        )

    if noisy_count == 0:
        noise_check = "Pass"
    else:
        noise_check = f"Needs inspection. Noisy chunks = {noisy_count}."

    result = {
        "case": case,
        "docs": docs,
        "retrieval_info": retrieval_info,
        "actual_mode": actual_mode,
        "unique_sources": sources,
        "noisy_count": noisy_count,
        "behavior_check": behavior_check,
        "source_check": source_check,
        "diversity_check": diversity_check,
        "noise_check": noise_check,
    }

    return result


def write_case_report(f, result):
    case = result["case"]
    docs = result["docs"]
    retrieval_info = result["retrieval_info"]

    f.write(f"## {case['name']}\n\n")

    f.write("### Question\n\n")
    f.write(f"{case['question']}\n\n")

    f.write("### Expected Behavior\n\n")
    f.write(f"- Expected retrieval behavior: `{case['expected_behavior']}`\n")
    f.write(f"- Expected source keywords: `{case.get('expected_source_keywords', [])}`\n")
    f.write(f"- Expected minimum unique sources: `{case.get('min_unique_sources', 1)}`\n\n")

    f.write("### Actual Retrieval Summary\n\n")
    f.write(f"- Actual mode: `{result['actual_mode']}`\n")
    f.write(f"- Number of retrieved chunks: `{len(docs)}`\n")
    f.write(f"- Number of unique sources: `{len(result['unique_sources'])}`\n")
    f.write(f"- Number of noisy chunks: `{result['noisy_count']}`\n\n")

    f.write("### Checks\n\n")
    f.write(f"- Behavior check: **{result['behavior_check']}**\n")
    f.write(f"- Expected source check: **{result['source_check']}**\n")
    f.write(f"- Source diversity check: **{result['diversity_check']}**\n")
    f.write(f"- Noise check: **{result['noise_check']}**\n\n")

    f.write("### Candidate Papers\n\n")
    f.write(format_candidate_papers(retrieval_info))
    f.write("\n\n")

    f.write("### Selected Papers\n\n")
    f.write(format_selected_papers(retrieval_info))
    f.write("\n\n")

    f.write("### Retrieved Source Distribution\n\n")
    f.write(summarize_sources(docs))
    f.write("\n\n")

    f.write("### Retrieved Chunks\n\n")
    f.write(format_retrieved_chunks(docs))
    f.write("\n\n")

    f.write("### Manual Observation\n\n")
    f.write("- Are the candidate papers reasonable?\n")
    f.write("- Are the selected papers appropriate for the question?\n")
    f.write("- Are the retrieved chunks actually useful for answering the question?\n")
    f.write("- Are there checklist / references / appendix chunks?\n")
    f.write("- Overall quality: Good / Medium / Poor\n\n")

    f.write("---\n\n")


def main():
    rag = EngineeredRAG()

    OUTPUT_PATH.parent.mkdir(exist_ok=True)

    all_results = []

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("# Engineered RAG Retrieval Evaluation\n\n")
        f.write(
            "This report evaluates the retrieval part of the engineered hierarchical RAG system.\n\n"
        )
        f.write("The evaluation focuses on:\n\n")
        f.write("1. paper-level routing quality;\n")
        f.write("2. whether broad queries retrieve from multiple papers;\n")
        f.write("3. whether specific paper queries retrieve the correct paper;\n")
        f.write("4. whether noisy chunks such as checklist, references, or appendix are avoided.\n\n")
        f.write("---\n\n")

        for case in TEST_CASES:
            print("=" * 80)
            print(f"Running test case: {case['name']}")
            print(f"Question: {case['question']}")

            result = evaluate_one_case(
                rag=rag,
                case=case,
                paper_k=4,
                chunk_k=8,
            )

            all_results.append(result)
            write_case_report(f, result)

        f.write("# Overall Summary\n\n")

        total_cases = len(all_results)
        behavior_pass = sum(1 for r in all_results if r["behavior_check"] == "Pass")
        noise_pass = sum(1 for r in all_results if r["noise_check"] == "Pass")
        source_pass = sum(1 for r in all_results if r["source_check"] == "Pass")
        diversity_pass = sum(1 for r in all_results if r["diversity_check"] == "Pass")

        f.write(f"- Total test cases: `{total_cases}`\n")
        f.write(f"- Behavior check pass: `{behavior_pass}/{total_cases}`\n")
        f.write(f"- Expected source check pass: `{source_pass}/{total_cases}`\n")
        f.write(f"- Source diversity check pass: `{diversity_pass}/{total_cases}`\n")
        f.write(f"- Noise check pass: `{noise_pass}/{total_cases}`\n\n")

        f.write("## Interpretation\n\n")
        f.write(
            "If behavior checks fail, improve the paper-level catalog or the mode decision rule.\n\n"
        )
        f.write(
            "If source checks fail, improve title / abstract extraction or add aliases for method names.\n\n"
        )
        f.write(
            "If noise checks fail, improve chunk_type labeling in build_index.py.\n\n"
        )
        f.write(
            "If candidate papers are correct but retrieved chunks are poor, add a reranker.\n\n"
        )

    print("=" * 80)
    print(f"Evaluation report saved to: {OUTPUT_PATH}")
    print("=" * 80)


if __name__ == "__main__":
    main()