"""
Inspect local QASPER v0.3 JSON files.

Run examples:

python scripts/inspect_qasper_local.py --split dev --num_samples 2
python scripts/inspect_qasper_local.py --split train --num_samples 1
python scripts/inspect_qasper_local.py --split test --num_samples 1
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
QASPER_RAW_DIR = PROJECT_ROOT / "eval" / "qasper_raw"
OUTPUT_DIR = PROJECT_ROOT / "eval" / "qasper_inspection"


SPLIT_FILES = {
    "train": QASPER_RAW_DIR / "qasper-train-v0.3.json",
    "dev": QASPER_RAW_DIR / "qasper-dev-v0.3.json",
    "test": QASPER_RAW_DIR / "qasper-test-v0.3.json",
}


def truncate(text: Any, max_chars: int = 500) -> str:
    s = str(text)
    return s if len(s) <= max_chars else s[:max_chars] + " ... [truncated]"


def load_qasper_split(split: str) -> dict[str, Any]:
    path = SPLIT_FILES[split]
    if not path.exists():
        raise FileNotFoundError(f"QASPER split file not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise TypeError(f"Expected top-level dict, got {type(data)}")

    return data


def get_paper_items(data: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    """QASPER original JSON is usually paper_id -> paper object."""
    items = []
    for paper_id, paper in data.items():
        if isinstance(paper, dict):
            items.append((str(paper_id), paper))
    return items


def full_text_stats(full_text: Any) -> dict[str, Any]:
    """Summarize QASPER full_text structure.

    In original QASPER JSON, full_text is commonly a list of sections:
    [
      {"section_name": "...", "paragraphs": [...]},
      ...
    ]
    """

    if not isinstance(full_text, list):
        return {
            "type": type(full_text).__name__,
            "num_sections": 0,
            "num_paragraphs": 0,
            "first_section": None,
            "first_paragraph_preview": truncate(full_text),
        }

    num_sections = len(full_text)
    num_paragraphs = 0
    first_section = None
    first_paragraph = ""

    for section in full_text:
        if not isinstance(section, dict):
            continue

        section_name = section.get("section_name")
        paragraphs = section.get("paragraphs", [])

        if first_section is None:
            first_section = section_name

        if isinstance(paragraphs, list):
            num_paragraphs += len(paragraphs)
            if not first_paragraph and paragraphs:
                first_paragraph = str(paragraphs[0])
        elif isinstance(paragraphs, str):
            num_paragraphs += 1
            if not first_paragraph:
                first_paragraph = paragraphs

    section_names = [
        section.get("section_name")
        for section in full_text[:8]
        if isinstance(section, dict)
    ]

    return {
        "type": "list[section]",
        "num_sections": num_sections,
        "num_paragraphs": num_paragraphs,
        "section_names_preview": section_names,
        "first_section": first_section,
        "first_paragraph_preview": truncate(first_paragraph),
    }


def answer_payload(answer_item: dict[str, Any]) -> dict[str, Any]:
    inner = answer_item.get("answer")
    if isinstance(inner, dict):
        return inner
    return answer_item


def summarize_split(data: dict[str, Any]) -> dict[str, Any]:
    paper_items = get_paper_items(data)

    num_questions = 0
    num_answers = 0
    answer_type_counter = Counter()
    evidence_counter = Counter()
    paragraph_counter = 0
    section_counter = 0

    for _, paper in paper_items:
        full_text = paper.get("full_text", [])
        if isinstance(full_text, list):
            section_counter += len(full_text)
            for section in full_text:
                if isinstance(section, dict):
                    paragraphs = section.get("paragraphs", [])
                    if isinstance(paragraphs, list):
                        paragraph_counter += len(paragraphs)
                    elif isinstance(paragraphs, str):
                        paragraph_counter += 1

        qas = paper.get("qas", [])
        if not isinstance(qas, list):
            continue

        num_questions += len(qas)

        for qa in qas:
            answers = qa.get("answers", []) if isinstance(qa, dict) else []
            if not isinstance(answers, list):
                continue

            num_answers += len(answers)

            for ans in answers:
                if not isinstance(ans, dict):
                    continue

                payload = answer_payload(ans)

                if payload.get("unanswerable") is True:
                    answer_type_counter["unanswerable"] += 1

                if payload.get("yes_no") is not None:
                    answer_type_counter["yes_no"] += 1

                free_form = payload.get("free_form_answer")
                if isinstance(free_form, str) and free_form.strip():
                    answer_type_counter["free_form"] += 1

                extractive = payload.get("extractive_spans")
                if isinstance(extractive, list) and extractive:
                    answer_type_counter["extractive"] += 1

                evidence = payload.get("evidence")
                if isinstance(evidence, list):
                    evidence_counter["evidence_items"] += len(evidence)

                highlighted = payload.get("highlighted_evidence")
                if isinstance(highlighted, list):
                    evidence_counter["highlighted_evidence_items"] += len(highlighted)

    return {
        "num_papers": len(paper_items),
        "num_questions": num_questions,
        "num_answers": num_answers,
        "num_sections": section_counter,
        "num_paragraphs": paragraph_counter,
        **{f"answers_{k}": v for k, v in answer_type_counter.items()},
        **dict(evidence_counter),
    }


def print_sample(paper_id: str, paper: dict[str, Any], index: int) -> dict[str, Any]:
    print("\n" + "=" * 100)
    print(f"Sample index: {index}")
    print(f"Paper id: {paper_id}")
    print("=" * 100)

    print("\nTop-level keys:")
    print(list(paper.keys()))

    print("\nTitle:")
    print(paper.get("title"))

    print("\nAbstract preview:")
    print(truncate(paper.get("abstract"), 800))

    stats = full_text_stats(paper.get("full_text"))
    print("\nFull text stats:")
    print(json.dumps(stats, ensure_ascii=False, indent=2))

    qas = paper.get("qas", [])
    if not isinstance(qas, list):
        qas = []

    print("\nNumber of QAs:")
    print(len(qas))

    first_qa_summary: dict[str, Any] = {}

    if qas:
        qa = qas[0]
        print("\nFirst QA keys:")
        print(list(qa.keys()))

        print("\nFirst question:")
        print(qa.get("question"))

        print("\nFirst question id:")
        print(qa.get("question_id"))

        answers = qa.get("answers", [])
        if not isinstance(answers, list):
            answers = []

        print("\nNumber of answers:")
        print(len(answers))

        answer_summaries = []
        for ans in answers[:2]:
            if not isinstance(ans, dict):
                continue

            payload = answer_payload(ans)

            summary = {
                "answer_item_keys": list(ans.keys()),
                "answer_payload_keys": list(payload.keys()),
                "unanswerable": payload.get("unanswerable"),
                "yes_no": payload.get("yes_no"),
                "free_form_answer": payload.get("free_form_answer"),
                "extractive_spans": payload.get("extractive_spans"),
                "evidence": payload.get("evidence"),
                "highlighted_evidence": payload.get("highlighted_evidence"),
            }

            answer_summaries.append(summary)

        print("\nFirst answer summaries:")
        print(json.dumps(answer_summaries, ensure_ascii=False, indent=2))

        first_qa_summary = {
            "question": qa.get("question"),
            "question_id": qa.get("question_id"),
            "num_answers": len(answers),
            "answer_summaries": answer_summaries,
        }

    return {
        "paper_id": paper_id,
        "title": paper.get("title"),
        "abstract_preview": truncate(paper.get("abstract"), 1200),
        "full_text_stats": stats,
        "num_qas": len(qas),
        "first_qa_summary": first_qa_summary,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", choices=["train", "dev", "test"], default="dev")
    parser.add_argument("--num_samples", type=int, default=2)
    parser.add_argument("--save_raw_sample", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print(f"Loading local QASPER split: {args.split}")
    data = load_qasper_split(args.split)
    paper_items = get_paper_items(data)

    print("\nSplit file:")
    print(SPLIT_FILES[args.split])

    print("\nSplit summary:")
    split_summary = summarize_split(data)
    print(json.dumps(split_summary, ensure_ascii=False, indent=2))

    sample_summaries = []
    for i, (paper_id, paper) in enumerate(paper_items[: args.num_samples]):
        sample_summaries.append(print_sample(paper_id, paper, i))

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output_path = OUTPUT_DIR / f"qasper_{args.split}_inspection_summary.json"
    output = {
        "split": args.split,
        "split_file": str(SPLIT_FILES[args.split]),
        "split_summary": split_summary,
        "sample_summaries": sample_summaries,
    }

    output_path.write_text(
        json.dumps(output, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("\nSaved inspection summary to:")
    print(output_path)

    if args.save_raw_sample and paper_items:
        raw_path = OUTPUT_DIR / f"qasper_{args.split}_raw_sample.json"
        first_paper_id, first_paper = paper_items[0]
        raw_path.write_text(
            json.dumps(
                {
                    "paper_id": first_paper_id,
                    "paper": first_paper,
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print("\nSaved raw sample to:")
        print(raw_path)


if __name__ == "__main__":
    main()