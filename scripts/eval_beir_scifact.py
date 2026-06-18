"""
Evaluate retrieval performance on BEIR / SciFact.

This script is a standalone evaluation runner for paper-rag-assistant.

It evaluates retrieval-level performance only, not final LLM answer quality.

Supported modes:
- bm25
- dense
- hybrid
- hybrid_rerank

Metrics:
- Hit@k
- Precision@k
- Recall@k
- MRR@k
- nDCG@k

Example:

python scripts/eval_beir_scifact.py --mode bm25 --top_k 10
python scripts/eval_beir_scifact.py --mode dense --top_k 10
python scripts/eval_beir_scifact.py --mode hybrid --top_k 10 --alpha 0.6
python scripts/eval_beir_scifact.py --mode hybrid_rerank --top_k 10 --rerank_top_n 50
"""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path
from typing import Any

import numpy as np
from datasets import load_dataset
from rank_bm25 import BM25Okapi
from tqdm import tqdm


def tokenize(text: str) -> list[str]:
    """Simple tokenizer for BM25."""

    return re.findall(r"[A-Za-z0-9]+", text.lower())


def minmax_normalize(scores: np.ndarray) -> np.ndarray:
    """Normalize one score vector into [0, 1]."""

    min_score = float(np.min(scores))
    max_score = float(np.max(scores))

    if max_score - min_score < 1e-12:
        return np.zeros_like(scores, dtype=np.float32)

    return ((scores - min_score) / (max_score - min_score)).astype(np.float32)


def pick(row: dict[str, Any], names: list[str]) -> Any:
    """Pick the first existing field from a dataset row."""

    for name in names:
        if name in row:
            return row[name]

    raise KeyError(f"None of the fields exist: {names}. Row keys: {list(row.keys())}")


def load_scifact() -> tuple[dict[str, str], dict[str, str], dict[str, dict[str, int]]]:
    """Load BEIR SciFact corpus, queries, and qrels from Hugging Face."""

    corpus_ds = load_dataset("BeIR/scifact", "corpus", split="corpus")
    queries_ds = load_dataset("BeIR/scifact", "queries", split="queries")

    corpus: dict[str, str] = {}
    for row in corpus_ds:
        doc_id = str(pick(row, ["_id", "id"]))
        title = str(row.get("title", "") or "")
        text = str(row.get("text", "") or "")
        corpus[doc_id] = f"{title}\n{text}".strip()

    queries: dict[str, str] = {}
    for row in queries_ds:
        query_id = str(pick(row, ["_id", "id"]))
        text = str(row.get("text", "") or row.get("title", "") or "")
        queries[query_id] = text.strip()

    qrels_ds = None
    for split in ["test", "validation", "train"]:
        try:
            qrels_ds = load_dataset("BeIR/scifact-qrels", split=split)
            break
        except Exception:
            continue

    if qrels_ds is None:
        raise RuntimeError("Could not load BeIR/scifact-qrels from any known split.")

    qrels: dict[str, dict[str, int]] = {}
    for row in qrels_ds:
        query_id = str(pick(row, ["query-id", "query_id", "qid", "query"]))
        doc_id = str(pick(row, ["corpus-id", "corpus_id", "docid", "doc_id"]))
        score = int(row.get("score", row.get("relevance", 1)))

        if score > 0:
            qrels.setdefault(query_id, {})[doc_id] = score

    queries = {qid: q for qid, q in queries.items() if qid in qrels}

    return corpus, queries, qrels


def top_k_indices(scores: np.ndarray, k: int) -> list[int]:
    """Return top-k indices sorted by score descending."""

    k = min(k, len(scores))

    if k <= 0:
        return []

    candidate_idx = np.argpartition(-scores, kth=k - 1)[:k]
    sorted_idx = candidate_idx[np.argsort(-scores[candidate_idx])]

    return sorted_idx.tolist()


def compute_metrics(
    rankings: dict[str, list[str]],
    qrels: dict[str, dict[str, int]],
    ks: list[int],
) -> dict[str, float]:
    """Compute Hit@k, Precision@k, Recall@k, MRR@k, nDCG@k."""

    query_ids = [qid for qid in rankings if qid in qrels and qrels[qid]]

    metrics: dict[str, float] = {}

    for k in ks:
        hit_scores = []
        precision_scores = []
        recall_scores = []
        rr_scores = []
        ndcg_scores = []

        for qid in query_ids:
            ranked_docs = rankings[qid][:k]
            relevant = qrels[qid]
            relevant_doc_ids = set(relevant.keys())

            hits = [doc_id for doc_id in ranked_docs if doc_id in relevant_doc_ids]

            hit_scores.append(1.0 if hits else 0.0)
            precision_scores.append(len(hits) / k)
            recall_scores.append(len(hits) / len(relevant_doc_ids))

            rr = 0.0
            for rank, doc_id in enumerate(ranked_docs, start=1):
                if doc_id in relevant_doc_ids:
                    rr = 1.0 / rank
                    break
            rr_scores.append(rr)

            dcg = 0.0
            for rank, doc_id in enumerate(ranked_docs, start=1):
                rel = relevant.get(doc_id, 0)
                gain = (2**rel - 1) / math.log2(rank + 1)
                dcg += gain

            ideal_rels = sorted(relevant.values(), reverse=True)[:k]
            idcg = 0.0
            for rank, rel in enumerate(ideal_rels, start=1):
                idcg += (2**rel - 1) / math.log2(rank + 1)

            ndcg_scores.append(dcg / idcg if idcg > 0 else 0.0)

        metrics[f"hit@{k}"] = float(np.mean(hit_scores)) if hit_scores else 0.0
        metrics[f"precision@{k}"] = float(np.mean(precision_scores)) if precision_scores else 0.0
        metrics[f"recall@{k}"] = float(np.mean(recall_scores)) if recall_scores else 0.0
        metrics[f"mrr@{k}"] = float(np.mean(rr_scores)) if rr_scores else 0.0
        metrics[f"ndcg@{k}"] = float(np.mean(ndcg_scores)) if ndcg_scores else 0.0

    metrics["num_queries"] = float(len(query_ids))

    return metrics


