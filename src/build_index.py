from pathlib import Path
import shutil

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document


PROJECT_ROOT = Path(__file__).resolve().parents[1]

PAPER_DIR = PROJECT_ROOT / "data" / "papers"
CHROMA_DIR = PROJECT_ROOT / "chroma_db"
COLLECTION_NAME = "paper_rag_week1"

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"


def clean_text(text):
    """Make sure every page/chunk content is a normal string."""
    if text is None:
        return ""

    if not isinstance(text, str):
        text = str(text)

    text = text.replace("\x00", " ")
    text = text.replace("\ufeff", " ")
    text = text.strip()

    return text


def clean_metadata(metadata):
    """Chroma only accepts simple metadata types."""
    clean_meta = {}

    for k, v in metadata.items():
        if v is None:
            continue

        if isinstance(v, (str, int, float, bool)):
            clean_meta[k] = v
        else:
            clean_meta[k] = str(v)

    return clean_meta

def infer_chunk_type(text):
    """
    Infer whether a chunk belongs to main paper text or boilerplate sections.
    This is used for retrieval filtering.
    """
    if text is None:
        return "empty"

    lower = text.lower()

    checklist_patterns = [
        "neurips paper checklist",
        "paper checklist",
        "do the main claims made in the abstract and introduction accurately reflect",
        "did you describe the limitations",
        "did you include the code",
        "for all authors",
        "the checklist follows the references",
        "submission checklist",
        "reproducibility checklist",
        "broader impacts",
    ]

    references_patterns = [
        "references",
        "bibliography",
    ]

    appendix_patterns = [
        "appendix",
        "supplementary material",
        "supplemental material",
    ]

    if any(pattern in lower for pattern in checklist_patterns):
        return "checklist"

    # Only mark as references if the chunk starts like a references section.
    stripped = lower.strip()
    if stripped.startswith("references") or stripped.startswith("bibliography"):
        return "references"

    if stripped.startswith("appendix") or stripped.startswith("supplementary material"):
        return "appendix"

    return "main"

