# Interview Script: Paper RAG Assistant

## 1. One-minute Project Introduction

I built an engineered RAG system for academic paper question answering.

The initial version was a basic PDF-based RAG pipeline: it loaded papers, split them into chunks, built a vector index, retrieved relevant chunks, and generated answers using an LLM.

Then I gradually upgraded it into a more practical RAG system. The final version includes paper-level retrieval, hybrid dense/BM25 retrieval, cross-encoder reranking, query routing, source-grounded answer generation, answer-level evaluation, and a Streamlit demo.

The goal was not only to make the system answer questions, but also to make the retrieval process more reliable and the final answers more grounded in evidence.

---

## 2. What Problem Does This Project Solve?

The project helps users read and analyze a collection of academic papers.

For example, users can ask:

- What AI-generated text detection methods are discussed in these papers?
- How does AdaDetectGPT work?
- How does DetectGPT work?
- Which methods provide statistical guarantees?
- What is the difference between DetectGPT and AdaDetectGPT?
- Which methods use logits?

The system retrieves relevant evidence from the papers and generates answers with source references.

---

## 3. Why Not Use a Simple Vector Search RAG?

A simple RAG system usually performs flat vector search over all chunks.

This has several problems.

First, it may confuse different papers because all chunks are mixed together.

Second, it may retrieve noisy sections such as references, appendices, checklists, or reproducibility statements.

Third, dense embeddings may not be reliable for exact method names, abbreviations, and technical terms.

Fourth, even if the correct paper is retrieved, the top chunks may not be the best evidence.

Therefore, I introduced hierarchical retrieval, metadata filtering, BM25 keyword retrieval, cross-encoder reranking, and query routing.

---

## 4. What Is the Final System Architecture?

The final pipeline is:

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
Top Evidence Chunks
  ↓
LLM Answer Generation
  ↓
Answer with Sources
```

This architecture is more reliable than directly retrieving chunks from the entire corpus.

---

## 5. What Is Hierarchical Retrieval?

Hierarchical retrieval means the system first retrieves relevant papers, then retrieves chunks from those candidate papers.

Instead of doing:

```text
query → all chunks → answer
```

the system does:

```text
query → candidate papers → chunks from candidate papers → answer
```

This helps reduce cross-paper confusion and makes retrieval more structured.

For example, if the user asks:

```text
How does AdaDetectGPT work?
```

the system should first identify the AdaDetectGPT paper and then retrieve chunks from that paper.

If the user asks:

```text
What AI-generated text detection methods are discussed in these papers?
```

the system should retrieve evidence from multiple papers.

---

## 6. What Is the Paper-level Catalog?

The paper-level catalog is a document-level index.

Each paper is represented by a catalog entry containing information such as:

```text
title
source file
abstract
first-page excerpt
aliases
keywords
method type
manual summary
```

The paper catalog helps the system decide which papers are relevant to a query.

It is especially useful when the user asks about a specific method or compares several methods.

---

## 7. Why Use Hybrid Retrieval?

I used both dense retrieval and BM25 retrieval.

Dense retrieval is good at semantic matching. It can retrieve conceptually related chunks even when the wording is different.

BM25 is good at exact keyword matching. It is especially useful for academic papers because many important terms are exact names or abbreviations, such as:

```text
DetectGPT
AdaDetectGPT
Fast-DetectGPT
logits
watermark
AUROC
FNR
TNR
statistical guarantees
```

By combining dense retrieval and BM25, the system can benefit from both semantic recall and keyword recall.

---

## 8. What Does the Reranker Do?

The dense retriever and BM25 retriever return candidate chunks.

However, not all candidate chunks are equally useful.

The cross-encoder reranker takes the query and each candidate chunk as a pair and assigns a relevance score.

Then the system keeps the top-ranked chunks as final evidence.

The reranker improves the quality of the context passed to the LLM.

The retrieval pipeline becomes:

```text
dense candidates
+
BM25 candidates
  ↓
merge
  ↓
rerank
  ↓
