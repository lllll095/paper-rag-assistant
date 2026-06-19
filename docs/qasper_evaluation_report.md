````markdown
# QASPER Evidence Retrieval Evaluation Report

This report evaluates the long-paper evidence retrieval ability of **Paper RAG Assistant** on QASPER. Unlike SciFact, which is mainly a short scientific document retrieval benchmark, QASPER is closer to the long-paper RAG setting: each example is associated with a scientific paper, a question, annotated answers, and supporting evidence.

The goal of this evaluation is not to directly benchmark final answer generation, but to test whether the retrieval pipeline can locate supporting evidence within long scientific papers.

---

## 1. Evaluation Goal

Paper RAG Assistant is designed for academic paper question answering. Its retrieval pipeline includes:

```text
paper-level routing
  -> chunk-level dense retrieval
  -> BM25 retrieval
  -> candidate merging
  -> cross-encoder reranking
  -> source-grounded answer generation
````

For QASPER, we focus on the retrieval part:

```text
given a question
  -> retrieve relevant chunks from scientific papers
  -> compare retrieved chunks with annotated evidence
```

This helps answer the following question:

> Can the system retrieve the supporting evidence needed to answer long-paper questions?

---

## 2. Dataset

We use the local QASPER v0.3 dataset.

QASPER is organized as:

```text
paper_id -> paper object
```

Each paper object contains:

```text
title
abstract
full_text
qas
figures_and_tables
```

The `full_text` field is a list of paper sections. Each section contains a `section_name` and a list of `paragraphs`.

Each QA example contains:

```text
question
question_id
answers
```

Each answer may contain:

```text
free_form_answer
extractive_spans
yes_no
evidence
highlighted_evidence
```

For the training split inspection, we observed:

| Item                       |  Count |
| -------------------------- | -----: |
| Papers                     |    888 |
| Questions                  |  2,593 |
| Answers                    |  2,675 |
| Sections                   | 12,450 |
| Paragraphs                 | 47,687 |
| Evidence items             |  4,209 |
| Highlighted evidence items |  3,579 |

---

## 3. Index Construction

We convert QASPER papers into project-compatible Chroma indexes.

Two vectorstores are built:

```text
eval/qasper_project_index/chunk_db
eval/qasper_project_index/paper_catalog_db
```

The Chroma collection names are aligned with the real Paper RAG Assistant project:

```text
chunk collection   = paper_rag_week1
catalog collection = paper_catalog_week2
```

### Paper-level catalog

For each QASPER paper, we create one catalog document:

```text
title + abstract
```

with metadata:

```text
source = paper_id
paper_id = paper_id
dataset = qasper
```

### Chunk-level documents

For each paragraph in the paper full text, we create one chunk document:

```text
Title: <paper title>
Section: <section name>

<paragraph text>
```

with metadata:

```text
source = paper_id
paper_id = paper_id
paragraph_id = paper_id::section_idx::paragraph_idx
section_name = section_name
chunk_type = main
dataset = qasper
```

This allows the real `EngineeredRAG` pipeline to retrieve QASPER chunks in the same way it retrieves chunks from PDF papers.

---

## 4. Evaluation Settings

We evaluate two settings.

### 4.1 End-to-end open-corpus retrieval

In this setting, the system receives only the question:

```text
question
  -> paper-level routing over QASPER dev papers
  -> chunk retrieval
  -> evidence matching
```

This is a difficult setting because many QASPER questions are paper-specific and under-specified without knowing the target paper.

For example, questions such as:

```text
What is the seed lexicon?
What dataset is used?
What baselines are compared?
```

are hard to route across many papers without the original paper context.

### 4.2 Oracle-paper evidence retrieval

In this setting, the gold paper is given:

```text
gold paper_id + question
  -> retrieve chunks only from the target paper
  -> compare retrieved chunks with gold evidence
