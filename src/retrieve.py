from pathlib import Path
import sys

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


PROJECT_ROOT = Path(__file__).resolve().parents[1]

CHROMA_DIR = PROJECT_ROOT / "chroma_db"
COLLECTION_NAME = "paper_rag_week1"

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"


def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        encode_kwargs={"normalize_embeddings": True},
    )

    vectorstore = Chroma(
        persist_directory=str(CHROMA_DIR),
        embedding_function=embeddings,
        collection_name=COLLECTION_NAME,
    )

    return vectorstore


def retrieve(query, k=5):
    vectorstore = load_vectorstore()
    docs = vectorstore.similarity_search(query, k=k)
    return docs


if __name__ == "__main__":
    if len(sys.argv) < 2:
        query = "What is the main contribution of this paper?"
    else:
        query = " ".join(sys.argv[1:])

    results = retrieve(query, k=5)

    print("=" * 80)
    print(f"Query: {query}")
    print("=" * 80)

    for i, doc in enumerate(results, start=1):
        print(f"Top {i}")
        print(f"Source: {doc.metadata.get('source')}")
        print(f"Page: {doc.metadata.get('page')}")
        print(f"Chunk ID: {doc.metadata.get('chunk_id')}")
        print("-" * 80)
        print(doc.page_content[:1200])
        print("=" * 80)