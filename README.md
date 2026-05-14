# Paper RAG Assistant: An Engineered RAG System for Academic Papers

This project implements an engineered Retrieval-Augmented Generation (RAG) system for academic paper question answering.

The system supports PDF-based knowledge ingestion, hierarchical paper-level retrieval, hybrid dense/BM25 retrieval, cross-encoder reranking, query routing, source-grounded answer generation, and multi-level evaluation.

---

## 1. Project Overview

The goal of this project is to build a practical RAG system for reading and analyzing academic papers.

Instead of using a simple flat vector search over all chunks, this project gradually upgrades the pipeline into a more engineering-oriented RAG system:

```text
PDF papers
  ↓
Text extraction and chunking
  ↓
Chunk-level vector index
  ↓
Paper-level catalog index
  ↓
Query routing
  ↓
Hierarchical retrieval
  ↓
Hybrid dense + BM25 retrieval
  ↓
Cross-encoder reranking
  ↓
Source-grounded answer generation
  ↓
Answer-level evaluation
```

---

## 2. Key Features

- PDF loading and text extraction
- Text chunking with metadata
- Chroma vector database
- Paper-level catalog retrieval
- Hierarchical retrieval
- Dense embedding retrieval
- BM25 keyword retrieval
- Hybrid retrieval
- Cross-encoder reranking
- Query router for different question types
- Source-grounded answer generation
- Retrieval evaluation
- Reranker ablation study
- Hybrid retrieval evaluation
- Query router evaluation
- Answer-level evaluation
- Streamlit demo interface

---

## 3. System Architecture

The final RAG pipeline is:

```text
User Question
  ↓
Query Router
  ↓
Paper-level Retrieval
  ↓
Candidate Papers
  ↓
Dense Retrieval + BM25 Retrieval
  ↓
Merge Candidate Chunks
  ↓
Cross-Encoder Reranker
  ↓
Top-ranked Evidence Chunks
  ↓
LLM Answer Generation
  ↓
Answer with Sources
```

---

## 4. Retrieval Design

### 4.1 Paper-level Retrieval

A paper catalog is built for document-level routing. Each paper is represented by:

```text
title
source file
abstract
first-page excerpt
manual metadata
keywords
aliases
method summary
```

This helps the system decide which papers are relevant before retrieving chunks.

### 4.2 Chunk-level Retrieval

For each selected paper, the system retrieves candidate chunks using both:

```text
Dense retrieval: semantic embedding search
BM25 retrieval: keyword-based lexical search
```

Dense retrieval captures semantic similarity, while BM25 is useful for exact method names and technical terms such as:

```text
DetectGPT
AdaDetectGPT
logits
watermark
AUROC
FNR
TNR
statistical guarantees
```

### 4.3 Reranking

After dense and BM25 candidates are merged, a cross-encoder reranker is used to re-score query-chunk pairs and select the most relevant evidence chunks.

---

## 5. Query Router

The system includes a lightweight query router that classifies questions into different types:

| Query Type | Example | Retrieval Strategy |
|---|---|---|
| method | How does AdaDetectGPT work? | Auto / specific paper |
| comparison | What is the difference between DetectGPT and AdaDetectGPT? | Global multi-paper retrieval |
| survey | What AI-generated text detection methods are discussed? | Global diverse retrieval |
| evidence | Which methods provide statistical guarantees? | Global evidence retrieval |
| experiment | What datasets are used? | Experiment-oriented retrieval |
| general | Other questions | Automatic retrieval |

---

## 6. Evaluation

The project includes several evaluation scripts:

| Evaluation Script | Purpose |
|---|---|
| `eval_engineered_rag.py` | Evaluate hierarchical retrieval quality |
| `eval_reranker_ablation.py` | Compare vector-only retrieval and reranker retrieval |
| `eval_hybrid_retrieval.py` | Compare dense only, BM25 only, and hybrid retrieval |
| `eval_query_router.py` | Evaluate query classification and routing |
| `eval_answer_quality.py` | Evaluate final answer quality, groundedness, citation support, and hallucination risk |

---

## 7. Project Structure

```text
paper-rag-week1/
  app.py
  README.md
  requirements.txt
  .env.example

  data/
    papers/
      *.pdf
    paper_metadata.json
    answer_eval_questions.json

  src/
    build_index.py
    build_paper_catalog.py
    rag_engineered.py
    query_router.py
    bm25_retriever.py
    reranker.py
    eval_engineered_rag.py
    eval_reranker_ablation.py
    eval_hybrid_retrieval.py
    eval_query_router.py
    eval_answer_quality.py

  outputs/
    engineered_rag_eval.md
    reranker_ablation.md
    hybrid_retrieval_eval.md
    query_router_eval.md
    answer_eval_report.md

  docs/
    project_showcase.md
    interview_script.md
```

---

## 8. How to Run

### Step 1: Activate Environment

```powershell
conda activate rag-week1
```

### Step 2: Build Chunk-level Index

```powershell
python src/build_index.py
```

### Step 3: Build Paper-level Catalog

```powershell
python src/build_paper_catalog.py
```

### Step 4: Run Command-line RAG

```powershell
python src/rag_engineered.py
```

### Step 5: Run Streamlit Demo

```powershell
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

## 9. Example Questions

```text
What AI-generated text detection methods are discussed in these papers?
```

```text
How does AdaDetectGPT work?
```

```text
How does DetectGPT detect machine-generated text?
```

```text
Which methods provide statistical guarantees for AI-generated text detection?
```

```text
What is the difference between DetectGPT and AdaDetectGPT?
```

---

## 10. Current Limitations

- The paper catalog still depends partly on manual metadata.
- Query routing is currently rule-based.
- Section-level metadata is still coarse.
- Answer evaluation uses LLM-as-a-judge and should be treated as approximate.
- The current Streamlit demo is read-only and does not yet support uploading new PDFs from the UI.

---

## 11. Future Work

Planned improvements:

- Add PDF upload and automatic indexing in the Streamlit app.
- Add section-aware chunk labeling.
- Improve paper catalog with automatic method-name extraction.
- Add more robust query routing.
- Add citation-level verification.
- Add benchmark-style evaluation with gold answers.
- Deploy the app online.