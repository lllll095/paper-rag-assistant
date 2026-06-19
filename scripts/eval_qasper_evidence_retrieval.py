"""
Evaluate QASPER evidence retrieval with the real EngineeredRAG pipeline.

This script evaluates whether Paper RAG Assistant can retrieve QASPER gold
evidence paragraphs / highlighted evidence from long scientific papers.

It uses:
- local QASPER v0.3 JSON files
- QASPER project-compatible Chroma indexes built by:
  python scripts/build_qasper_project_index.py --split dev
- the real EngineeredRAG.retrieve() pipeline

Run quick test:

python scripts/eval_qasper_evidence_retrieval.py --split dev --limit_examples 20

Run full dev evaluation:

python scripts/eval_qasper_evidence_retrieval.py --split dev
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from tqdm import tqdm


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import rag_engineered  # noqa: E402
from rag_engineered import EngineeredRAG  # noqa: E402


QASPER_RAW_DIR = PROJECT_ROOT / "eval" / "qasper_raw"
QASPER_INDEX_DIR = PROJECT_ROOT / "eval" / "qasper_project_index"

QASPER_CHUNK_DB_DIR = QASPER_INDEX_DIR / "chunk_db"
QASPER_CATALOG_DB_DIR = QASPER_INDEX_DIR / "paper_catalog_db"

OUTPUT_DIR = PROJECT_ROOT / "eval" / "results"

SPLIT_FILES = {
    "train": QASPER_RAW_DIR / "qasper-train-v0.3.json",
    "dev": QASPER_RAW_DIR / "qasper-dev-v0.3.json",
    "test": QASPER_RAW_DIR / "qasper-test-v0.3.json",
}


def normalize_text(text: str) -> str:
    """Normalize text for evidence matching."""

    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def token_set(text: str) -> set[str]:
    """Convert normalized text into token set."""

    return set(normalize_text(text).split())


def jaccard(a: str, b: str) -> float:
    """Token-level Jaccard similarity."""

    a_tokens = token_set(a)
    b_tokens = token_set(b)

    if not a_tokens or not b_tokens:
        return 0.0

    return len(a_tokens & b_tokens) / len(a_tokens | b_tokens)


def sequence_ratio(a: str, b: str) -> float:
    """Character-level fuzzy matching ratio after normalization."""

    a_norm = normalize_text(a)
    b_norm = normalize_text(b)

    if not a_norm or not b_norm:
        return 0.0

    return SequenceMatcher(None, a_norm, b_norm).ratio()


def evidence_match_score(retrieved_text: str, gold_text: str) -> float:
    """Compute a robust matching score between retrieved chunk and gold evidence.

    QASPER evidence is often a paragraph or highlighted sentence. Since our
    chunk text contains title + section + paragraph, exact substring matching
    is often possible, but we also use fuzzy matching for robustness.
    """

    retrieved_norm = normalize_text(retrieved_text)
    gold_norm = normalize_text(gold_text)

    if not retrieved_norm or not gold_norm:
        return 0.0

    # Exact containment is the strongest signal.
    if gold_norm in retrieved_norm:
        return 1.0

    # Sometimes the retrieved chunk is almost the same paragraph with section text.
    jac = jaccard(retrieved_text, gold_text)
    ratio = sequence_ratio(retrieved_text, gold_text)

    return max(jac, ratio)


def is_evidence_hit(
    retrieved_text: str,
    gold_evidence_items: list[str],
    threshold: float,
) -> tuple[bool, float, str]:
    """Check whether a retrieved chunk matches any gold evidence item."""

    best_score = 0.0
    best_gold = ""

    for gold in gold_evidence_items:
        if not isinstance(gold, str) or not gold.strip():
            continue

        score = evidence_match_score(retrieved_text, gold)

        if score > best_score:
            best_score = score
            best_gold = gold

    return best_score >= threshold, best_score, best_gold


def load_qasper_split(split: str) -> dict[str, Any]:
    """Load local QASPER split."""

    path = SPLIT_FILES[split]

    if not path.exists():
        raise FileNotFoundError(f"QASPER split file not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise TypeError(f"Expected top-level dict, got {type(data)}")

    return data


def get_answer_payload(answer_item: dict[str, Any]) -> dict[str, Any]:
    """Extract inner QASPER answer payload."""

    inner = answer_item.get("answer")
    if isinstance(inner, dict):
        return inner
    return answer_item


def collect_qasper_examples(
    data: dict[str, Any],
    include_unanswerable: bool = False,
) -> list[dict[str, Any]]:
    """Collect QA examples with evidence from QASPER."""

    examples: list[dict[str, Any]] = []

    for paper_id, paper in data.items():
        if not isinstance(paper, dict):
            continue

        qas = paper.get("qas", [])
        if not isinstance(qas, list):
            continue

        for qa in qas:
            if not isinstance(qa, dict):
                continue

            question = qa.get("question", "")
            question_id = qa.get("question_id", "")
            answers = qa.get("answers", [])

            if not isinstance(answers, list):
                continue

            for answer_idx, answer_item in enumerate(answers):
                if not isinstance(answer_item, dict):
                    continue

                payload = get_answer_payload(answer_item)

                if payload.get("unanswerable") is True and not include_unanswerable:
                    continue

                evidence = payload.get("evidence", [])
                highlighted = payload.get("highlighted_evidence", [])

                if not isinstance(evidence, list):
                    evidence = []

                if not isinstance(highlighted, list):
                    highlighted = []

                if not evidence and not highlighted:
                    continue

                examples.append(
                    {
                        "paper_id": str(paper_id),
                        "title": paper.get("title", ""),
                        "question_id": str(question_id),
                        "answer_idx": answer_idx,
                        "question": str(question),
                        "free_form_answer": payload.get("free_form_answer", ""),
                        "extractive_spans": payload.get("extractive_spans", []),
                        "yes_no": payload.get("yes_no"),
                        "evidence": evidence,
                        "highlighted_evidence": highlighted,
                    }
                )

    return examples


def patch_qasper_paths() -> None:
    """Patch project index paths to QASPER index."""

    rag_engineered.CHUNK_DB_DIR = QASPER_CHUNK_DB_DIR
    rag_engineered.CATALOG_DB_DIR = QASPER_CATALOG_DB_DIR


def docs_to_ids_and_texts(docs: list[Any], top_k: int) -> list[dict[str, Any]]:
    """Convert retrieved LangChain docs into lightweight records."""

    records = []

    for rank, doc in enumerate(docs[:top_k], start=1):
        metadata = getattr(doc, "metadata", {}) or {}
        content = getattr(doc, "page_content", "") or ""

        records.append(
            {
                "rank": rank,
                "source": str(metadata.get("source", "")),
                "paper_id": str(metadata.get("paper_id", metadata.get("source", ""))),
                "paragraph_id": metadata.get("paragraph_id"),
                "section_name": metadata.get("section_name"),
                "chunk_id": metadata.get("chunk_id"),
                "reranker_score": metadata.get("reranker_score"),
                "bm25_score": metadata.get("bm25_score"),
                "vector_score": metadata.get("vector_score"),
                "content": content,
            }
        )

    return records


def evaluate_examples(
    rag: Any,
    examples: list[dict[str, Any]],
    top_k: int,
    paper_k: int,
    chunk_k: int,
    match_threshold: float,
    oracle_paper: bool = False,
    debug_examples: int = 3,
) -> tuple[dict[str, float], list[dict[str, Any]]]:
    """Evaluate QASPER evidence retrieval examples."""

    details: list[dict[str, Any]] = []

    paper_hit_count = 0
    evidence_hit_count = 0
    highlighted_hit_count = 0

    best_evidence_scores = []
    best_highlighted_scores = []

    for idx, ex in enumerate(tqdm(examples, desc="QASPER evidence retrieval")):
        if oracle_paper:
            docs = rag.retrieve_chunks_from_source(
                query=ex["question"],
                source=ex["paper_id"],
                k=chunk_k,
                fetch_k=max(20, chunk_k * 3),
            )

            retrieval_info = {
                "mode": "oracle_paper",
                "gold_paper_id": ex["paper_id"],
                "selected_papers": [
                    {
                        "source": ex["paper_id"],
                        "title": ex["title"],
                        "score": None,
                    }
                ],
                "paper_k": None,
                "chunk_k": chunk_k,
            }
        else:
            docs, retrieval_info = rag.retrieve(
                query=ex["question"],
                paper_k=paper_k,
                chunk_k=chunk_k,
            )

        retrieved = docs_to_ids_and_texts(docs, top_k=top_k)

        gold_paper_id = ex["paper_id"]
        retrieved_paper_ids = [item["paper_id"] for item in retrieved]

        paper_hit = gold_paper_id in retrieved_paper_ids

        if paper_hit:
            paper_hit_count += 1

        evidence_items = [str(x) for x in ex.get("evidence", []) if str(x).strip()]
        highlighted_items = [
            str(x)
            for x in ex.get("highlighted_evidence", [])
            if str(x).strip()
        ]

        example_best_evidence_score = 0.0
        example_best_highlighted_score = 0.0
        evidence_hit = False
        highlighted_hit = False
        matched_evidence = ""
        matched_highlighted = ""

        for item in retrieved:
            hit, score, best_gold = is_evidence_hit(
                retrieved_text=item["content"],
                gold_evidence_items=evidence_items,
                threshold=match_threshold,
            )
            if score > example_best_evidence_score:
                example_best_evidence_score = score
                matched_evidence = best_gold

            if hit:
                evidence_hit = True

            h_hit, h_score, h_gold = is_evidence_hit(
                retrieved_text=item["content"],
                gold_evidence_items=highlighted_items,
                threshold=match_threshold,
            )
            if h_score > example_best_highlighted_score:
                example_best_highlighted_score = h_score
                matched_highlighted = h_gold

            if h_hit:
                highlighted_hit = True

        if evidence_hit:
            evidence_hit_count += 1

        if highlighted_hit:
            highlighted_hit_count += 1

        best_evidence_scores.append(example_best_evidence_score)
        best_highlighted_scores.append(example_best_highlighted_score)

        detail = {
            "example_idx": idx,
            "paper_id": gold_paper_id,
            "title": ex["title"],
            "question_id": ex["question_id"],
            "question": ex["question"],
            "paper_hit": paper_hit,
            "evidence_hit": evidence_hit,
            "highlighted_hit": highlighted_hit,
            "best_evidence_score": example_best_evidence_score,
            "best_highlighted_score": example_best_highlighted_score,
            "matched_evidence": matched_evidence,
            "matched_highlighted": matched_highlighted,
            "gold_evidence": evidence_items,
            "gold_highlighted_evidence": highlighted_items,
            "retrieved": [
                {
                    key: value
                    for key, value in item.items()
                    if key != "content"
                }
                for item in retrieved
            ],
            "retrieved_preview": [
                {
                    "rank": item["rank"],
                    "paper_id": item["paper_id"],
                    "section_name": item["section_name"],
                    "content_preview": item["content"][:500],
                }
                for item in retrieved[:3]
            ],
            "retrieval_info": retrieval_info,
        }

        details.append(detail)

        if idx < debug_examples:
            print("\n" + "=" * 100)
            print(f"DEBUG example {idx}")
            print("paper_id:", gold_paper_id)
            print("question:", ex["question"])
            print("paper_hit:", paper_hit)
            print("evidence_hit:", evidence_hit)
            print("highlighted_hit:", highlighted_hit)
            print("best_evidence_score:", f"{example_best_evidence_score:.4f}")
            print("best_highlighted_score:", f"{example_best_highlighted_score:.4f}")
            print("retrieved paper ids:", retrieved_paper_ids[:top_k])
            print("first gold evidence:", evidence_items[0][:500] if evidence_items else "")
            if retrieved:
                print("first retrieved preview:")
                print(retrieved[0]["content"][:500].replace("\n", " "))

    n = len(examples)

    metrics = {
        "num_examples": float(n),
        "paper_hit@k": paper_hit_count / n if n else 0.0,
        "evidence_hit@k": evidence_hit_count / n if n else 0.0,
        "highlighted_hit@k": highlighted_hit_count / n if n else 0.0,
        "avg_best_evidence_score": (
            sum(best_evidence_scores) / n if n else 0.0
        ),
        "avg_best_highlighted_score": (
            sum(best_highlighted_scores) / n if n else 0.0
        ),
    }

    return metrics, details


def save_outputs(
    split: str,
    metrics: dict[str, float],
    details: list[dict[str, Any]],
    args: argparse.Namespace,
) -> None:
    """Save metrics and detailed records."""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    mode = "oracle_paper" if args.oracle_paper else "end_to_end"

    suffix = (
        f"qasper_{split}_evidence_{mode}_"
        f"paperk{args.paper_k}_chunkk{args.chunk_k}_topk{args.top_k}"
    )

    metrics_path = OUTPUT_DIR / f"{suffix}_metrics.json"
    details_path = OUTPUT_DIR / f"{suffix}_details.json"

    payload = {
        "task": "qasper_evidence_retrieval",
        "mode": "oracle_paper" if args.oracle_paper else "end_to_end",
        "split": split,
        "args": vars(args),
        "metrics": metrics,
    }

    metrics_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    details_path.write_text(
        json.dumps(details, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    print("\nSaved metrics to:")
    print(metrics_path)

    print("\nSaved details to:")
    print(details_path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", choices=["train", "dev", "test"], default="dev")
    parser.add_argument("--limit_examples", type=int, default=0)
    parser.add_argument("--top_k", type=int, default=8)
    parser.add_argument("--paper_k", type=int, default=20)
    parser.add_argument("--chunk_k", type=int, default=8)
    parser.add_argument("--match_threshold", type=float, default=0.75)
    parser.add_argument("--debug_examples", type=int, default=3)
    parser.add_argument(
        "--oracle_paper",
        action="store_true",
        help="Restrict retrieval to the gold paper and evaluate within-paper evidence retrieval.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not QASPER_CHUNK_DB_DIR.exists():
        raise FileNotFoundError(f"QASPER chunk DB not found: {QASPER_CHUNK_DB_DIR}")

    if not QASPER_CATALOG_DB_DIR.exists():
        raise FileNotFoundError(
            f"QASPER paper catalog DB not found: {QASPER_CATALOG_DB_DIR}"
        )

    print(f"Loading QASPER split: {args.split}")
    data = load_qasper_split(args.split)

    print("Collecting answerable QA examples with evidence...")
    examples = collect_qasper_examples(data)

    if args.limit_examples and args.limit_examples > 0:
        examples = examples[: args.limit_examples]

    print(f"Number of evaluation examples: {len(examples)}")

    patch_qasper_paths()

    print("Building EngineeredRAG with QASPER index...")
    rag = EngineeredRAG()

    metrics, details = evaluate_examples(
        rag=rag,
        examples=examples,
        top_k=args.top_k,
        paper_k=args.paper_k,
        chunk_k=args.chunk_k,
        match_threshold=args.match_threshold,
        oracle_paper=args.oracle_paper,
        debug_examples=args.debug_examples,
    )

    print("\nMetrics:")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")

    save_outputs(
        split=args.split,
        metrics=metrics,
        details=details,
        args=args,
    )


if __name__ == "__main__":
    main()