top chunks
```

---

## 9. What Does the Query Router Do?

The query router classifies user questions into different types.

The current router supports:

```text
method
comparison
survey
evidence
experiment
general
```

Each query type uses different retrieval parameters.

For example:

| Query Type | Example | Strategy |
|---|---|---|
| method | How does AdaDetectGPT work? | Auto / specific-paper retrieval |
| comparison | What is the difference between DetectGPT and AdaDetectGPT? | Multi-paper retrieval |
| survey | What methods are discussed? | Global diverse retrieval |
| evidence | Which methods provide statistical guarantees? | Global evidence retrieval |
| experiment | What datasets are used? | Experiment-oriented retrieval |

This makes the retrieval system adaptive rather than fixed.

---

## 10. How Did You Reduce Noisy Retrieval?

I used metadata and filtering.

Each chunk has metadata such as:

```text
source
page
chunk_id
chunk_type
```

The `chunk_type` field can mark whether a chunk is:

```text
main
checklist
references
appendix
```

During retrieval, the system can prioritize main-text chunks and avoid noisy sections.

This is important because some paper checklists contain words such as "abstract", "introduction", and "contribution", which can mislead the retriever.

---

## 11. How Did You Evaluate the System?

I evaluated the system at several levels.

### 11.1 Retrieval Evaluation

I checked whether retrieved chunks came from reasonable papers and whether they were useful for answering the question.

### 11.2 Reranker Ablation

I compared:

```text
vector-only retrieval
vs
vector retrieval + reranker
```

This helped check whether the reranker improved chunk ranking.

### 11.3 Hybrid Retrieval Evaluation

I compared:

```text
dense only
BM25 only
hybrid + reranker
```

This helped evaluate whether BM25 and dense retrieval complement each other.

### 11.4 Query Router Evaluation

I checked whether the router classified questions correctly and whether the selected retrieval strategy was reasonable.

### 11.5 Answer-level Evaluation

I evaluated final answers using criteria such as:

```text
answer relevance
groundedness
citation support
completeness
hallucination risk
```

---

## 12. What Is Answer-level Evaluation?

Answer-level evaluation checks the final output of the RAG system.

For each question, the system generates an answer and evaluates whether:

1. the answer addresses the question;
2. the claims are supported by retrieved context;
3. the cited sources support the answer;
4. the answer is complete enough;
5. the answer avoids hallucination.

This is important because good retrieval does not automatically guarantee a good answer.

---

## 13. What Is the Streamlit Demo?

I built a Streamlit demo for interactive use.

The demo allows the user to:

1. enter a question;
2. run the engineered RAG pipeline;
3. view the final answer;
4. inspect the query route;
5. inspect candidate papers;
6. inspect selected papers;
7. inspect retrieved chunks;
8. view vector, BM25, and reranker scores.

This makes the system easier to demonstrate and debug.

---

## 14. What Was the Hardest Part?

The hardest part was improving retrieval quality.

At first, the system could run, but it sometimes retrieved irrelevant chunks, especially checklist or appendix text.

I learned that prompt engineering alone cannot solve poor retrieval.

The main improvements came from:

1. adding metadata;
2. building a paper-level catalog;
3. using hybrid retrieval;
4. adding a reranker;
5. evaluating retrieval results systematically.

---

## 15. What Was the Most Important Lesson?

The most important lesson is:

```text
RAG quality depends more on retrieval quality than on prompt wording alone.
```

If the retrieved context is wrong, the LLM cannot reliably answer the question.

A practical RAG system needs:

```text
good indexing
good metadata
good retrieval strategy
reranking
evaluation
```

---

## 16. What Are the Current Limitations?

The current system still has several limitations.

First, the paper catalog partly relies on manual metadata.

Second, the query router is rule-based.

Third, section-level metadata is still coarse.

Fourth, the Streamlit app is currently read-only and does not support uploading new PDFs from the UI.

Fifth, the answer-level evaluation uses LLM-as-a-judge, which is useful but approximate.

Finally, the evaluation dataset is still small.

---

## 17. How Would You Improve It Next?

I would improve the system in several directions.

First, I would add automatic paper metadata extraction, such as extracting method names, tasks, and contributions.

Second, I would add section-level chunk labeling, such as abstract, introduction, method, experiment, and conclusion.

Third, I would support PDF upload and online indexing in the Streamlit app.

Fourth, I would add citation-level verification.

Fifth, I would build a gold-standard evaluation set with human-written reference answers.

Finally, I would deploy the app as a web service.

---

## 18. How Would You Explain the Project in a Resume?

One possible resume bullet is:

```text
Built an engineered RAG system for academic paper QA, including PDF ingestion, hierarchical paper-level retrieval, hybrid dense/BM25 retrieval, cross-encoder reranking, query routing, source-grounded answer generation, Streamlit demo, and multi-level evaluation for retrieval and answer quality.
```

A more concise version is:

```text
Developed a paper QA RAG system with hierarchical retrieval, hybrid BM25/vector search, reranking, query routing, and answer-level evaluation.
```

---

## 19. Possible Interview Questions and Answers

### Q1. Why did you use both dense retrieval and BM25?

Dense retrieval captures semantic similarity, while BM25 captures exact keyword matches. Academic papers contain many method names and technical terms, so BM25 is useful for terms like DetectGPT, logits, AUROC, and statistical guarantees.

### Q2. Why did you add a reranker?

The first-stage retrievers are mainly for recall. They may return noisy candidates. The reranker scores query-chunk pairs more precisely and improves the final context quality.

### Q3. What problem does hierarchical retrieval solve?

It reduces cross-paper confusion. Instead of searching all chunks directly, the system first retrieves relevant papers, then retrieves chunks from selected papers.

### Q4. How do you reduce hallucination?

The answer prompt requires the model to answer only based on retrieved context and cite sources. I also evaluate groundedness, citation support, and hallucination risk in the answer-level evaluation.

### Q5. What would you improve next?

I would improve automatic paper metadata extraction, add section-aware retrieval, support PDF upload and online indexing, and build a stronger gold-standard evaluation dataset.

---

## 20. Two-minute Project Explanation

I built a RAG system for academic paper question answering.

The first version was a basic PDF RAG pipeline: load papers, split them into chunks, build a vector database, retrieve chunks, and generate answers with an LLM.

Then I found that simple vector search was not reliable enough. It could confuse papers, retrieve irrelevant chunks, or miss exact technical terms. So I upgraded the system.

The final version uses hierarchical retrieval. It first retrieves candidate papers from a paper-level catalog, then retrieves chunks from those papers. For chunk retrieval, I combine dense embedding search and BM25 keyword search. Dense retrieval helps with semantic similarity, while BM25 helps with exact terms and method names. After merging candidates, I use a cross-encoder reranker to select the most relevant chunks.

I also added a query router that classifies questions into types such as method, comparison, survey, evidence, and experiment, and adjusts retrieval parameters accordingly.

Finally, I built several evaluation scripts to evaluate retrieval quality, reranker performance, hybrid retrieval, query routing, and final answer quality. I also built a Streamlit demo to make the system interactive.

The main lesson I learned is that practical RAG is not just prompt engineering. The core is retrieval design, metadata, reranking, and evaluation.