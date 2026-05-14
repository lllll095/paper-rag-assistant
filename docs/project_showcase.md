# Project Showcase: Paper RAG Assistant

## 1. Project Overview

**Paper RAG Assistant** is an engineered Retrieval-Augmented Generation (RAG) system for academic paper question answering.

The system is designed to help users read, search, compare, and summarize a collection of research papers. Users can ask questions such as:

- What AI-generated text detection methods are discussed in these papers?
- How does AdaDetectGPT work?
- How does DetectGPT detect machine-generated text?
- Which methods provide statistical guarantees?
- What is the difference between DetectGPT and AdaDetectGPT?
- What datasets and evaluation metrics are used in these papers?

The project started from a basic PDF-based RAG pipeline and was gradually upgraded into a more engineering-oriented RAG system with hierarchical retrieval, hybrid retrieval, reranking, query routing, answer-level evaluation, and a Streamlit interface.

---

## 2. Motivation

A naive RAG system usually performs flat vector search over all text chunks. This simple approach can work for small demos, but it often fails in realistic academic paper QA scenarios.

Typical problems include:

1. **Cross-paper confusion**  
   The retriever may mix chunks from unrelated papers.

2. **Noisy retrieval**  
   It may retrieve references, appendices, checklists, or boilerplate sections instead of the actual main text.

3. **Weak handling of exact terms**  
   Dense embedding retrieval may miss method names, abbreviations, or technical terms such as DetectGPT, AdaDetectGPT, logits, AUROC, FNR, and TNR.

4. **Poor evidence selection**  
   Even if the correct paper is retrieved, the selected chunks may not be the best evidence for answering the question.

5. **Unreliable answers**  
   If the retrieved context is poor, the LLM may generate incomplete or unsupported answers.

This project addresses these issues by designing a more structured and evaluable RAG pipeline.

---

## 3. System Architecture

The final system follows this pipeline:

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

This architecture is more reliable than directly searching over all chunks with a single vector retriever.

---

## 4. Core Components

## 4.1 PDF Loading and Chunk Indexing

The system first loads academic papers from:

```text
data/papers/
```

Each PDF is parsed into pages, cleaned, and split into chunks.

Each chunk is stored with metadata such as:

```text
source
page
chunk_id
chunk_type
```

The `chunk_type` field is used to distinguish main text from noisy sections such as:

```text
main
checklist
references
appendix
```

The chunk-level vector index is stored in Chroma.

---

## 4.2 Paper-level Catalog

In addition to the chunk-level index, the system builds a paper-level catalog.

Each paper is represented by a higher-level document containing:

```text
title
source file
abstract
first-page excerpt
manual metadata
aliases
keywords
method type
summary
```

This catalog helps the system first identify relevant papers before retrieving detailed chunks.

This is important because many user questions are either about a specific paper or require comparison across several papers.

---

## 4.3 Query Router

The system includes a lightweight query router.

It classifies user questions into types such as:

| Query Type | Example | Retrieval Strategy |
|---|---|---|
| method | How does AdaDetectGPT work? | Auto / specific-paper retrieval |
| comparison | What is the difference between DetectGPT and AdaDetectGPT? | Multi-paper retrieval |
| survey | What AI-generated text detection methods are discussed? | Global diverse retrieval |
| evidence | Which methods provide statistical guarantees? | Global evidence retrieval |
| experiment | What datasets are used? | Experiment-oriented retrieval |
| general | Other questions | Automatic retrieval |

The query router dynamically controls retrieval parameters such as:

```text
paper_k
chunk_k
max_per_source
retrieval_mode
```

This makes the retrieval strategy adaptive rather than fixed.

---

## 4.4 Hierarchical Retrieval

Instead of directly searching over all chunks, the system performs hierarchical retrieval.

The process is:

```text
Question
  ↓
Retrieve candidate papers from paper catalog
  ↓
Decide specific-paper or global mode
  ↓
Retrieve chunks from selected candidate papers
```

This helps reduce cross-paper confusion and improves the relevance of retrieved evidence.

---

## 4.5 Hybrid Retrieval

The system combines two types of chunk retrieval:

```text
Dense retrieval: semantic embedding search
BM25 retrieval: keyword-based search
```

Dense retrieval is useful for semantic matching.

BM25 retrieval is useful for exact method names and technical terms, such as:

```text
DetectGPT
AdaDetectGPT
Fast-DetectGPT
logits
watermark
statistical guarantees
AUROC
FNR
TNR
```

The system merges dense and BM25 candidates before reranking.

This improves recall and makes the retriever more robust.

---

## 4.6 Cross-Encoder Reranking

After candidate chunks are retrieved, a cross-encoder reranker scores each query-chunk pair.

The reranker helps select the most relevant chunks from the candidate pool.

The retrieval process becomes:

```text
Dense candidates
  +
BM25 candidates
  ↓
Merge
  ↓
Cross-encoder reranking
  ↓
Top evidence chunks
```

This improves the final context passed to the LLM.

---

## 4.7 Answer Generation

The LLM receives:

```text
question
retrieved context
source information
retrieval strategy description
```

