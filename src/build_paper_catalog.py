import re
import shutil
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

import json


PROJECT_ROOT = Path(__file__).resolve().parents[1]

PAPER_DIR = PROJECT_ROOT / "data" / "papers"
CATALOG_DIR = PROJECT_ROOT / "paper_catalog_db"

CATALOG_COLLECTION_NAME = "paper_catalog_week2"
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

METADATA_PATH = PROJECT_ROOT / "data" / "paper_metadata.json"

def clean_text(text):
    if text is None:
        return ""

    if not isinstance(text, str):
        text = str(text)

    text = text.replace("\x00", " ")
    text = text.replace("\ufeff", " ")
    text = text.replace("\r", "\n")

    text = "".join(
        ch if ch.isprintable() or ch in ["\n", "\t"] else " "
        for ch in text
    )

    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def title_from_filename(pdf_path):
    title = pdf_path.stem
    title = title.replace("_", " ")
    title = title.replace("-", " ")
    title = re.sub(r"\s+", " ", title).strip()
    return title

def load_manual_metadata():
    """
    Load optional paper-level metadata from data/paper_metadata.json.

    The metadata file is used to improve paper-level routing.
    """
    if not METADATA_PATH.exists():
        print(f"No manual metadata found at {METADATA_PATH}")
        return {}

    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        items = json.load(f)

    metadata_map = {}

    for item in items:
        source = item.get("source")
        if not source:
            continue

        metadata_map[source] = item

    print(f"Loaded manual metadata for {len(metadata_map)} papers.")

    return metadata_map

def extract_abstract(first_pages_text):
    """
    Try to extract abstract from the first few pages.
    If extraction fails, return an empty string.
    """
    text = clean_text(first_pages_text)

    # Common pattern: Abstract ... Introduction
    pattern = re.compile(
        r"(abstract\s*[:.\-]?\s*)(.*?)(\n\s*1\s+introduction|\n\s*introduction|\n\s*keywords|\n\s*1\.)",
        flags=re.IGNORECASE | re.DOTALL,
    )

    match = pattern.search(text)

    if match:
        abstract = match.group(2)
        abstract = clean_text(abstract)
        return abstract[:3000]

    # Fallback: find "abstract" and take following text
    lower = text.lower()
    idx = lower.find("abstract")

    if idx >= 0:
        abstract = text[idx + len("abstract"): idx + len("abstract") + 2000]
        return clean_text(abstract)

    return ""


def load_first_pages(pdf_path, max_pages=3):
    loader = PyPDFLoader(str(pdf_path))
    docs = loader.load()

    selected_docs = docs[:max_pages]

    texts = []

    for doc in selected_docs:
        text = clean_text(doc.page_content)
        if text:
            texts.append(text)

    return "\n\n".join(texts)


def build_catalog():
    pdf_files = sorted(PAPER_DIR.glob("*.pdf"))
    manual_metadata = load_manual_metadata()

    if not pdf_files:
        raise FileNotFoundError(f"No PDF files found in {PAPER_DIR}")

    print(f"Found {len(pdf_files)} PDF files.")

    documents = []

    for i, pdf_path in enumerate(pdf_files):
        print("=" * 80)
        print(f"Processing paper {i + 1}/{len(pdf_files)}: {pdf_path.name}")

        try:
            first_pages_text = load_first_pages(pdf_path, max_pages=3)
        except Exception as e:
            print(f"Failed to parse {pdf_path.name}: {e}")
            continue

        manual_item = manual_metadata.get(pdf_path.name, {})
        
        title = manual_item.get("title") or title_from_filename(pdf_path)
        aliases = manual_item.get("aliases", [])
        task = manual_item.get("task", "")
        method_type = manual_item.get("method_type", "")
        keywords = manual_item.get("keywords", [])
        manual_summary = manual_item.get("summary", "")
        
        abstract = extract_abstract(first_pages_text)

        if abstract:
            print("Abstract extracted.")
        else:
            print("Abstract not found. Using first-page text as fallback.")

        catalog_text = f"""
Title:
{title}

Source file:
{pdf_path.name}

Aliases:
{", ".join(aliases)}

Task:
{task}

Method type:
{method_type}

Keywords:
{", ".join(keywords)}

Manual summary:
{manual_summary}

Abstract:
{abstract if abstract else first_pages_text[:2500]}

First pages excerpt:
{first_pages_text[:2500]}
"""

        metadata = {
            "paper_id": f"paper_{i}",
            "title": title,
            "source": pdf_path.name,
            "has_abstract": bool(abstract),
            "aliases": ", ".join(aliases),
            "task": task,
            "method_type": method_type,
            "keywords": ", ".join(keywords),
        }

        documents.append(
            Document(
                page_content=clean_text(catalog_text),
                metadata=metadata,
            )
        )

    if not documents:
        raise ValueError("No valid paper catalog documents were created.")

    if CATALOG_DIR.exists():
        print(f"Removing old paper catalog index: {CATALOG_DIR}")
        shutil.rmtree(CATALOG_DIR)

    print("=" * 80)
    print("Loading embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        encode_kwargs={"normalize_embeddings": True},
    )

    print("Building paper-level Chroma catalog...")

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=str(CATALOG_DIR),
        collection_name=CATALOG_COLLECTION_NAME,
    )

    print("=" * 80)
    print(f"Paper catalog saved to: {CATALOG_DIR}")
    print(f"Number of indexed papers: {len(documents)}")
    print("Paper catalog building finished.")
    print("=" * 80)

    return vectorstore


if __name__ == "__main__":
    build_catalog()