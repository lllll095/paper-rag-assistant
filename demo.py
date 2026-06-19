#!/usr/bin/env python3
"""Paper RAG Assistant demo: verify installation and show capabilities."""

import sys
from pathlib import Path


MODULES = [
    "rag_engineered",
    "query_router",
    "reranker",
    "bm25_retriever",
    "load_pdf",
    "split_text",
    "retrieve",
    "build_index",
]


def green(text):
    return f"\033[32m{text}\033[0m"


def red(text):
    return f"\033[31m{text}\033[0m"


def check_modules():
    """Verify all core modules can be imported."""
    src_dir = Path(__file__).resolve().parent / "src"
    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))

    print(f"\n{green('[Paper RAG]')} Checking module imports...")
    all_ok = True
    for mod in MODULES:
        try:
            __import__(mod)
            print(f"  [OK] {mod}")
        except ImportError as e:
            print(f"  [FAIL] {mod}: {e}")
            all_ok = False
    return all_ok


def print_pipeline():
    """Print the RAG pipeline architecture."""
    print(f"\n{green('[Paper RAG]')} Pipeline:")
    steps = [
        "PDF papers",
        "  |-- Text extraction (PyPDF)",
        "  |-- Chunking (RecursiveCharacterTextSplitter)",
        "  |-- Chunk-level vector index (Chroma + bge-small-en)",
        "  |-- Paper-level catalog index",
        "  |-- Query router (method / comparison / survey / evidence)",
        "  |-- Hierarchical retrieval (paper level + chunk level)",
        "  |-- Hybrid retrieval (dense + BM25)",
        "  |-- Cross-encoder reranking (ms-marco-MiniLM)",
        "  |-- Source-grounded answer generation (LLM)",
        "  |-- Answer-level evaluation",
    ]
    for s in steps:
        print(f"  {s}")


def main():
    print(f"{green('[Paper RAG]')} Engineered RAG for Academic Papers")

    ok = check_modules()

    if ok:
        print_pipeline()
        print(f"\n{green('[Paper RAG]')} All modules loaded successfully.")
        print(f"  Build index:  python src/build_index.py")
        print(f"  Run RAG:      python src/rag_engineered.py")
        print(f"  Streamlit:    streamlit run app.py")
        print(f"  Run tests:    python -m pytest tests/ -v")
    else:
        print(f"\n{red('[Paper RAG]')} Some modules failed to load.")
        sys.exit(1)


if __name__ == "__main__":
    main()
