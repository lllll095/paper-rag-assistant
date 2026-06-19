import json
from pathlib import Path


RESULT_DIR = Path("eval/results")

FILES = {
    "BM25": "scifact_bm25_metrics.json",
    "Dense": "scifact_dense_metrics.json",
    "Hybrid": "scifact_hybrid_metrics.json",
    "Hybrid + Reranker": "scifact_hybrid_rerank_metrics.json",
    "Project EngineeredRAG": "scifact_project_retriever_paperk50_chunkk10_metrics.json",
}


def load_metrics(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload["metrics"]


def main() -> None:
    rows = []

    for method, filename in FILES.items():
        path = RESULT_DIR / filename

        if not path.exists():
            print(f"[WARN] Missing file: {path}")
            continue

        metrics = load_metrics(path)

        rows.append(
            {
                "method": method,
                "hit@10": metrics.get("hit@10", 0.0),
                "precision@10": metrics.get("precision@10", 0.0),
                "recall@10": metrics.get("recall@10", 0.0),
                "mrr@10": metrics.get("mrr@10", 0.0),
                "ndcg@10": metrics.get("ndcg@10", 0.0),
            }
        )

    if not rows:
        print("No metrics found.")
        return

    print("\nSciFact Retrieval Evaluation Summary\n")

    header = "| Method | Hit@10 | Precision@10 | Recall@10 | MRR@10 | nDCG@10 |"
    sep = "|---|---:|---:|---:|---:|---:|"

    print(header)
    print(sep)

    for row in rows:
        print(
            f"| {row['method']} "
            f"| {row['hit@10']:.4f} "
            f"| {row['precision@10']:.4f} "
            f"| {row['recall@10']:.4f} "
            f"| {row['mrr@10']:.4f} "
            f"| {row['ndcg@10']:.4f} |"
        )


if __name__ == "__main__":
    main()