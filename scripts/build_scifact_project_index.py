"""
Build a project-compatible SciFact index for paper-rag-assistant.

This script converts BEIR/SciFact corpus into two Chroma vectorstores:

1. chunk_db:
   document-level chunks used by chunk retrieval.

2. paper_catalog_db:
   paper-level catalog used by EngineeredRAG.retrieve_candidate_papers().

The goal is to make SciFact usable by the real EngineeredRAG retrieval pipeline
without overwriting the normal paper-rag-assistant indexes.
"""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

from datasets import load_dataset
from langchain_core.documents import Document
from langchain_chroma import Chroma

try:
    from langchain_huggingface import HuggingFaceEmbeddings
except ImportError:
    from langchain_community.embeddings import HuggingFaceEmbeddings


PROJECT_ROOT = Path(__file__).resolve().parents[1]

import sys

SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import rag_engineered

OUTPUT_ROOT = PROJECT_ROOT / "eval" / "scifact_project_index"
CHUNK_DB_DIR = OUTPUT_ROOT / "chunk_db"
PAPER_CATALOG_DB_DIR = OUTPUT_ROOT / "paper_catalog_db"

EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"
CHUNK_COLLECTION_NAME = "paper_rag_week1"


def pick(row: dict[str, Any], names: list[str]) -> Any:
    """Pick the first existing field from a dataset row."""

    for name in names:
        if name in row:
            return row[name]

    raise KeyError(f"None of the fields exist: {names}. Row keys: {list(row.keys())}")


def load_scifact_corpus() -> list[dict[str, str]]:
    """Load SciFact corpus from Hugging Face."""

    corpus_ds = load_dataset("BeIR/scifact", "corpus", split="corpus")

    rows: list[dict[str, str]] = []

    for row in corpus_ds:
        doc_id = str(pick(row, ["_id", "id"]))
        title = str(row.get("title", "") or "")
        text = str(row.get("text", "") or "")

        rows.append(
            {
                "doc_id": doc_id,
                "title": title,
                "text": text,
            }
        )

    return rows


def build_documents(rows: list[dict[str, str]]) -> tuple[list[Document], list[Document]]:
    """Build chunk-level and paper-level documents."""

    chunk_docs: list[Document] = []
    catalog_docs: list[Document] = []

    for idx, row in enumerate(rows):
        doc_id = row["doc_id"]
        title = row["title"]
        text = row["text"]

        full_text = f"{title}\n{text}".strip()

        # Chunk-level document.
        # SciFact corpus documents are usually short enough to use as one chunk.
        chunk_docs.append(
            Document(
                page_content=full_text,
                metadata={
                    "source": doc_id,
                    "doc_id": doc_id,
                    "chunk_id": idx,
                    "title": title,
                    "page": 0,
                    "page_label": "0",
                    "chunk_type": "main",
                    "dataset": "scifact",
                },
            )
        )

        # Paper-level catalog document.
        # EngineeredRAG's paper router can use this as paper-level entry.
        catalog_docs.append(
            Document(
                page_content=full_text,
                metadata={
                    "source": doc_id,
                    "doc_id": doc_id,
                    "title": title,
                    "dataset": "scifact",
                },
            )
        )

    return chunk_docs, catalog_docs


def reset_output_dirs() -> None:
    """Remove old SciFact index directories."""

    if OUTPUT_ROOT.exists():
        print(f"Removing old index directory: {OUTPUT_ROOT}")
        shutil.rmtree(OUTPUT_ROOT)

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)


def main() -> None:
    print("Loading SciFact corpus...")
    rows = load_scifact_corpus()
    print(f"SciFact corpus size: {len(rows)}")

    print("Building LangChain documents...")
    chunk_docs, catalog_docs = build_documents(rows)

    print("Resetting output directories...")
    reset_output_dirs()

    print(f"Loading embedding model: {EMBEDDING_MODEL_NAME}")
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        encode_kwargs={"normalize_embeddings": True},
    )

    print("Building chunk-level Chroma DB...")
    Chroma.from_documents(
        documents=chunk_docs,
        embedding=embeddings,
        persist_directory=str(CHUNK_DB_DIR),
        collection_name=CHUNK_COLLECTION_NAME,
    )

    print("Building paper-level catalog Chroma DB...")
    Chroma.from_documents(
        documents=catalog_docs,
        embedding=embeddings,
        persist_directory=str(PAPER_CATALOG_DB_DIR),
        collection_name=rag_engineered.CATALOG_COLLECTION_NAME,
    )

    print("\nDone.")
    print(f"Chunk DB: {CHUNK_DB_DIR}")
    print(f"Paper catalog DB: {PAPER_CATALOG_DB_DIR}")


if __name__ == "__main__":
    main()