def load_all_pdfs():
    all_docs = []

    pdf_files = list(PAPER_DIR.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(f"No PDF files found in {PAPER_DIR}")

    print(f"Found {len(pdf_files)} PDF files.")

    for pdf_path in pdf_files:
        print(f"Loading PDF: {pdf_path.name}")

        loader = PyPDFLoader(str(pdf_path))
        docs = loader.load()

        valid_page_count = 0

        for page_id, doc in enumerate(docs):
            text = clean_text(doc.page_content)

            if text == "":
                print(f"  Empty page skipped: {pdf_path.name}, page {page_id}")
                continue

            metadata = clean_metadata(doc.metadata)
            metadata["source"] = pdf_path.name
            metadata["page"] = metadata.get("page", page_id)

            all_docs.append(
                Document(
                    page_content=text,
                    metadata=metadata,
                )
            )

            valid_page_count += 1

        print(f"  Loaded valid pages: {valid_page_count}")

    return all_docs


def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    chunks = splitter.split_documents(docs)

    clean_chunks = []

    for chunk in chunks:
        text = clean_text(chunk.page_content)

        if text == "":
            continue

        metadata = clean_metadata(chunk.metadata)
        chunk_type = infer_chunk_type(text)

        metadata["chunk_id"] = len(clean_chunks)
        metadata["chunk_type"] = chunk_type

        clean_chunks.append(
            Document(
                page_content=text,
                metadata=metadata,
            )
        )

    return clean_chunks


def check_chunks(chunks):
    print("=" * 80)
    print("Checking chunks before embedding...")
    print(f"Number of chunks: {len(chunks)}")

    if len(chunks) == 0:
        raise ValueError(
            "No valid text chunks were created. "
            "Your PDFs may be scanned/image-based or text extraction failed."
        )

    for i, doc in enumerate(chunks[:3]):
        print("-" * 80)
        print(f"Chunk {i}")
        print("type(doc):", type(doc))
        print("type(page_content):", type(doc.page_content))
        print("metadata:", doc.metadata)
        print("preview:", repr(doc.page_content[:300]))

    for i, doc in enumerate(chunks):
        if not isinstance(doc.page_content, str):
            raise TypeError(
                f"Bad chunk at index {i}: page_content type is {type(doc.page_content)}"
            )

    print("Chunk check passed.")
    print("=" * 80)


def build_index():
    docs = load_all_pdfs()
    chunks = split_documents(docs)
    check_chunks(chunks)

    print("=" * 80)
    print(f"Loaded pages: {len(docs)}")
    print(f"Created chunks: {len(chunks)}")
    print(f"Embedding model: {EMBEDDING_MODEL}")
    print("=" * 80)

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        encode_kwargs={"normalize_embeddings": True},
    )

    # Test embedding first
    print("Testing embedding on first 2 chunks...")
    test_texts = [doc.page_content for doc in chunks[:2]]
    test_vectors = embeddings.embed_documents(test_texts)
    print(f"Embedding test passed. Vector dimension: {len(test_vectors[0])}")

    # Delete old Chroma index
    if CHROMA_DIR.exists():
        print(f"Removing old index: {CHROMA_DIR}")
        shutil.rmtree(CHROMA_DIR)

        print("Building Chroma index...")

    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(CHROMA_DIR),
    )

    batch_size = 32
    skipped_chunks = []

    for start in range(0, len(chunks), batch_size):
        end = min(start + batch_size, len(chunks))
        batch = chunks[start:end]

        print(f"Adding chunks {start} to {end}...")

        try:
            vectorstore.add_documents(batch)

        except Exception as e:
            print("=" * 80)
            print(f"Batch {start} to {end} failed.")
            print("Now checking chunks one by one...")
            print("=" * 80)

            for j, doc in enumerate(batch):
                global_id = start + j

                try:
                    # 先单独测试这个 chunk 能不能 embedding
                    embeddings.embed_documents([doc.page_content])

                    # 如果能 embedding，再加入 Chroma
                    vectorstore.add_documents([doc])

                except Exception as single_e:
                    print("-" * 80)
                    print(f"Skipped bad chunk: {global_id}")
                    print("source:", doc.metadata.get("source"))
                    print("page:", doc.metadata.get("page"))
                    print("chunk_id:", doc.metadata.get("chunk_id"))
                    print("error:", repr(single_e))
                    print("preview:", repr(doc.page_content[:500]))

                    skipped_chunks.append(
                        {
                            "chunk_id": global_id,
                            "source": doc.metadata.get("source"),
                            "page": doc.metadata.get("page"),
                            "error": repr(single_e),
                            "preview": doc.page_content[:500],
                        }
                    )

    print("=" * 80)
    print(f"Vector index saved to: {CHROMA_DIR}")
    print(f"Index building finished.")
    print(f"Skipped bad chunks: {len(skipped_chunks)}")
    print("=" * 80)

    if skipped_chunks:
        bad_log = PROJECT_ROOT / "outputs" / "bad_chunks.txt"
        bad_log.parent.mkdir(exist_ok=True)

        with open(bad_log, "w", encoding="utf-8") as f:
            for item in skipped_chunks:
                f.write("=" * 80 + "\n")
                f.write(f"chunk_id: {item['chunk_id']}\n")
                f.write(f"source: {item['source']}\n")
                f.write(f"page: {item['page']}\n")
                f.write(f"error: {item['error']}\n")
                f.write(f"preview: {item['preview']}\n")

        print(f"Bad chunk log saved to: {bad_log}")

    print("=" * 80)
    print(f"Vector index saved to: {CHROMA_DIR}")
    print("Index building finished.")
    print("=" * 80)

    return vectorstore


if __name__ == "__main__":
    build_index()