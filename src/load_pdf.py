from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

PAPER_DIR = Path("data") / "papers"

def load_all_pdfs():
    pdf_files = list(PAPER_DIR.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError("No PDF files found in data/papers/")

    all_docs = []

    for pdf_path in pdf_files:
        loader = PyPDFLoader(str(pdf_path))
        docs = loader.load()

        print("=" * 80)
        print(f"File: {pdf_path.name}")
        print(f"Number of pages: {len(docs)}")
        print("Preview:")
        print(docs[0].page_content[:500])

        all_docs.extend(docs)

    return all_docs

if __name__ == "__main__":
    docs = load_all_pdfs()
    print("=" * 80)
    print(f"Total loaded pages: {len(docs)}")