```

This is closer to the original QASPER task, where each question is associated with a given paper. It directly evaluates whether the system can locate supporting evidence within a long scientific paper.

---

## 5. Metrics

We use retrieval-oriented evidence matching metrics.

| Metric                       | Meaning                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------------ |
| `paper_hit@k`                | Whether top-k retrieved chunks contain at least one chunk from the gold paper.       |
| `evidence_hit@k`             | Whether top-k retrieved chunks match any annotated QASPER evidence item.             |
| `highlighted_hit@k`          | Whether top-k retrieved chunks match any highlighted evidence item.                  |
| `avg_best_evidence_score`    | Average best fuzzy matching score between retrieved chunks and gold evidence.        |
| `avg_best_highlighted_score` | Average best fuzzy matching score between retrieved chunks and highlighted evidence. |

Evidence matching uses normalized text matching, exact containment, token-level overlap, and fuzzy matching. These are retrieval-oriented hit metrics and are **not directly comparable** to the official QASPER Answer F1 / Evidence F1 metrics.

---

## 6. End-to-End Open-Corpus Retrieval Result

We first evaluate the full open-corpus setting on a small sample of 20 examples.

| Metric                       |  Value |
| ---------------------------- | -----: |
| Number of examples           |     20 |
| `paper_hit@k`                | 0.2000 |
| `evidence_hit@k`             | 0.2000 |
| `highlighted_hit@k`          | 0.2000 |
| `avg_best_evidence_score`    | 0.3185 |
| `avg_best_highlighted_score` | 0.3579 |

The result is low because this setting requires the system to identify the target paper from the question alone. This is not the most natural QASPER setup, since QASPER questions are usually written with a specific paper in mind.

This result suggests that QASPER is not ideal as a pure open-corpus paper-routing benchmark without additional paper context.

---

## 7. Oracle-Paper Evidence Retrieval Result

We then evaluate the oracle-paper setting on the QASPER dev split.

In this setting, the gold paper is given, and the system retrieves evidence chunks only from that paper.

| Metric                       |      Value |
| ---------------------------- | ---------: |
| Number of examples           |      1,553 |
| `paper_hit@k`                |     1.0000 |
| `evidence_hit@k`             | **0.7869** |
| `highlighted_hit@k`          | **0.7276** |
| `avg_best_evidence_score`    | **0.8304** |
| `avg_best_highlighted_score` | **0.7989** |

This result shows that, when the target paper is known, Paper RAG Assistant can retrieve supporting evidence effectively from long scientific papers.

In particular:

```text
evidence_hit@k = 0.7869
highlighted_hit@k = 0.7276
```

This means that the system retrieves QASPER annotated evidence in the top-k chunks for 78.69% of evidence-bearing examples, and retrieves highlighted evidence for 72.76% of examples.

---

## 8. Analysis

The comparison between the two settings is important.

| Setting                             | `paper_hit@k` | `evidence_hit@k` | `highlighted_hit@k` |
| ----------------------------------- | ------------: | ---------------: | ------------------: |
| End-to-end open-corpus, 20 examples |        0.2000 |           0.2000 |              0.2000 |
| Oracle-paper, 1,553 examples        |        1.0000 |       **0.7869** |          **0.7276** |

The large gap suggests that the main difficulty in the end-to-end setting is paper-level routing, not within-paper evidence retrieval.

This is expected because QASPER is primarily a long-document QA dataset. Many questions are meaningful only when the associated paper is known. Therefore, the oracle-paper setting is a more appropriate evaluation for long-paper evidence retrieval.

The oracle-paper result demonstrates that the system's chunk-level retrieval and reranking pipeline can effectively locate supporting evidence inside long scientific papers.

---

## 9. Relationship with Official QASPER Metrics

The official QASPER evaluation usually reports Answer F1 and Evidence F1. Our current metrics are different.

Our evaluation reports:

```text
evidence_hit@k
highlighted_hit@k
avg_best_evidence_score
avg_best_highlighted_score
```

These are retrieval-oriented diagnostic metrics. They measure whether the system can retrieve evidence chunks, not whether the final generated answer exactly matches the gold answer.

Therefore, the oracle-paper result should be interpreted as evidence retrieval performance, not as official QASPER leaderboard performance.

A more complete future evaluation could add:

```text
retrieved evidence
  -> LLM answer generation
  -> official QASPER Answer F1 / Evidence F1
```

---

## 10. Conclusion

The QASPER evaluation gives two main conclusions.

First, QASPER is not ideal as a pure open-corpus paper-routing benchmark when only the question is provided, because many questions are paper-specific and depend on the target paper context.

Second, under the oracle-paper setting, Paper RAG Assistant performs well on long-paper evidence retrieval. Over 1,553 QASPER dev examples, the system achieves:

```text
evidence_hit@k = 0.7869
highlighted_hit@k = 0.7276
avg_best_evidence_score = 0.8304
```

This shows that the system can effectively retrieve supporting evidence from long scientific papers.

Together with the SciFact retrieval evaluation, this provides a more complete evaluation picture:

```text
SciFact:
  short scientific document retrieval
  module-level BM25 / Dense / Hybrid / Reranker ablation

QASPER:
  long-paper evidence retrieval
  oracle-paper within-document evidence localization
```

Overall, these evaluations show that Paper RAG Assistant is not only a demo RAG system, but also a reproducible and diagnosable academic-paper RAG pipeline.

```
```
