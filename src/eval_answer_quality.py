import json
import re
import sys
from pathlib import Path


CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from rag_engineered import EngineeredRAG


EVAL_DATA_PATH = PROJECT_ROOT / "data" / "answer_eval_questions.json"
OUTPUT_MD_PATH = PROJECT_ROOT / "outputs" / "answer_eval_report.md"
OUTPUT_JSONL_PATH = PROJECT_ROOT / "outputs" / "answer_eval_results.jsonl"


def load_eval_questions():
    if not EVAL_DATA_PATH.exists():
        raise FileNotFoundError(
            f"Evaluation file not found: {EVAL_DATA_PATH}\n"
            "Please create data/answer_eval_questions.json first."
        )

    with open(EVAL_DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("answer_eval_questions.json must contain a list of questions.")

    return data


def format_context_for_judge(docs, max_chars_per_doc=1200):
    blocks = []

    for i, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "unknown")
        page = doc.metadata.get("page", "unknown")
        chunk_id = doc.metadata.get("chunk_id", "unknown")
        chunk_type = doc.metadata.get("chunk_type", "unknown")
        vector_score = doc.metadata.get("vector_score", "unknown")
        bm25_score = doc.metadata.get("bm25_score", "unknown")
        reranker_score = doc.metadata.get("reranker_score", "unknown")

        content = doc.page_content[:max_chars_per_doc]

        block = f"""
[Source {i}]
File: {source}
Page: {page}
Chunk ID: {chunk_id}
Chunk Type: {chunk_type}
Vector Score: {vector_score}
BM25 Score: {bm25_score}
Reranker Score: {reranker_score}

Content:
{content}
"""
        blocks.append(block)

    return "\n\n".join(blocks)


def extract_cited_sources(answer):
    """
    Extract source references like [Source 1], [Source 2].
    """
    pattern = r"\[Source\s+(\d+)\]"
    matches = re.findall(pattern, answer)

    cited = sorted({int(m) for m in matches})

    return cited


def basic_citation_check(answer, docs):
    cited = extract_cited_sources(answer)
    valid_range = set(range(1, len(docs) + 1))

    invalid = [idx for idx in cited if idx not in valid_range]

    if not cited:
        return {
            "has_citation": False,
            "invalid_citations": invalid,
            "citation_check": "No explicit source citation found.",
        }

    if invalid:
        return {
            "has_citation": True,
            "invalid_citations": invalid,
            "citation_check": f"Invalid source citation(s): {invalid}",
        }

    return {
        "has_citation": True,
        "invalid_citations": [],
        "citation_check": "Pass",
    }


def safe_parse_json(text):
    """
    Parse a JSON object from an LLM response.
    """
    text = text.strip()

    try:
        return json.loads(text)
    except Exception:
        pass

    match = re.search(r"\{.*\}", text, flags=re.DOTALL)

    if match:
        try:
            return json.loads(match.group(0))
        except Exception:
            pass

    return {
        "answer_relevance": 0,
        "groundedness": 0,
        "citation_support": 0,
        "completeness": 0,
        "insufficient_context_handling": 0,
        "hallucination_risk": "unknown",
        "overall_score": 0,
        "verdict": "parse_failed",
        "comments": f"Failed to parse judge output: {text[:500]}",
    }


def judge_answer_with_llm(rag, question, expected_behavior, answer, docs):
    context = format_context_for_judge(docs)

    judge_prompt = f"""
You are evaluating a RAG answer for an academic paper QA system.

Your job is to judge whether the answer is supported by the retrieved context.

Question:
{question}

Expected behavior:
{expected_behavior}

Retrieved context:
{context}

Answer to evaluate:
{answer}

Evaluate the answer using the following criteria:

1. answer_relevance:
   Does the answer address the user's question?

2. groundedness:
   Are the claims in the answer supported by the retrieved context?

3. citation_support:
   Do the cited sources actually support the claims?

4. completeness:
   Is the answer sufficiently complete given the available context?

5. insufficient_context_handling:
   If the context is insufficient, did the answer say so instead of hallucinating?
   If the context is sufficient and the answer uses it properly, give a high score.

6. hallucination_risk:
   Estimate the risk of unsupported claims: low / medium / high.

Return only a valid JSON object with this schema:

{{
  "answer_relevance": 0,
  "groundedness": 0,
  "citation_support": 0,
  "completeness": 0,
  "insufficient_context_handling": 0,
  "hallucination_risk": "low",
  "overall_score": 0,
  "verdict": "good / medium / poor",
  "comments": "brief explanation"
}}

Use integer scores from 1 to 5 for the first five metrics.
Use overall_score from 1 to 10.
"""

    response = rag.client.chat.completions.create(
        model=rag.model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a strict evaluator for retrieval-augmented generation. "
                    "You must judge only based on the retrieved context."
                ),
            },
            {
                "role": "user",
                "content": judge_prompt,
            },
        ],
        temperature=0.0,
    )

    raw = response.choices[0].message.content

    return safe_parse_json(raw)