The answer prompt requires the model to:

1. answer only using the retrieved context;
2. avoid unsupported claims;
3. cite sources such as `[Source 1]`;
4. say the context is insufficient if the evidence is not enough.

This makes the final answer more grounded.

---

## 5. Evaluation Design

The project includes multiple evaluation scripts.

| Evaluation Script | Purpose |
|---|---|
| `eval_engineered_rag.py` | Evaluate hierarchical retrieval quality |
| `eval_reranker_ablation.py` | Compare vector-only retrieval with reranker retrieval |
| `eval_hybrid_retrieval.py` | Compare dense only, BM25 only, and hybrid + reranker |
| `eval_query_router.py` | Evaluate query classification and routing |
| `eval_answer_quality.py` | Evaluate final answer quality |

The evaluation is organized into three levels:

```text
Retrieval-level evaluation
  ↓
Routing / reranking / hybrid retrieval evaluation
  ↓
Answer-level evaluation
```

---

## 6. Answer-level Evaluation

The answer-level evaluation checks:

1. **Answer relevance**  
   Whether the answer addresses the user's question.

2. **Groundedness**  
   Whether the answer is supported by retrieved context.

3. **Citation support**  
   Whether cited sources actually support the claims.

4. **Completeness**  
   Whether the answer is sufficiently complete given the retrieved evidence.

5. **Insufficient context handling**  
   Whether the model avoids hallucination when context is insufficient.

6. **Hallucination risk**  
   Whether the answer contains unsupported claims.

This helps evaluate the final output, not just the retrieval stage.

---

## 7. Streamlit Demo

The project includes a Streamlit interface.

To run the demo:

```powershell
streamlit run app.py
```

The app supports:

- entering a question;
- running the engineered RAG pipeline;
- displaying the answer;
- showing query route information;
- showing candidate papers;
- showing selected papers;
- showing retrieved chunks;
- displaying vector, BM25, and reranker scores.

This makes the project easier to demonstrate and inspect.

---

## 8. Project Structure

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
    demo_qa.md
    retrieval_experiment.md
    engineered_rag_eval.md
    reranker_ablation.md
    hybrid_retrieval_eval.md
    query_router_eval.md
    answer_eval_report.md
    answer_eval_results.jsonl

  docs/
    project_showcase.md
    interview_script.md
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

```text
Which methods use logits for AI-generated text detection?
```

---

## 10. Technical Highlights

The main technical highlights are:

1. **From flat RAG to hierarchical RAG**  
   The system first retrieves relevant papers, then retrieves chunks from those papers.

2. **Metadata-aware retrieval**  
   Chunks are labeled with metadata such as source, page, chunk ID, and chunk type.

3. **Hybrid retrieval**  
   Dense retrieval and BM25 retrieval are combined to improve recall.

4. **Cross-encoder reranking**  
   Candidate chunks are reranked before being sent to the LLM.

5. **Adaptive query routing**  
   Different question types use different retrieval strategies.

6. **Multi-level evaluation**  
   The project evaluates retrieval, reranking, hybrid retrieval, routing, and final answer quality.

7. **Interactive demo**  
   The Streamlit app makes the system easy to inspect and demonstrate.

---

## 11. What I Learned

Through this project, I learned that RAG quality depends heavily on retrieval quality.

Important lessons include:

1. A simple vector search pipeline is often not enough.
2. Metadata is critical for reliable RAG.
3. Paper-level routing can reduce cross-document confusion.
4. BM25 is useful for exact technical terms.
5. Reranking improves final evidence quality.
6. Query routing makes retrieval more adaptive.
7. Answer-level evaluation is necessary for checking groundedness and hallucination risk.
8. Engineering a RAG system requires iterative evaluation, not just prompt engineering.

---

## 12. Current Limitations

The current system still has limitations:

1. The paper catalog partly depends on manual metadata.
2. The query router is rule-based.
3. Section-level metadata is still coarse.
4. The Streamlit app is currently read-only and does not support online PDF upload.
5. Answer-level evaluation uses LLM-as-a-judge, which is useful but approximate.
6. The current evaluation set is still small.
7. Citation verification is not yet fully automatic.

---

## 13. Future Work

Possible future improvements include:

1. Add PDF upload and online indexing in Streamlit.
2. Automatically extract paper metadata and method names.
3. Add section-level chunk labeling.
4. Improve query routing with an LLM-based router.
5. Add citation-level verification.
6. Build a gold-answer benchmark for evaluation.
7. Add support for multi-turn conversation.
8. Deploy the app online.
9. Add user feedback for retrieval quality.
10. Optimize latency and caching.

---

## 14. Summary

This project demonstrates a practical evolution from a simple PDF RAG demo to a more engineered academic paper QA system.

The final system includes:

```text
PDF ingestion
chunk indexing
paper-level catalog
query routing
hierarchical retrieval
hybrid dense/BM25 retrieval
cross-encoder reranking
source-grounded answer generation
multi-level evaluation
Streamlit demo
```

This makes the project suitable as a learning project, a portfolio project, and a foundation for more advanced RAG applications.