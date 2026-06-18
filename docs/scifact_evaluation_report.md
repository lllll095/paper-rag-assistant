# SciFact Retrieval Evaluation Report

## 1. 评测目的

本实验使用 BEIR/SciFact 作为标准检索评测数据集，评估 Paper RAG Assistant 中不同检索策略的效果，包括 BM25、Dense Retrieval、Hybrid Retrieval 和 Hybrid + Cross-Encoder Reranker。

## 2. 数据集

SciFact 是一个 scientific claim retrieval 数据集，包含 scientific claims、scientific corpus 和 relevance labels。该数据集自带 qrels，因此可以直接计算 Recall@k、MRR@k 和 nDCG@k 等标准检索指标。

## 3. 对比方法

| 方法 | 说明 |
|---|---|
| BM25 | 关键词检索 baseline |
| Dense | 基于 embedding 的语义检索 |
| Hybrid | Dense score 和 BM25 score 融合 |
| Hybrid + Reranker | 先 hybrid 召回 top-N，再用 cross-encoder reranker 重排 |

## 4. 评测指标

| 指标 | 含义 |
|---|---|
| Hit@10 | top-10 中是否至少命中一个相关文档 |
| Precision@10 | top-10 中相关文档比例 |
| Recall@10 | top-10 召回的相关文档比例 |
| MRR@10 | 第一个相关文档出现位置的倒数平均 |
| nDCG@10 | 考虑相关性等级和排序位置的综合排序指标 |

## 5. 实验结果

把 summarize 脚本输出的表格贴到这里。

## 6. 结果分析

根据实际结果写：

- BM25 是否对科学术语检索更稳；
- Dense 是否在语义相关问题上表现更好；
- Hybrid 是否相比单一检索有提升；
- Reranker 是否提升 MRR@10 / nDCG@10；
- 如果 reranker 没提升，可能是模型 domain mismatch 或初始召回候选质量问题。

## 7. 结论

本实验表明 Paper RAG Assistant 不只是实现了 RAG pipeline，还能够用标准 IR benchmark 对 retrieval、hybrid retrieval 和 reranking 进行系统评估。