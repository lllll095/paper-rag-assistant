from pathlib import Path

from rag_qa import get_rag_engine


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "retrieval_eval.md"


QUESTIONS = [
    "What is the main contribution of this paper?",
    "What problem does this paper study?",
    "What are the key assumptions?",
    "What are the limitations of the method?",
    "What experiments are conducted in this paper?",
    "What baselines are compared in this paper?",
    "What evaluation metrics are used?",
    "What is the proposed algorithm?",
    "What are the main theoretical results?",
    "What future work is mentioned?",
]


def truncate_text(text: str, max_chars: int = 900) -> str:
    text = " ".join(text.split())
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "..."


def main():
    rag_engine = get_rag_engine()

    lines = []
    lines.append("# Retrieval Evaluation\n\n")
    lines.append(
        "This file is used for manually evaluating retrieval quality. "
        "For each question, inspect whether the retrieved chunks contain information "
        "that can answer the question.\n\n"
    )

    lines.append("## Grading Rubric\n\n")
    lines.append("- **Good**: Top 1--3 chunks are clearly relevant and sufficient.\n")
    lines.append("- **Medium**: Some relevant chunks are retrieved, but important context is missing or mixed with noise.\n")
    lines.append("- **Bad**: Retrieved chunks are mostly irrelevant.\n\n")
    lines.append("---\n\n")

    for i, question in enumerate(QUESTIONS, start=1):
        print("=" * 80)
        print(f"Evaluating Question {i}: {question}")

        docs = rag_engine.retrieve(question, k=5)

        lines.append(f"# Question {i}\n\n")
        lines.append(f"**Question:** {question}\n\n")
        lines.append("**Manual Grade:** Good / Medium / Bad\n\n")
        lines.append("**Notes:** \n\n")

        lines.append("## Retrieved Chunks\n\n")

        for j, doc in enumerate(docs, start=1):
            source = doc.metadata.get("source", "unknown")
            page = doc.metadata.get("page", "unknown")
            chunk_id = doc.metadata.get("chunk_id", "unknown")
            snippet = truncate_text(doc.page_content)

            lines.append(f"### Top {j}\n\n")
            lines.append(f"- Source: `{source}`\n")
            lines.append(f"- Page: `{page}`\n")
            lines.append(f"- Chunk ID: `{chunk_id}`\n\n")
            lines.append("```text\n")
            lines.append(snippet)
            lines.append("\n```\n\n")

        lines.append("---\n\n")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("".join(lines), encoding="utf-8")

    print("=" * 80)
    print(f"Retrieval evaluation file saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()