def format_retrieved_sources(docs):
    lines = []

    for i, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "unknown")
        page = doc.metadata.get("page", "unknown")
        chunk_id = doc.metadata.get("chunk_id", "unknown")
        chunk_type = doc.metadata.get("chunk_type", "unknown")
        vector_score = doc.metadata.get("vector_score", "unknown")
        bm25_score = doc.metadata.get("bm25_score", "unknown")
        reranker_score = doc.metadata.get("reranker_score", "unknown")

        lines.append(
            f"{i}. `{source}`, page `{page}`, chunk `{chunk_id}`, "
            f"type `{chunk_type}`, vector `{vector_score}`, "
            f"bm25 `{bm25_score}`, reranker `{reranker_score}`"
        )

    return "\n".join(lines)


def write_case_report(f, result):
    item = result["item"]
    question = item["question"]

    f.write(f"## {item.get('id', 'unknown')}: {question}\n\n")

    f.write("### Question Metadata\n\n")
    f.write(f"- Question type: `{item.get('question_type', 'unknown')}`\n")
    f.write(f"- Expected behavior: {item.get('expected_behavior', '')}\n\n")

    f.write("### Retrieval Info\n\n")
    retrieval_info = result["retrieval_info"]

    f.write(f"- Final retrieval mode: `{retrieval_info.get('mode', 'unknown')}`\n")

    query_route = retrieval_info.get("query_route")
    if query_route:
        f.write(f"- Query route: `{query_route}`\n")

    f.write("\n### Retrieved Sources\n\n")
    f.write(format_retrieved_sources(result["docs"]))
    f.write("\n\n")

    f.write("### Answer\n\n")
    f.write("```text\n")
    f.write(result["answer"])
    f.write("\n```\n\n")

    f.write("### Basic Citation Check\n\n")
    citation_check = result["citation_check"]

    f.write(f"- Has citation: `{citation_check['has_citation']}`\n")
    f.write(f"- Invalid citations: `{citation_check['invalid_citations']}`\n")
    f.write(f"- Citation check: {citation_check['citation_check']}\n\n")

    f.write("### LLM Judge Scores\n\n")
    judge = result["judge"]

    f.write(f"- Answer relevance: `{judge.get('answer_relevance')}/5`\n")
    f.write(f"- Groundedness: `{judge.get('groundedness')}/5`\n")
    f.write(f"- Citation support: `{judge.get('citation_support')}/5`\n")
    f.write(f"- Completeness: `{judge.get('completeness')}/5`\n")
    f.write(
        f"- Insufficient context handling: "
        f"`{judge.get('insufficient_context_handling')}/5`\n"
    )
    f.write(f"- Hallucination risk: `{judge.get('hallucination_risk')}`\n")
    f.write(f"- Overall score: `{judge.get('overall_score')}/10`\n")
    f.write(f"- Verdict: `{judge.get('verdict')}`\n")
    f.write(f"- Comments: {judge.get('comments')}\n\n")

    f.write("### Manual Notes\n\n")
    f.write("- Is the answer actually useful?\n")
    f.write("- Are the sources sufficient?\n")
    f.write("- Are there unsupported claims?\n")
    f.write("- Should the answer be more concise or more detailed?\n\n")

    f.write("---\n\n")


