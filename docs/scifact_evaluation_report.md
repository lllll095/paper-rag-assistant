````markdown
# SciFact Retrieval Evaluation Report

本文记录 Paper RAG Assistant 在 BEIR/SciFact 数据集上的检索评测结果。实验目标是评估不同 retrieval strategy 对科学论文证据检索质量的影响，包括 BM25、Dense Retrieval、Hybrid Retrieval 和 Hybrid + Cross-Encoder Reranker。

---

## 1. 评测目的

Paper RAG Assistant 的核心能力之一是从论文语料中检索和排序相关 evidence。为了避免只凭主观样例判断 RAG 效果，本实验使用 BEIR/SciFact 作为标准检索评测数据集，对不同检索模块进行 ablation evaluation。

本实验主要评估：

```text
BM25 only
Dense Retrieval only
Hybrid Retrieval
Hybrid Retrieval + Cross-Encoder Reranker
````

评测重点不是最终 LLM answer quality，而是 retrieval-level quality。

---

## 2. 数据集

本实验使用 BEIR/SciFact。

SciFact 是一个 scientific claim retrieval 数据集。每个 query 是一个 scientific claim，系统需要从 scientific corpus 中检索相关文献或证据文档。

该数据集自带 qrels，也就是 query-document relevance labels，因此可以直接计算标准检索指标，不需要额外人工标注。

本次实验规模：

```text
Corpus size: 5183
Query size: 300
Qrels size: 300
```

---

## 3. 对比方法

| 方法                | 说明                                             |
| ----------------- | ---------------------------------------------- |
| BM25              | 关键词检索 baseline，适合精确术语匹配。                       |
| Dense             | 使用 embedding similarity 进行语义检索。                |
| Hybrid            | 对 BM25 score 和 dense score 进行融合。               |
| Hybrid + Reranker | 先用 Hybrid 召回候选文档，再用 cross-encoder reranker 重排。 |

Hybrid Retrieval 使用 score fusion：

```text
hybrid_score = alpha * dense_score + (1 - alpha) * bm25_score
```

本实验中：

```text
alpha = 0.6
```

---

## 4. 评测指标

| 指标           | 含义                     |
| ------------ | ---------------------- |
| Hit@10       | top-10 中是否至少命中一个相关文档。  |
| Precision@10 | top-10 中相关文档所占比例。      |
| Recall@10    | top-10 召回的相关文档比例。      |
| MRR@10       | 第一个相关文档出现位置的倒数平均。      |
| nDCG@10      | 综合考虑相关性等级和排序位置的排序质量指标。 |

在 RAG 场景中，Recall@10 和 nDCG@10 尤其重要。前者衡量系统是否召回了足够的 evidence，后者衡量高质量 evidence 是否排在更靠前的位置。

---

## 5. 实验结果

| Method            |     Hit@10 | Precision@10 |  Recall@10 |     MRR@10 |    nDCG@10 |
| ----------------- | ---------: | -----------: | ---------: | ---------: | ---------: |
| BM25              |     0.7967 |       0.0853 |     0.7757 |     0.6184 |     0.6523 |
| Dense             |     0.8567 |       0.0953 |     0.8452 |     0.6845 |     0.7200 |
| Hybrid            | **0.8800** |   **0.0963** | **0.8657** | **0.7086** | **0.7429** |
| Hybrid + Reranker |     0.8467 |       0.0933 |     0.8322 |     0.6625 |     0.6960 |

---

## 6. 结果分析

### 6.1 Dense Retrieval 明显优于 BM25

Dense Retrieval 在所有主要指标上都优于 BM25。

例如：

```text
BM25 Recall@10:  0.7757
Dense Recall@10: 0.8452

BM25 nDCG@10:    0.6523
Dense nDCG@10:   0.7200
```

这说明在 SciFact 这种 scientific claim retrieval 场景中，语义检索比纯关键词匹配更有效。很多 scientific claim 和相关论文之间并不是完全字面匹配，而是语义相关，因此 dense embedding 能够召回更多相关 evidence。

---

### 6.2 Hybrid Retrieval 效果最好

Hybrid Retrieval 在所有指标上取得最佳结果：

```text
Hit@10:       0.8800
Precision@10: 0.0963
Recall@10:    0.8657
MRR@10:       0.7086
nDCG@10:      0.7429
```

相比 Dense Retrieval，Hybrid Retrieval 进一步提升：

```text
Recall@10: 0.8452 → 0.8657
MRR@10:    0.6845 → 0.7086
nDCG@10:   0.7200 → 0.7429
```

这说明 BM25 和 Dense Retrieval 具有互补性。

Dense Retrieval 擅长语义相似，BM25 擅长关键词和术语匹配。对于 scientific corpus，许多 query 包含专业术语、实体、指标或方法名，因此 BM25 的精确匹配能力可以补充 dense retrieval 的语义检索能力。

---

### 6.3 Cross-Encoder Reranker 在本实验中没有带来提升

Hybrid + Reranker 的结果低于 Hybrid：

```text
Hybrid Recall@10:             0.8657
Hybrid + Reranker Recall@10:  0.8322

Hybrid MRR@10:                0.7086
Hybrid + Reranker MRR@10:     0.6625

Hybrid nDCG@10:               0.7429
Hybrid + Reranker nDCG@10:    0.6960
```

这说明本次使用的 reranker 没有改善排序，反而降低了检索效果。

一个可能原因是 domain mismatch。本实验使用的 reranker 是：

```text
cross-encoder/ms-marco-MiniLM-L-6-v2
```

该模型主要面向通用 passage ranking 场景，而 SciFact 是 scientific claim retrieval 场景。科学论文中的证据匹配通常依赖专业术语、科研 claim、实验结论和隐含语义，通用 reranker 不一定能准确判断科学证据相关性。

因此，本实验结果说明：reranker 需要通过实际评测验证，不能默认认为加入 reranker 一定提升 RAG 检索质量。

---

## 7. 结论

本次 SciFact retrieval evaluation 表明：

1. Dense Retrieval 明显优于 BM25，说明语义检索对 scientific claim retrieval 很重要。
2. Hybrid Retrieval 取得最佳效果，说明 BM25 和 Dense Retrieval 具有互补性。
3. Cross-Encoder Reranker 在本实验中没有提升效果，可能存在 domain mismatch。
4. RAG 系统中的每个模块都需要通过 ablation evaluation 验证，而不能只凭经验判断。

整体来看，本实验证明 Paper RAG Assistant 不只是实现了 RAG pipeline，还能够用标准 IR benchmark 对 retrieval、hybrid retrieval 和 reranking 进行系统评估。

---

## 8. 面试总结说法

如果面试中被问到“你怎么评估 RAG 检索效果”，可以这样回答：

> 我用 BEIR/SciFact 做了标准 retrieval evaluation，对 BM25、Dense Retrieval、Hybrid Retrieval 和 Hybrid + Cross-Encoder Reranker 做了 ablation。评测指标包括 Hit@10、Precision@10、Recall@10、MRR@10 和 nDCG@10。
>
> 实验结果显示，Dense Retrieval 明显优于 BM25，而 Hybrid Retrieval 在所有指标上最好，说明语义检索和关键词检索是互补的。另一方面，通用 MS MARCO cross-encoder reranker 在 SciFact 上没有提升效果，说明 reranker 存在 domain mismatch，不能默认加 reranker 就一定更好。
>
> 这个实验让我能系统评估 RAG retrieval pipeline，而不是只通过几个 demo case 判断效果。

```
```
