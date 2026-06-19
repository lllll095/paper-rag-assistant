
"""
Evaluate Paper RAG Assistant's real EngineeredRAG retriever on SciFact.

This script uses the SciFact Chroma indexes built by:

python scripts/build_scifact_project_index.py

It does NOT reimplement retrieval internally. Instead, it calls the real
EngineeredRAG.retrieve() pipeline.

Evaluation chain:

SciFact queries
  -> EngineeredRAG.retrieve()
  -> retrieved docs metadata["source"]
  -> compare with SciFact qrels
  -> Hit@k / Precision@k / Recall@k / MRR@k / nDCG@k

Example:

python scripts/eval_project_retriever_scifact.py --limit_queries 20 --top_k 10
python scripts/eval_project_retriever_scifact.py --top_k 10 --paper_k 50 --chunk_k 10
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from tqdm import tqdm


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


from eval_beir_scifact import compute_metrics, load_scifact  # noqa: E402


DEFAULT_CHUNK_DB_DIR = PROJECT_ROOT / "eval" / "scifact_project_index" / "chunk_db"
DEFAULT_CATALOG_DB_DIR = PROJECT_ROOT / "eval" / "scifact_project_index" / "paper_catalog_db"


def patch_module_paths(module: Any, chunk_db_dir: Path, catalog_db_dir: Path) -> dict[str, str]:
    """Patch common module-level index path constants.

    This avoids modifying the main project code immediately.
    If your EngineeredRAG already supports constructor path arguments later,
    this monkey patch can be replaced by explicit arguments.
    """

    patched: dict[str, str] = {}

    chunk_attr_candidates = [
        "CHUNK_DB_DIR",
        "CHROMA_DIR",
        "VECTORSTORE_DIR",
    ]

    catalog_attr_candidates = [
        "PAPER_CATALOG_DB_DIR",
        "PAPER_CATALOG_DIR",
        "CATALOG_DB_DIR",
        "PAPER_DB_DIR",
    ]

    for attr in chunk_attr_candidates:
        if hasattr(module, attr):
            setattr(module, attr, chunk_db_dir)
            patched[attr] = str(chunk_db_dir)

    for attr in catalog_attr_candidates:
        if hasattr(module, attr):
            setattr(module, attr, catalog_db_dir)
            patched[attr] = str(catalog_db_dir)

    return patched


def build_project_rag(chunk_db_dir: Path, catalog_db_dir: Path):
    """Build EngineeredRAG with SciFact-compatible index paths."""

    import rag_engineered  # noqa: WPS433

    patched = {
        "rag_engineered": patch_module_paths(
            rag_engineered,
            chunk_db_dir=chunk_db_dir,
            catalog_db_dir=catalog_db_dir,
        )
    }

    # BM25ChunkRetriever may also contain its own module-level Chroma path.
    try:
        import bm25_retriever  # noqa: WPS433

        patched["bm25_retriever"] = patch_module_paths(
            bm25_retriever,
            chunk_db_dir=chunk_db_dir,
            catalog_db_dir=catalog_db_dir,
        )
    except Exception as exc:
        patched["bm25_retriever"] = {"warning": f"Could not patch bm25_retriever: {exc}"}

    print("Patched index paths:")
    print(json.dumps(patched, ensure_ascii=False, indent=2))

    return rag_engineered.EngineeredRAG()


def docs_to_ranked_doc_ids(docs: list[Any], top_k: int) -> list[str]:
    """Convert retrieved LangChain Documents into SciFact corpus ids.

    In the SciFact project index, metadata["source"] is set to SciFact doc_id.
    """

    ranked: list[str] = []
    seen: set[str] = set()

    for doc in docs:
        metadata = getattr(doc, "metadata", {}) or {}

        doc_id = (
            metadata.get("source")
            or metadata.get("doc_id")
            or metadata.get("corpus_id")
            or metadata.get("paper_id")
        )

        if doc_id is None:
            continue

        doc_id = str(doc_id)

        if doc_id in seen:
            continue

        ranked.append(doc_id)
        seen.add(doc_id)

        if len(ranked) >= top_k:
            break

    return ranked


def evaluate_project_retriever(
    rag: Any,
    queries: dict[str, str],
    qrels : dict[str, dict[str, int]],
    top_k: int,
    paper_k: int,
    chunk_k: int,
) -> dict[str, list[str]]:
    """Run EngineeredRAG.retrieve() for all queries and collect rankings."""

    rankings: dict[str, list[str]] = {}

    for qid, query in tqdm(queries.items(), desc="Project retriever evaluation"):
        try:
            docs, retrieval_info = rag.retrieve(
                query=query,
                paper_k=paper_k,
                chunk_k=chunk_k,
            )

            ranked_doc_ids = docs_to_ranked_doc_ids(docs, top_k=top_k)
            rankings[qid] = ranked_doc_ids

            if len(rankings) <= 3:
                gold_ids = set(str(x) for x in qrels.get(qid, {}).keys())

                candidate_ids = [
                    str(item.get("source"))
                    for item in retrieval_info.get("candidate_papers", [])
                    if item.get("source") is not None
                ]

                selected_ids = [
                    str(item.get("source"))
                    for item in retrieval_info.get("selected_papers", [])
                    if item.get("source") is not None
                ]

                print("\n" + "=" * 80)
                print(f"DEBUG qid: {qid}")
                print(f"query: {query}")

                print("gold ids:", sorted(gold_ids))
                print(f"num candidate papers: {len(candidate_ids)}")
                print("candidate ids top 20:", candidate_ids[:20])
                print("gold in candidate:", sorted(gold_ids.intersection(candidate_ids)))

                print(f"num selected papers: {len(selected_ids)}")
                print("selected ids:", selected_ids[:20])
                print("gold in selected:", sorted(gold_ids.intersection(selected_ids)))

                print(f"num docs: {len(docs)}")
                print("retrieved ids:", ranked_doc_ids)
                print("gold in retrieved:", sorted(gold_ids.intersection(ranked_doc_ids)))

                print("retrieval_info:")
                print(json.dumps(retrieval_info, ensure_ascii=False, indent=2))

        except Exception as exc:
            print(f"[WARN] Retrieval failed for query {qid}: {type(exc).__name__}: {exc}")
            rankings[qid] = []

    return rankings

def serialize_args(args: argparse.Namespace) -> dict[str, Any]:
        """Convert argparse Namespace into JSON-serializable dict."""

        output = {}

        for key, value in vars(args).items():
            if isinstance(value, Path):
                output[key] = str(value)
            else:
                output[key] = value

        return output

def save_outputs(
    output_dir: Path,
    metrics: dict[str, float],
    rankings: dict[str, list[str]],
    args: argparse.Namespace,
) -> None:
    """Save metrics and rankings."""

    output_dir.mkdir(parents=True, exist_ok=True)

    metrics_path = output_dir / "scifact_project_retriever_metrics.json"
    rankings_path = output_dir / "scifact_project_retriever_rankings.json"

    payload = {
        "mode": "project_engineered_rag",
        "args": serialize_args(args),
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

    parser.add_argument("--top_k", type=int, default=10)
    parser.add_argument("--paper_k", type=int, default=50)
    parser.add_argument("--chunk_k", type=int, default=10)
    parser.add_argument("--limit_queries", type=int, default=0)

    parser.add_argument(
        "--chunk_db_dir",
        type=Path,
        default=DEFAULT_CHUNK_DB_DIR,
    )
    parser.add_argument(
        "--catalog_db_dir",
        type=Path,
        default=DEFAULT_CATALOG_DB_DIR,
    )
    parser.add_argument(
        "--output_dir",
        type=Path,
        default=PROJECT_ROOT / "eval" / "results",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not args.chunk_db_dir.exists():
        raise FileNotFoundError(f"Chunk DB not found: {args.chunk_db_dir}")

    if not args.catalog_db_dir.exists():
        raise FileNotFoundError(f"Paper catalog DB not found: {args.catalog_db_dir}")

    print("Loading SciFact queries and qrels...")
    _, queries, qrels = load_scifact()

    if args.limit_queries and args.limit_queries > 0:
        limited_qids = list(queries.keys())[: args.limit_queries]
        queries = {qid: queries[qid] for qid in limited_qids}
        qrels = {qid: qrels[qid] for qid in limited_qids if qid in qrels}

    print(f"Query size: {len(queries)}")
    print(f"Qrels size: {len(qrels)}")

    print("Building project EngineeredRAG...")
    rag = build_project_rag(
        chunk_db_dir=args.chunk_db_dir,
        catalog_db_dir=args.catalog_db_dir,
    )

    rankings = evaluate_project_retriever(
        rag=rag,
        queries=queries,
        qrels=qrels,
        top_k=args.top_k,
        paper_k=args.paper_k,
        chunk_k=args.chunk_k,
    )

    metrics = compute_metrics(
        rankings=rankings,
        qrels=qrels,
        ks=[1, 3, 5, 10],
    )

    print("\nMetrics:")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")

    save_outputs(
        output_dir=args.output_dir,
        metrics=metrics,
        rankings=rankings,
        args=args,
    )


if __name__ == "__main__":
    main()

