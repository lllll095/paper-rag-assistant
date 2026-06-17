````markdown
# RAG Evaluation 与优化体系总结

本文总结 RAG 系统的评估方法、常见指标、错误分析方式，以及它们和 ResearchPilot / Paper RAG Assistant 的关系。

目标是回答面试中常见问题：

- 你怎么评估 RAG 系统？
- Recall@k、MRR、nDCG 是什么？
- reranker 怎么评估？
- answer-level evaluation 怎么做？
- RAG 出错时怎么 debug？
- hybrid retrieval 为什么有效？

---

## 1. 为什么 RAG 需要分层评估？

一个 RAG 系统通常不是单一模块，而是一条链路：

```text
用户问题
  ↓
Query Routing / Query Rewriting
  ↓
Retrieval
  ↓
Reranking
  ↓
Answer Generation
  ↓
Citation / Grounding / Faithfulness
````

所以 RAG 出错时，不能只看最终答案好不好，而要拆开看：

```text
是 query route 错了？
是 retrieval 没召回证据？
是 reranker 排序错了？
是 LLM 没用好证据？
是引用不能支持答案？
```

因此我会把 RAG evaluation 分成五层：

1. Query Router Evaluation
2. Retrieval-level Evaluation
3. Reranking-level Evaluation
4. Answer-level Evaluation
5. System-level Evaluation

---

## 2. Query Router Evaluation

如果系统中有 query router，比如把问题分成：

```text
method
comparison
survey
evidence
experiment
general
```

那么第一步要评估 router 是否把问题分到了正确类型。

### 2.1 评估方式

构造一个带人工标签的 query set：

| Query                                    | Gold label | Predicted label |
| ---------------------------------------- | ---------- | --------------- |
| What is the main method of AdaDetectGPT? | method     | method          |
| Compare DetectGPT and AdaDetectGPT.      | comparison | comparison      |
| What evidence supports this claim?       | evidence   | general         |

然后计算：

```text
accuracy = 预测正确的 query 数量 / 总 query 数量
```

也可以看每类问题的错误案例。

### 2.2 常见错误

```text
method 问题被分到 general
comparison 问题没有触发多论文对比
evidence 问题没有要求强 citation
experiment 问题没有检索实验设置和结果
```

### 2.3 面试说法

> 如果 RAG 系统有 query router，我会把它当成一个轻量分类器来评估。可以构造一组人工标注 query，标签包括 method、comparison、survey、evidence、experiment、general 等，然后比较 router 输出和人工标签是否一致。router 错了会导致后续检索策略错误，所以它是 RAG pipeline 中需要单独评估的一层。

---

## 3. Retrieval-level Evaluation

Retrieval-level evaluation 评估的是：

```text
检索器有没有把真正相关的 evidence 找出来？
```

这是 RAG 最重要的一层。因为如果正确证据没有被检索出来，后面的 LLM 再强也很难生成可靠答案。

---

## 4. Recall@k

### 4.1 定义

Recall@k 衡量的是：

```text
前 k 个检索结果覆盖了多少相关文档 / chunk。
```

公式：

```text
Recall@k = 前 k 个结果中相关结果数量 / 所有相关结果数量
```

### 4.2 例子

假设某个 query 的真实相关 chunks 是：

```text
A, B, C
```

系统返回的前 5 个 chunks 是：

```text
A, D, E, B, F
```

其中命中了 A 和 B，一共 2 个。

那么：

```text
Recall@5 = 2 / 3
```

### 4.3 RAG 中为什么重要？

RAG 更关心 Recall@k，因为：

```text
只要相关证据没被召回，LLM 就没有材料可以回答。
```

所以 retrieval 阶段通常优先保证高 recall。

### 4.4 面试说法

> Recall@k 对 RAG 非常重要，因为它衡量的是系统有没有把正确 evidence 召回到上下文中。如果相关证据没有被检索出来，后面的 reranker 和 LLM generation 都很难补救。

---

## 5. Precision@k

### 5.1 定义

Precision@k 衡量的是：

```text
前 k 个检索结果中，有多少比例是相关的。
```

公式：

```text
Precision@k = 前 k 个结果中相关结果数量 / k
```

### 5.2 例子

如果前 5 个结果是：

```text
A, D, E, B, F
```

其中 A 和 B 相关，那么：

```text
Precision@5 = 2 / 5
```

### 5.3 和 Recall@k 的区别

```text
Recall@k 关注有没有召回足够多的正确证据；
Precision@k 关注返回结果里噪声多不多。
```

RAG 中常常先追求 Recall，再通过 reranker 提升 Precision 和排序质量。

---

## 6. Hit@k

### 6.1 定义

Hit@k 只关心：

```text
前 k 个结果里有没有至少一个相关结果。
```

如果有：

```text
Hit@k = 1
```

如果没有：

```text
Hit@k = 0
```

### 6.2 适用场景

如果一个问题只需要一个关键证据，Hit@k 很直观。

但如果一个问题需要多个证据，Hit@k 不够细。

---

## 7. MRR

MRR 全称是 Mean Reciprocal Rank。

它关注：

```text
第一个相关结果排在第几位。
```

### 7.1 单个 query 的 RR

如果第一个相关结果排第 1 位：

```text
RR = 1 / 1 = 1
```

如果第一个相关结果排第 3 位：

```text
RR = 1 / 3
```

如果前面没有相关结果：

```text
RR = 0
```

MRR 就是多个 query 的 RR 平均值。

### 7.2 为什么适合评估 reranker？

reranker 的目标之一是：

```text
把最相关的 evidence 排到更前面。
```

所以 MRR 很适合看第一个相关证据是否被提前。

### 7.3 面试说法

> MRR 衡量第一个相关结果出现的位置。对于 RAG 来说，如果正确 evidence 排得越靠前，越容易被 LLM 使用。因此 MRR 适合评估检索排序质量，也适合做 reranker ablation。

---

## 8. nDCG@k

nDCG 衡量的是排序质量，适合相关性不是 0/1，而是有等级的情况。

例如人工标注相关性：

```text
3 = highly relevant
2 = relevant
1 = weakly relevant
0 = irrelevant
```

如果高相关 evidence 排在前面，nDCG 就高。

如果高相关 evidence 被排到后面，nDCG 就低。

### 8.1 为什么有用？

RAG 中很多 chunk 不是简单相关 / 不相关，而是有强弱之分：

```text
直接回答问题的 chunk：highly relevant
背景介绍 chunk：weakly relevant
无关 chunk：irrelevant
```

nDCG 可以反映这种分级相关性。

### 8.2 面试说法

> nDCG@k 适合评估排序质量，尤其是相关性有等级的时候。对于 RAG，如果最有信息量的 evidence 被排在更前面，nDCG 会更高。因此它适合评估 dense retrieval、hybrid retrieval 和 reranker 的排序效果。

---

## 9. Reranking-level Evaluation

Reranker 的作用不是从全库检索，而是：

```text
对初筛出来的候选 chunks 重新排序。
```

例如：

```text
Dense/BM25 初筛 50 个 chunks
  ↓