def main():
    eval_items = load_eval_questions()
    rag = EngineeredRAG()

    OUTPUT_MD_PATH.parent.mkdir(exist_ok=True)

    all_results = []

    with open(OUTPUT_JSONL_PATH, "w", encoding="utf-8") as jsonl_file:
        for item in eval_items:
            question = item["question"]
            expected_behavior = item.get("expected_behavior", "")

            print("=" * 80)
            print(f"Evaluating: {item.get('id', 'unknown')}")
            print(question)

            answer, docs, retrieval_info = rag.answer_question(
                question=question,
                show_debug=False,
            )

            citation_check = basic_citation_check(answer, docs)

            judge = judge_answer_with_llm(
                rag=rag,
                question=question,
                expected_behavior=expected_behavior,
                answer=answer,
                docs=docs,
            )

            result = {
                "item": item,
                "answer": answer,
                "docs": docs,
                "retrieval_info": retrieval_info,
                "citation_check": citation_check,
                "judge": judge,
            }

            all_results.append(result)

            jsonl_record = {
                "id": item.get("id"),
                "question": question,
                "question_type": item.get("question_type"),
                "expected_behavior": expected_behavior,
                "answer": answer,
                "retrieval_mode": retrieval_info.get("mode"),
                "query_route": retrieval_info.get("query_route"),
                "citation_check": citation_check,
                "judge": judge,
                "sources": [
                    {
                        "source": doc.metadata.get("source", "unknown"),
                        "page": doc.metadata.get("page", "unknown"),
                        "chunk_id": doc.metadata.get("chunk_id", "unknown"),
                        "chunk_type": doc.metadata.get("chunk_type", "unknown"),
                        "vector_score": doc.metadata.get("vector_score", "unknown"),
                        "bm25_score": doc.metadata.get("bm25_score", "unknown"),
                        "reranker_score": doc.metadata.get("reranker_score", "unknown"),
                    }
                    for doc in docs
                ],
            }

            jsonl_file.write(json.dumps(jsonl_record, ensure_ascii=False) + "\n")

    with open(OUTPUT_MD_PATH, "w", encoding="utf-8") as f:
        f.write("# Answer-level Evaluation Report\n\n")
        f.write("This report evaluates the final answers produced by the engineered RAG system.\n\n")
        f.write("It checks answer relevance, groundedness, citation support, completeness, and hallucination risk.\n\n")
        f.write("---\n\n")

        for result in all_results:
            write_case_report(f, result)

        f.write("# Overall Summary\n\n")

        if all_results:
            avg_overall = sum(
                float(r["judge"].get("overall_score", 0))
                for r in all_results
            ) / len(all_results)

            avg_groundedness = sum(
                float(r["judge"].get("groundedness", 0))
                for r in all_results
            ) / len(all_results)

            avg_relevance = sum(
                float(r["judge"].get("answer_relevance", 0))
                for r in all_results
            ) / len(all_results)

            high_risk = sum(
                1
                for r in all_results
                if str(r["judge"].get("hallucination_risk", "")).lower() == "high"
            )

            no_citation = sum(
                1
                for r in all_results
                if not r["citation_check"]["has_citation"]
            )

            f.write(f"- Number of evaluated questions: `{len(all_results)}`\n")
            f.write(f"- Average overall score: `{avg_overall:.2f}/10`\n")
            f.write(f"- Average groundedness: `{avg_groundedness:.2f}/5`\n")
            f.write(f"- Average answer relevance: `{avg_relevance:.2f}/5`\n")
            f.write(f"- High hallucination risk cases: `{high_risk}`\n")
            f.write(f"- No-citation cases: `{no_citation}`\n\n")

        f.write("## Interpretation\n\n")
        f.write("- If relevance is low, improve query routing or retrieval coverage.\n")
        f.write("- If groundedness is low, improve reranking and context filtering.\n")
        f.write("- If citation support is low, improve the answer prompt and citation format.\n")
        f.write("- If completeness is low, increase chunk_k or improve paper catalog.\n")
        f.write("- If hallucination risk is high, make the answer prompt more conservative.\n")

    print("=" * 80)
    print(f"Answer-level evaluation report saved to: {OUTPUT_MD_PATH}")
    print(f"JSONL results saved to: {OUTPUT_JSONL_PATH}")
    print("=" * 80)


if __name__ == "__main__":
    main()