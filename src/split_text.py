from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

PAPER_DIR = Path("data") / "papers"

def load_all_pdfs():
    all_docs = []

    for pdf_path in PAPER_DIR.glob("*.pdf"):
        loader = PyPDFLoader(str(pdf_path))
        docs = loader.load()

        for doc in docs:
            doc.metadata["source"] = pdf_path.name

        all_docs.extend(docs)

    if not all_docs:
        raise FileNotFoundError("No PDF files found in data/papers/")

    return all_docs

def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    chunks = splitter.split_documents(docs)

    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = i

    return chunks

if __name__ == "__main__":
    docs = load_all_pdfs()
    chunks = split_documents(docs)

    print(f"Number of PDF pages: {len(docs)}")
    print(f"Number of chunks: {len(chunks)}")
    print("=" * 80)

    for chunk in chunks[:3]:
        print(f"Source: {chunk.metadata.get('source')}")
        print(f"Page: {chunk.metadata.get('page')}")
        print(f"Chunk ID: {chunk.metadata.get('chunk_id')}")
        print(chunk.page_content[:800])
        print("=" * 80)