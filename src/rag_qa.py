import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = PROJECT_ROOT / ".env"

CHROMA_DIR = PROJECT_ROOT / "chroma_db"
COLLECTION_NAME = "paper_rag_week1"

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

load_dotenv(dotenv_path=ENV_PATH)


class PaperRAG:
    def __init__(self):
        self.client, self.model = self._load_llm_client()
        self.vectorstore = self._load_vectorstore()

    def _load_llm_client(self):
        api_key = os.getenv("DASHSCOPE_API_KEY")
        base_url = os.getenv("LLM_BASE_URL")
        model = os.getenv("LLM_MODEL", "qwen-plus")

        if not api_key:
            raise ValueError("DASHSCOPE_API_KEY is not set. Please check your .env file.")

        if not base_url:
            raise ValueError("LLM_BASE_URL is not set. Please check your .env file.")

        client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )

        return client, model

    def _load_vectorstore(self):
        print("Loading embedding model and Chroma vectorstore...")

        embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            encode_kwargs={"normalize_embeddings": True},
        )

        vectorstore = Chroma(
            persist_directory=str(CHROMA_DIR),
            embedding_function=embeddings,
            collection_name=COLLECTION_NAME,
        )

        print("Vectorstore loaded.")

        return vectorstore

    def retrieve(self, query, k=5):
        docs = self.vectorstore.similarity_search(query, k=k)
        return docs

    @staticmethod
    def format_context(docs):
        context_blocks = []

        for i, doc in enumerate(docs, start=1):
            source = doc.metadata.get("source", "unknown")
            page = doc.metadata.get("page", "unknown")
            chunk_id = doc.metadata.get("chunk_id", "unknown")

            block = f"""
[Source {i}]
File: {source}
Page: {page}
Chunk ID: {chunk_id}

Content:
{doc.page_content}
"""
            context_blocks.append(block)

        return "\n\n".join(context_blocks)

    def answer_question(self, question, k=5):
        docs = self.retrieve(question, k=k)
        context = self.format_context(docs)

        prompt = f"""
You are a research assistant helping a statistics PhD student read scientific papers.

Answer the question using only the provided context.

If the context is insufficient, say:
"The provided context is insufficient."

Question:
{question}

Context:
{context}

Please provide your answer in the following format:

Answer:
A concise answer to the question.

Explanation:
A short explanation grounded in the retrieved context.

Sources:
List the source numbers you used, such as [Source 1], [Source 3].
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a careful research assistant. You must answer only based on the provided context.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.2,
        )

        answer = response.choices[0].message.content

        return answer, docs


_rag_engine = None


def get_rag_engine():
    global _rag_engine

    if _rag_engine is None:
        _rag_engine = PaperRAG()

    return _rag_engine


def answer_question(question, k=5):
    rag_engine = get_rag_engine()
    return rag_engine.answer_question(question, k=k)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        question = "What is the main contribution of AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees? Please answer based on the abstract and introduction."
    else:
        question = " ".join(sys.argv[1:])

    answer, docs = answer_question(question)

    print("=" * 80)
    print("Question:")
    print(question)

    print("=" * 80)
    print("Answer:")
    print(answer)

    print("=" * 80)
    print("Retrieved Sources:")
    for i, doc in enumerate(docs, start=1):
        print(
            f"[Source {i}] "
            f"{doc.metadata.get('source')}, "
            f"page {doc.metadata.get('page')}, "
            f"chunk {doc.metadata.get('chunk_id')}"
        )