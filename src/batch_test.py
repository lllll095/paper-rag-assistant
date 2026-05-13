from pathlib import Path
from rag_qa import answer_question


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "batch_answers.md"


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


def main():
    lines = []

    for i, question in enumerate(QUESTIONS, start=1):
        print("=" * 80)
        print(f"Question {i}: {question}")

        answer, docs = answer_question(question)

        lines.append(f"# Question {i}\n")
        lines.append(f"**Question:** {question}\n\n")
        lines.append("## Answer\n\n")
        lines.append(answer)
        lines.append("\n\n## Retrieved Sources\n\n")

        for j, doc in enumerate(docs, start=1):
            source = doc.metadata.get("source", "unknown")
            page = doc.metadata.get("page", "unknown")
            chunk_id = doc.metadata.get("chunk_id", "unknown")
            lines.append(f"- [Source {j}] {source}, page {page}, chunk {chunk_id}\n")

        lines.append("\n\n---\n\n")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("".join(lines), encoding="utf-8")

    print("=" * 80)
    print(f"Batch test finished. Results saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()