Cross-Encoder Reranker 重新打分
  ↓
保留 top 5 作为 LLM 上下文
```

### 9.1 怎么评估 reranker？

做 ablation：

```text
without reranker
vs
with reranker
```

比较：

```text
Recall@k
MRR
nDCG@k
answer-level quality
```

如果 reranker 有效，通常会看到：

```text
MRR 提升
nDCG@k 提升
top-k 中噪声减少
answer faithfulness 更好
```

### 9.2 面试说法

> 我会用 ablation 评估 reranker：比较使用和不使用 cross-encoder reranker 时的 MRR、nDCG@k 和最终 answer quality。reranker 的目标是把真正相关的 evidence 排到更前面，所以它对 MRR 和 nDCG 的影响通常比对 Recall 更明显。

---

## 10. Hybrid Retrieval Evaluation

Hybrid retrieval 通常结合：

```text
Dense Retrieval
+
BM25 Keyword Retrieval
```

### 10.1 为什么 dense 和 BM25 互补？

Dense retrieval 擅长语义相似：

```text
“如何检测 AI 生成文本”
≈
“machine-generated text detection method”
```

BM25 擅长精确匹配：

```text
DetectGPT
AdaDetectGPT
AUROC
FNR
p-value
conformal prediction
```

在学术论文 RAG 中，很多问题包含方法名、数据集名、指标名和术语，所以 BM25 很重要。

### 10.2 怎么评估 hybrid retrieval？

做三组 ablation：

```text
dense only
BM25 only
dense + BM25 hybrid
```

比较：

```text
Recall@k
MRR
nDCG@k
answer quality
```

### 10.3 面试说法

> 我会通过 ablation 评估 hybrid retrieval：分别比较 dense only、BM25 only 和 hybrid retrieval。Dense retrieval 擅长语义相似，BM25 擅长术语和方法名精确匹配。对于论文问答，很多 query 包含 AdaDetectGPT、AUROC、conformal p-value 这类精确术语，因此 hybrid retrieval 通常比单一 dense retrieval 更稳。

---

## 11. Answer-level Evaluation

Retrieval 做得好，不代表答案一定好。LLM 可能：

```text
没有正确使用证据
过度总结
编造不存在的内容
引用不支持论断
没有回答完整
```

所以还需要 answer-level evaluation。

常见维度：

| 维度                 | 含义           |
| ------------------ | ------------ |
| Answer relevance   | 答案是否回答了用户问题  |
| Faithfulness       | 答案是否忠实于检索证据  |
| Citation support   | 引用是否支持对应论断   |
| Hallucination risk | 是否有证据中不存在的内容 |
| Completeness       | 是否覆盖问题主要方面   |

### 11.1 Faithfulness

Faithfulness 问的是：

```text
答案里的论断是否能从 evidence 中推出。
```

如果答案说：

```text
方法 A 显著优于方法 B
```

但 evidence 里没有这个比较，那就是 faithfulness 问题。

### 11.2 Citation Support

Citation support 问的是：

```text
答案引用的 source 是否真的支持该句论断。
```

这在论文 RAG 中非常重要，因为面试官会关心 source-grounded answer。

### 11.3 面试说法

> Answer-level evaluation 不只是看答案是否流畅，而是看答案是否 relevant、faithful、citation-supported。对于论文 RAG，我尤其关注 citation support，因为每个关键论断最好都能被检索到的 source 支持。

---

## 12. System-level Evaluation

如果 RAG 系统要工程化，还要看系统指标：

```text
latency
cost
token usage
fallback rate
API error rate
retrieval time
reranking time
generation time
```

例如：

```text
reranker 可能提升质量，但增加延迟；
top_k 越大，recall 可能提升，但 token cost 也上升；
fallback 能提升成功率，但会增加耗时。
```

### 12.1 面试说法

> 工程化 RAG 不能只看答案质量，还要看 latency、cost 和稳定性。例如 reranker 可能提升 faithfulness，但会增加延迟；top_k 增大可能提升 recall，但也会增加 token cost。所以需要在质量、速度和成本之间做 trade-off。

---

## 13. RAG 错误分析

当 RAG 答案错了，可以按链路定位。

### 13.1 答案错，但检索结果里有正确证据

说明 retrieval 没问题，问题可能在：

```text
prompt
answer generation
citation grounding
LLM 没有正确使用 evidence
```

优化方向：

```text
改 prompt
要求先列 evidence 再回答
增加 citation constraint
增加 reviewer / verifier
```

---

### 13.2 答案错，检索结果里没有正确证据

说明 retrieval 有问题。

优化方向：

```text
调整 chunk size
调整 top_k
更换 embedding model
加入 BM25
使用 hybrid retrieval
query rewriting
metadata filtering
```

---

### 13.3 正确证据检索到了，但排得靠后

说明 ranking 有问题。

优化方向：

```text
加入 reranker
调整 dense/BM25 融合权重
调整 reranker top_n
使用 nDCG / MRR 做排序评估
```

---

### 13.4 问题类型判断错了

说明 query router 有问题。

优化方向：

```text
增加规则
增加 few-shot examples
构造 router evaluation set
让 router 输出结构化标签
```

---

## 14. 和 Paper RAG Assistant 的对应关系

Paper RAG Assistant 中可以这样对应：

| 项目模块                   | 评估方式                                                 |
| ---------------------- | ---------------------------------------------------- |
| Query Router           | router accuracy / case study                         |
| Dense Retrieval        | Recall@k / MRR                                       |
| BM25 Retrieval         | keyword hit rate / Recall@k                          |
| Hybrid Retrieval       | dense vs BM25 vs hybrid ablation                     |
| Cross-Encoder Reranker | reranker ablation / MRR / nDCG                       |
| Answer Generation      | answer relevance / faithfulness                      |
| Citation               | citation support / hallucination risk                |
| Full Pipeline          | answer-level evaluation / qualitative error analysis |

---

## 15. 面试完整回答

如果面试官问：

> 你怎么评估一个 RAG 系统？

可以这样回答：

> 我会把 RAG evaluation 拆成 retrieval-level、reranking-level 和 answer-level 三层。
>
> 第一层是 retrieval-level，主要看 Recall@k、MRR 等指标，判断相关 evidence 有没有被检索出来。因为如果证据没有被召回，后面的 LLM 很难生成 grounded answer。
>
> 第二层是 reranking-level，我会做 ablation，对比使用 cross-encoder reranker 前后的 MRR、nDCG@k 或 answer quality，判断 reranker 是否真的把相关 evidence 排到了更前面。
>
> 第三层是 answer-level，主要看 answer relevance、faithfulness、citation support 和 hallucination risk。RAG 的目标不是生成流畅答案，而是生成被 evidence 支持的答案。
>
> 在 Paper RAG Assistant 里，我做了 retrieval evaluation、reranker ablation、hybrid retrieval evaluation、query router evaluation 和 answer-level evaluation，用来分别评估检索、排序、路由和最终答案质量。

---

## 16. 核心记忆点

面试前重点记住：

```text
Recall@k：有没有召回相关证据。
Precision@k：返回结果里噪声多不多。
MRR：第一个相关结果排得多靠前。
nDCG：高相关结果是否排在前面。
Reranker ablation：比较 reranker 前后排序质量。
Hybrid retrieval：dense 负责语义，BM25 负责关键词。
Faithfulness：答案是否忠实于 evidence。
Citation support：引用是否支持对应论断。
RAG debug：先判断是 retrieval 问题、ranking 问题、generation 问题，还是 router 问题。
```

```
```