def build_bm25(corpus_texts: list[str]) -> BM25Okapi:
    """Build BM25 index."""

    tokenized_corpus = [tokenize(text) for text in tqdm(corpus_texts, desc="Tokenizing corpus")]
    return BM25Okapi(tokenized_corpus)


def rank_bm25(
    bm25: BM25Okapi,
    queries: dict[str, str],
    doc_ids: list[str],
    top_k: int,
) -> dict[str, list[str]]:
    """Retrieve documents with BM25."""

    rankings: dict[str, list[str]] = {}

    for qid, query in tqdm(queries.items(), desc="BM25 retrieval"):
        scores = np.asarray(bm25.get_scores(tokenize(query)), dtype=np.float32)
        top_idx = top_k_indices(scores, top_k)
        rankings[qid] = [doc_ids[i] for i in top_idx]

    return rankings


def encode_dense(
    corpus_texts: list[str],
    queries: dict[str, str],
    model_name: str,
) -> tuple[np.ndarray, np.ndarray, list[str]]:
    """Encode corpus and queries with a sentence-transformer model."""

    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(model_name)

    corpus_emb = model.encode(
        corpus_texts,
        batch_size=64,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    query_ids = list(queries.keys())
    query_texts = [queries[qid] for qid in query_ids]

    query_emb = model.encode(
        query_texts,
        batch_size=64,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    return np.asarray(corpus_emb), np.asarray(query_emb), query_ids


def rank_dense(
    corpus_emb: np.ndarray,
    query_emb: np.ndarray,
    query_ids: list[str],
    doc_ids: list[str],
    top_k: int,
) -> dict[str, list[str]]:
    """Retrieve documents with dense dot-product similarity."""

    rankings: dict[str, list[str]] = {}

    scores_matrix = query_emb @ corpus_emb.T

    for row_idx, qid in enumerate(tqdm(query_ids, desc="Dense retrieval")):
        scores = scores_matrix[row_idx]
        top_idx = top_k_indices(scores, top_k)
        rankings[qid] = [doc_ids[i] for i in top_idx]

    return rankings


def rank_hybrid(
    bm25: BM25Okapi,
    corpus_emb: np.ndarray,
    query_emb: np.ndarray,
    query_ids: list[str],
    queries: dict[str, str],
    doc_ids: list[str],
    top_k: int,
    alpha: float,
) -> dict[str, list[str]]:
    """Hybrid retrieval by min-max normalized dense + BM25 scores."""

    rankings: dict[str, list[str]] = {}

    dense_scores_matrix = query_emb @ corpus_emb.T

    for row_idx, qid in enumerate(tqdm(query_ids, desc="Hybrid retrieval")):
        query = queries[qid]

        bm25_scores = np.asarray(bm25.get_scores(tokenize(query)), dtype=np.float32)
        dense_scores = dense_scores_matrix[row_idx].astype(np.float32)

        bm25_norm = minmax_normalize(bm25_scores)
        dense_norm = minmax_normalize(dense_scores)

        scores = alpha * dense_norm + (1.0 - alpha) * bm25_norm

        top_idx = top_k_indices(scores, top_k)
        rankings[qid] = [doc_ids[i] for i in top_idx]

    return rankings


def rerank_with_cross_encoder(
    initial_rankings: dict[str, list[str]],
    queries: dict[str, str],
    corpus: dict[str, str],
    reranker_model_name: str,
    top_k: int,
) -> dict[str, list[str]]:
    """Rerank initial candidates with a cross-encoder."""

    from sentence_transformers import CrossEncoder

    reranker = CrossEncoder(reranker_model_name)

    reranked: dict[str, list[str]] = {}

    for qid, candidate_doc_ids in tqdm(initial_rankings.items(), desc="Cross-encoder reranking"):
        query = queries[qid]
        pairs = [(query, corpus[doc_id]) for doc_id in candidate_doc_ids]

        if not pairs:
            reranked[qid] = []
            continue

        scores = reranker.predict(pairs)
        scores = np.asarray(scores, dtype=np.float32)

        order = np.argsort(-scores)[:top_k]
        reranked[qid] = [candidate_doc_ids[i] for i in order]

    return reranked


def save_outputs(
    output_dir: Path,
    mode: str,
    metrics: dict[str, float],
    rankings: dict[str, list[str]],
    args: argparse.Namespace,
) -> None:
    """Save metrics and rankings."""

    output_dir.mkdir(parents=True, exist_ok=True)

    metrics_path = output_dir / f"scifact_{mode}_metrics.json"
    rankings_path = output_dir / f"scifact_{mode}_rankings.json"

    payload = {
        "mode": mode,
        "args": vars(args),
        "metrics": metrics,
    }

    metrics_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    rankings_path.write_text(
        json.dumps(rankings, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"\nSaved metrics to: {metrics_path}")
    print(f"Saved rankings to: {rankings_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--mode",
        choices=["bm25", "dense", "hybrid", "hybrid_rerank"],
        default="bm25",
    )
    parser.add_argument(
        "--dense_model",
        default="BAAI/bge-small-en-v1.5",
        help="SentenceTransformer model for dense retrieval.",
    )
    parser.add_argument(
        "--reranker_model",
        default="cross-encoder/ms-marco-MiniLM-L-6-v2",
        help="CrossEncoder model for reranking.",
    )
    parser.add_argument("--top_k", type=int, default=10)
    parser.add_argument("--rerank_top_n", type=int, default=50)
    parser.add_argument("--alpha", type=float, default=0.6)
    parser.add_argument("--limit_queries", type=int, default=0)
    parser.add_argument("--output_dir", default="eval/results")

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print("Loading SciFact...")
    corpus, queries, qrels = load_scifact()

    if args.limit_queries and args.limit_queries > 0:
        limited_qids = list(queries.keys())[: args.limit_queries]
        queries = {qid: queries[qid] for qid in limited_qids}
        qrels = {qid: qrels[qid] for qid in limited_qids if qid in qrels}

    doc_ids = list(corpus.keys())
    corpus_texts = [corpus[doc_id] for doc_id in doc_ids]

    print(f"Corpus size: {len(corpus)}")
    print(f"Query size: {len(queries)}")
    print(f"Qrels size: {len(qrels)}")

    retrieval_top_k = max(args.top_k, args.rerank_top_n)

    bm25 = None
    corpus_emb = None
    query_emb = None
    query_ids = None

    if args.mode in ["bm25", "hybrid", "hybrid_rerank"]:
        bm25 = build_bm25(corpus_texts)

    if args.mode in ["dense", "hybrid", "hybrid_rerank"]:
        corpus_emb, query_emb, query_ids = encode_dense(
            corpus_texts=corpus_texts,
            queries=queries,
            model_name=args.dense_model,
        )

    if args.mode == "bm25":
        assert bm25 is not None
        rankings = rank_bm25(
            bm25=bm25,
            queries=queries,
            doc_ids=doc_ids,
            top_k=args.top_k,
        )

    elif args.mode == "dense":
        assert corpus_emb is not None
        assert query_emb is not None
        assert query_ids is not None
        rankings = rank_dense(
            corpus_emb=corpus_emb,
            query_emb=query_emb,
            query_ids=query_ids,
            doc_ids=doc_ids,
            top_k=args.top_k,
        )

    elif args.mode == "hybrid":
        assert bm25 is not None
        assert corpus_emb is not None
        assert query_emb is not None
        assert query_ids is not None
        rankings = rank_hybrid(
            bm25=bm25,
            corpus_emb=corpus_emb,
            query_emb=query_emb,
            query_ids=query_ids,
            queries=queries,
            doc_ids=doc_ids,
            top_k=args.top_k,
            alpha=args.alpha,
        )

    elif args.mode == "hybrid_rerank":
        assert bm25 is not None
        assert corpus_emb is not None
        assert query_emb is not None
        assert query_ids is not None

        initial_rankings = rank_hybrid(
            bm25=bm25,
            corpus_emb=corpus_emb,
            query_emb=query_emb,
            query_ids=query_ids,
            queries=queries,
            doc_ids=doc_ids,
            top_k=retrieval_top_k,
            alpha=args.alpha,
        )

        rankings = rerank_with_cross_encoder(
            initial_rankings=initial_rankings,
            queries=queries,
            corpus=corpus,
            reranker_model_name=args.reranker_model,
            top_k=args.top_k,
        )

    else:
        raise ValueError(f"Unsupported mode: {args.mode}")

    metrics = compute_metrics(
        rankings=rankings,
        qrels=qrels,
        ks=[1, 3, 5, 10],
    )

    print("\nMetrics:")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")

    save_outputs(
        output_dir=Path(args.output_dir),
        mode=args.mode,
        metrics=metrics,
        rankings=rankings,
        args=args,
    )


if __name__ == "__main__":
    main()

