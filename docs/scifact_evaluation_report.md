
## Project-level EngineeredRAG Evaluation

除了独立实现 BM25、Dense、Hybrid 和 Hybrid + Reranker 之外，本项目还进一步将 BEIR/SciFact corpus 构造成 Paper RAG Assistant 兼容的 Chroma index，并调用项目真实的 `EngineeredRAG.retrieve()` pipeline 进行评测。

该流程不再是单独的 flat retrieval，而是完整经过项目内部的分层检索链路：

```text
SciFact query
  -> paper-level catalog retrieval
  -> candidate paper selection
  -> chunk-level dense retrieval
  -> BM25 retrieval
  -> candidate merge
  -> cross-encoder reranking
  -> retrieved documents
  -> metric computation
````

因此，这一部分评测的是 Paper RAG Assistant 的真实系统级检索能力，而不仅是单独检索模块的性能。

### Project EngineeredRAG Results

| Setting                                            |     Hit@10 | Precision@10 |  Recall@10 |     MRR@10 |    nDCG@10 |
| -------------------------------------------------- | ---------: | -----------: | ---------: | ---------: | ---------: |
| Project EngineeredRAG, `paper_k=50`, `chunk_k=10`  | **0.8300** |   **0.0913** | **0.8146** | **0.6625** | **0.6932** |
| Project EngineeredRAG, `paper_k=100`, `chunk_k=10` |     0.8200 |       0.0907 |     0.8046 |     0.6580 |     0.6866 |
| Project EngineeredRAG, `paper_k=200`, `chunk_k=10` |     0.8233 |       0.0907 |     0.8072 |     0.6594 |     0.6881 |
| Project EngineeredRAG, `paper_k=50`, `chunk_k=20`  | **0.8300** |   **0.0913** | **0.8146** | **0.6625** | **0.6932** |

The best project-level setting is `paper_k=50, chunk_k=10`, achieving:

```text
Hit@10    = 0.8300
Recall@10 = 0.8146
MRR@10    = 0.6625
nDCG@10   = 0.6932
```

This means that, over 300 SciFact queries, the full EngineeredRAG pipeline retrieves at least one relevant document in the top-10 results for 83.00% of queries, and achieves Recall@10 of 81.46%.

### Comparison with Flat Retrieval

| Method                |     Hit@10 | Precision@10 |  Recall@10 |     MRR@10 |    nDCG@10 |
| --------------------- | ---------: | -----------: | ---------: | ---------: | ---------: |
| BM25                  |     0.7967 |       0.0853 |     0.7757 |     0.6184 |     0.6523 |
| Dense                 |     0.8567 |       0.0953 |     0.8452 |     0.6845 |     0.7200 |
| Hybrid                | **0.8800** |   **0.0963** | **0.8657** | **0.7086** | **0.7429** |
| Hybrid + Reranker     |     0.8467 |       0.0933 |     0.8322 |     0.6625 |     0.6960 |
| Project EngineeredRAG |     0.8300 |       0.0913 |     0.8146 |     0.6625 |     0.6932 |

The flat Hybrid retriever obtains the best overall retrieval performance on SciFact. This is expected because SciFact is a short scientific document retrieval benchmark: each corpus item is relatively short and can be directly ranked against the query.

By contrast, Project EngineeredRAG is a hierarchical long-paper RAG pipeline. It first retrieves candidate papers from a paper-level catalog, then performs chunk-level retrieval and reranking within selected candidate papers. This design is more suitable for long PDF paper collections, where each paper contains many chunks and paper-level routing helps reduce search space.

Therefore, the slightly lower Project EngineeredRAG score does not indicate that the project pipeline is ineffective. Instead, it reflects a task mismatch:

```text
SciFact:
  many short scientific documents
  -> flat retrieval is naturally strong

Paper RAG Assistant:
  fewer long PDF papers
  -> hierarchical paper-level routing is useful
```

Even with this mismatch, the full Project EngineeredRAG pipeline still achieves Recall@10 = 0.8146 and nDCG@10 = 0.6932, showing that the real system can be connected to a standard IR benchmark and evaluated reproducibly.

### Parameter Ablation

The project-level ablation shows that increasing `paper_k` from 50 to 100 or 200 does not improve the final retrieval metrics. Similarly, increasing `chunk_k` from 10 to 20 produces almost identical results.

This suggests that the main bottleneck is not simply the number of candidate papers or chunks. Instead, the performance is likely limited by the ranking behavior of the full hierarchical pipeline and by the mismatch between SciFact's short-document claim retrieval setting and the project's original long-PDF RAG setting.

In particular:

1. `paper_k=50` is already sufficient for this benchmark.
2. Increasing `paper_k` introduces more candidate documents but does not improve top-10 ranking.
3. Increasing `chunk_k` does not change the final top-10 results.
4. The flat Hybrid retriever remains the strongest method for SciFact.
5. The full EngineeredRAG pipeline remains valuable as a system-level evaluation of the actual project retrieval process.

### Main Conclusion

The SciFact evaluation gives two complementary conclusions.

First, at the module level, Hybrid Retrieval performs best, showing that BM25 and Dense Retrieval are complementary for scientific retrieval. BM25 helps with exact scientific terms, while Dense Retrieval captures semantic similarity.

Second, at the system level, the real Project EngineeredRAG pipeline can be evaluated on a standard benchmark and achieves reasonable retrieval quality. Although it is slightly weaker than flat Hybrid Retrieval on SciFact, this is expected because the project pipeline is designed for long academic PDFs rather than short scientific abstracts.

Overall, this evaluation demonstrates that Paper RAG Assistant is not just a demo system. It supports reproducible retrieval evaluation, module-level ablation, and system-level diagnosis.


