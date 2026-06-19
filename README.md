# Paper RAG Assistant

[![Test](https://github.com/lllll095/paper-rag-assistant/actions/workflows/test.yml/badge.svg)](https://github.com/lllll095/paper-rag-assistant/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](pyproject.toml)

An engineered Retrieval-Augmented Generation (RAG) system for academic paper question answering. Supports PDF ingestion, hierarchical paper-level retrieval, hybrid dense/BM25 search, cross-encoder reranking, query routing, and source-grounded answer generation.

---

## Pipeline

```text
PDF papers
  |-- Text extraction and chunking
  |-- Chunk-level vector index (Chroma + bge-small-en-v1.5)
  |-- Paper-level catalog index
  |-- Query router (method / comparison / survey / evidence / experiment)
  |-- Hierarchical retrieval (paper level + chunk level)
  |-- Hybrid retrieval (dense + BM25)
  |-- Cross-encoder reranker (ms-marco-MiniLM-L6-v2)
  |-- Source-grounded answer generation (LLM)
  |-- Answer-level evaluation
```

## Features

- **PDF loading and text extraction** with cleanup
- **Text chunking** with metadata (source, page, chunk_id, chunk_type)
- **Chroma vector database** for dense embeddings
- **Paper-level catalog** for document routing
- **Hierarchical retrieval** - paper first, then chunks
- **Hybrid retrieval** - dense embeddings + BM25 keyword search
- **Cross-encoder reranking** for evidence selection
- **Query router** - classifies questions into method / comparison / survey / evidence / experiment types
- **Source-grounded answer generation** with citations
- **Multi-level evaluation** - retrieval, reranker, hybrid, query router, answer quality
- **Streamlit demo interface**

## Quick Start

```bash
# Clone and install
git clone https://github.com/lllll095/paper-rag-assistant.git
cd paper-rag-assistant

# Create environment
conda create -n rag-week1 python=3.10
conda activate rag-week1

# Install
pip install -e ".[dev]"

# Configure
cp .env.example .env
# Edit .env with your API keys

# Build indices
python src/build_index.py
python src/build_paper_catalog.py

# Run RAG
python src/rag_engineered.py

# Launch UI
streamlit run app.py

# Run tests
python -m pytest tests/ -v
```

## Architecture

The final RAG pipeline:

```text
User Question
  |-- Query Router
  |-- Paper-level Retrieval
  |-- Candidate Papers
  |-- Dense Retrieval + BM25 Retrieval
  |-- Merge Candidate Chunks
  |-- Cross-Encoder Reranker
  |-- Top-ranked Evidence Chunks
  |-- LLM Answer Generation
  |-- Answer with Sources
```

## Evaluation

| Script | Purpose |
|---|---|
| eval_engineered_rag.py | Evaluate hierarchical retrieval quality |
| eval_reranker_ablation.py | Compare vector-only vs reranker retrieval |
| eval_hybrid_retrieval.py | Compare dense, BM25, and hybrid |
| eval_query_router.py | Evaluate query classification |
| eval_answer_quality.py | Evaluate answer groundedness, citations, hallucination |

## Project Structure

```
src/
  rag_engineered.py      Main RAG pipeline (EngineeredRAG class)
  query_router.py        Query classification router
  bm25_retriever.py      BM25 keyword retriever
  reranker.py            Cross-encoder reranker
  load_pdf.py            PDF text extraction
  split_text.py          Text chunking and metadata
  build_index.py         Build vector index
  build_paper_catalog.py Build paper-level catalog
  eval_*.py              Evaluation scripts
app.py                   Streamlit UI
scripts/                 Additional evaluation scripts
tests/                   Pytest tests
```

## License

MIT License - see [LICENSE](LICENSE) for details.
