
"""
Build a project-compatible QASPER index for paper-rag-assistant.

This script converts local QASPER v0.3 JSON files into two Chroma vectorstores:

1. chunk_db:
   paragraph-level chunks from long papers.

2. paper_catalog_db:
   paper-level catalog entries for EngineeredRAG's paper routing.

Run:

python scripts/build_qasper_project_index.py --split dev
python scripts/build_qasper_project_index.py --split train --limit_papers 100
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any

from langchain_core.documents import Document
from langchain_chroma import Chroma

try:
    from langchain_huggingface import HuggingFaceEmbeddings
except ImportError:
    from langchain_community.embeddings import HuggingFaceEmbeddings


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import rag_engineered  # noqa: E402


QASPER_RAW_DIR = PROJECT_ROOT / "eval" / "qasper_raw"
OUTPUT_ROOT = PROJECT_ROOT / "eval" / "qasper_project_index"

CHUNK_DB_DIR = OUTPUT_ROOT / "chunk_db"
PAPER_CATALOG_DB_DIR = OUTPUT_ROOT / "paper_catalog_db"

SPLIT_FILES = {
    "train": QASPER_RAW_DIR / "qasper-train-v0.3.json",
    "dev": QASPER_RAW_DIR / "qasper-dev-v0.3.json",
    "test": QASPER_RAW_DIR / "qasper-test-v0.3.json",
}

EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"

# Must match the collection names used by the real project.
CHUNK_COLLECTION_NAME = "paper_rag_week1"
CATALOG_COLLECTION_NAME = rag_engineered.CATALOG_COLLECTION_NAME


def load_qasper_split(split: str) -> dict[str, Any]:
    path = SPLIT_FILES[split]

    if not path.exists():
        raise FileNotFoundError(f"QASPER split file not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise TypeError(f"Expected top-level dict, got {type(data)}")

    return data


def iter_papers(data: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    papers = []

    for paper_id, paper in data.items():
        if isinstance(paper, dict):
            papers.append((str(paper_id), paper))

    return papers


def normalize_abstract(abstract: Any) -> str:
    if isinstance(abstract, list):
        return "\n".join(str(x) for x in abstract)

    if abstract is None:
        return ""

    return str(abstract)


def iter_paragraphs(paper: dict[str, Any]):
    """Yield paragraph-level units from QASPER full_text."""

    full_text = paper.get("full_text", [])

    if not isinstance(full_text, list):
        return

    for section_idx, section in enumerate(full_text):
        if not isinstance(section, dict):
            continue

        section_name = str(section.get("section_name") or "")
        paragraphs = section.get("paragraphs", [])

        if isinstance(paragraphs, str):
            paragraphs = [paragraphs]

        if not isinstance(paragraphs, list):
            continue

        for para_idx, paragraph in enumerate(paragraphs):
            paragraph_text = str(paragraph).strip()

            if not paragraph_text:
                continue

            yield {
                "section_idx": section_idx,
                "section_name": section_name,
                "paragraph_idx": para_idx,
                "paragraph_text": paragraph_text,
            }


def build_documents(
    data: dict[str, Any],
    limit_papers: int | None = None,
) -> tuple[list[Document], list[Document]]:
    """Build chunk-level and paper-level catalog documents."""

    chunk_docs: list[Document] = []
    catalog_docs: list[Document] = []

    papers = iter_papers(data)

    if limit_papers is not None and limit_papers > 0:
        papers = papers[:limit_papers]

    global_chunk_id = 0

    for paper_index, (paper_id, paper) in enumerate(papers):
        title = str(paper.get("title") or "")
        abstract = normalize_abstract(paper.get("abstract"))

        # Paper-level catalog entry.
        catalog_text = f"{title}\n\nAbstract:\n{abstract}".strip()

        catalog_docs.append(
            Document(
                page_content=catalog_text,
                metadata={
                    "source": paper_id,
                    "doc_id": paper_id,
                    "paper_id": paper_id,
                    "title": title,
                    "dataset": "qasper",
                    "paper_index": paper_index,
                },
            )
        )

        # Chunk-level entries.
        for para in iter_paragraphs(paper):
            section_name = para["section_name"]
            paragraph_text = para["paragraph_text"]

            chunk_text = (
                f"Title: {title}\n"
                f"Section: {section_name}\n\n"
                f"{paragraph_text}"
            ).strip()

            chunk_docs.append(
                Document(
                    page_content=chunk_text,
                    metadata={
                        "source": paper_id,
                        "doc_id": paper_id,
                        "paper_id": paper_id,
                        "title": title,
                        "dataset": "qasper",
                        "chunk_id": global_chunk_id,
                        "section_idx": para["section_idx"],
                        "section_name": section_name,
                        "paragraph_idx": para["paragraph_idx"],
                        "paragraph_id": (
                            f"{paper_id}::"
                            f"{para['section_idx']}::"
                            f"{para['paragraph_idx']}"
                        ),
                        "chunk_type": "main",
                        "page": 0,
                        "page_label": "0",
                    },
                )
            )

            global_chunk_id += 1

    return chunk_docs, catalog_docs


def reset_output_dirs() -> None:
    if OUTPUT_ROOT.exists():
        print(f"Removing old QASPER index directory: {OUTPUT_ROOT}")
        shutil.rmtree(OUTPUT_ROOT)

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", choices=["train", "dev", "test"], default="dev")
    parser.add_argument("--limit_papers", type=int, default=0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print(f"Loading QASPER split: {args.split}")
    data = load_qasper_split(args.split)

    limit_papers = args.limit_papers if args.limit_papers > 0 else None

    print("Building LangChain documents...")
    chunk_docs, catalog_docs = build_documents(
        data=data,
        limit_papers=limit_papers,
    )

    print(f"Number of chunk documents: {len(chunk_docs)}")
    print(f"Number of catalog documents: {len(catalog_docs)}")

    if not chunk_docs:
        raise RuntimeError("No chunk documents were built.")

    if not catalog_docs:
        raise RuntimeError("No catalog documents were built.")

    print("Resetting output directories...")
    reset_output_dirs()

    print(f"Loading embedding model: {EMBEDDING_MODEL_NAME}")
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        encode_kwargs={"normalize_embeddings": True},
    )

    print(f"Building chunk-level Chroma DB: collection={CHUNK_COLLECTION_NAME}")
    Chroma.from_documents(
        documents=chunk_docs,
        embedding=embeddings,
        persist_directory=str(CHUNK_DB_DIR),
        collection_name=CHUNK_COLLECTION_NAME,
    )

    print(f"Building paper-level catalog DB: collection={CATALOG_COLLECTION_NAME}")
    Chroma.from_documents(
        documents=catalog_docs,
        embedding=embeddings,
        persist_directory=str(PAPER_CATALOG_DB_DIR),
        collection_name=CATALOG_COLLECTION_NAME,
    )

    summary = {
        "split": args.split,
        "limit_papers": limit_papers,
        "num_chunk_docs": len(chunk_docs),
        "num_catalog_docs": len(catalog_docs),
        "chunk_db_dir": str(CHUNK_DB_DIR),
        "paper_catalog_db_dir": str(PAPER_CATALOG_DB_DIR),
        "chunk_collection_name": CHUNK_COLLECTION_NAME,
        "catalog_collection_name": CATALOG_COLLECTION_NAME,
    }

    summary_path = OUTPUT_ROOT / "build_summary.json"
    summary_path.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("\nDone.")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

