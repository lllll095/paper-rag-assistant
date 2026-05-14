from pathlib import Path

from rag_qa import PaperRAG


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "retrieval_experiment.md"


def format_doc_preview(doc, max_chars=600):
    source = doc.metadata.get("source", "unknown")
    page = doc.metadata.get("page", "unknown")
    chunk_id = doc.metadata.get("chunk_id", "unknown")

    preview = doc.page_content[:max_chars].replace("\n", " ")

    return f"""Source: {source}
Page: {page}
Chunk ID: {chunk_id}
Preview:
{preview}
"""


def run_topk_experiment():
    rag = PaperRAG()

    selected_source = rag.choose_source_interactive()

    print("=" * 80)
    print("Enter a retrieval question.")
    print("Example: What is the main contribution of this paper?")
    print("=" * 80)

    question = input("Question: ").strip()

    if not question:
        question = "What is the main contribution of this paper?"

    retrieval_query = question

    top_k_values = [3, 5, 8, 10]

    OUTPUT_PATH.parent.mkdir(exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("# Week 2 Retrieval Experiment\n\n")

        f.write("## Selected Paper\n\n")
        f.write(f"{selected_source}\n\n")

        f.write("## Question\n\n")
        f.write(f"{question}\n\n")

        f.write("## Retrieval Query\n\n")
        f.write("```text\n")
        f.write(retrieval_query)
        f.write("\n```\n\n")

        for k in top_k_values:
            print("=" * 80)
            print(f"Testing top_k = {k}")
            print("=" * 80)

            docs = rag.retrieve(
                query=retrieval_query,
                k=k,
                source_filter=selected_source,
            )

            f.write(f"## Experiment: top_k = {k}\n\n")

            for i, doc in enumerate(docs, start=1):
                source = doc.metadata.get("source", "unknown")
                page = doc.metadata.get("page", "unknown")
                chunk_id = doc.metadata.get("chunk_id", "unknown")
                preview = doc.page_content[:600].replace("\n", " ")

                print(f"[{i}] {source}, page {page}, chunk {chunk_id}")
                print(preview)
                print("-" * 80)

                f.write(f"### Retrieved Chunk {i}\n\n")
                f.write(f"- Source: `{source}`\n")
                f.write(f"- Page: `{page}`\n")
                f.write(f"- Chunk ID: `{chunk_id}`\n\n")
                f.write("```text\n")
                f.write(preview)
                f.write("\n```\n\n")

            f.write("### Observation\n\n")
            f.write("- Relevant chunks:\n")
            f.write("- Noisy chunks:\n")
            f.write("- Is this top_k setting good? Yes / No\n\n")

    print("=" * 80)
    print(f"Experiment report saved to: {OUTPUT_PATH}")
    print("=" * 80)


if __name__ == "__main__":
    run_topk_experiment()