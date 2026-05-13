# Paper RAG Assistant

This project is a simple Retrieval-Augmented Generation (RAG) system for academic papers.

It can load PDF papers, split them into text chunks, build a vector database, retrieve relevant passages, and answer questions based on the retrieved context.

---

## 1. Project Goal

The goal of this project is to build a minimal but complete RAG pipeline for academic paper question answering.

The overall pipeline is:

```text
PDF papers
    ↓
Text extraction
    ↓
Text chunking
    ↓
Embedding
    ↓
Chroma vector database
    ↓
Semantic retrieval
    ↓
LLM-based question answering
    ↓
Answer with sources
```

This project is part of my Week 1 RAG learning practice. The main purpose is to understand the basic workflow of a RAG system and implement a working prototype.

---

## 2. Project Structure

```text
paper-rag-week1/
  data/
    papers/
      *.pdf
  chroma_db/
  src/
    __pycache__/
    batch_test.py
    build_index.py
    eval_retrieval.py
    load_pdf.py
    rag_qa.py
    retrieve.py
    split_text.py
    test_llm.py
  outputs/
    demo_qa.md
  README.md
  .gitignore
```

---

## 3. Main Components

### `src/test_llm.py`

Tests whether the LLM API can be called successfully.

This is used before running the RAG pipeline to make sure the model interface works correctly.

---

### `src/load_pdf.py`

Loads PDF files from:

```text
data/papers/
```

Each PDF is parsed into pages, and each page is stored as a document object.

---

### `src/split_text.py`

Splits long paper texts into smaller chunks.

Chunking is important because LLMs and embedding models cannot process arbitrarily long documents at once.

---

### `src/build_index.py`

Builds a Chroma vector index from the PDF chunks.

Main steps:

```text
load PDFs
    ↓
clean extracted text
    ↓
split documents into chunks
    ↓
generate embeddings
    ↓
save Chroma vector index
```

The vector index is saved to:

```text
chroma_db/
```

---

### `src/retrieve.py`

Retrieves relevant chunks for a given question.

This file is mainly used to test whether the retriever can find useful contexts from the vector database.

---

### `src/rag_qa.py`

Runs the full RAG-QA pipeline:

```text
question
    ↓
retrieve relevant chunks
    ↓
construct context
    ↓
call LLM
    ↓
generate answer
    ↓
show retrieved sources
```

---

### `src/batch_test.py`

Runs multiple questions automatically.

This can be used later for batch evaluation.

---

### `src/eval_retrieval.py`

Evaluates retrieval performance.

This file will be more useful in the next stage, when retrieval quality is systematically tested.

---

## 4. Environment Setup

Activate the conda environment:

```powershell
conda activate rag-week1
```

Install the required packages:

```powershell
pip install langchain langchain-community langchain-chroma langchain-huggingface sentence-transformers chromadb pypdf
```

If using OpenAI-compatible APIs, also install:

```powershell
pip install openai python-dotenv
```

---

## 5. Data Preparation

Put all PDF papers into:

```text
data/papers/
```

Example:

```text
data/
  papers/
    AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf
    DetectGPT Zero-Shot Machine-Generated Text Detection using Probability Curvature.pdf
    Release strategies and the social impacts of Language Models.pdf
```

Do not put PDF files into the `src/` folder.

The `src/` folder should only contain Python code.

---

## 6. How to Run

All commands should be run from the project root directory:

```powershell
cd C:\Users\22168\Desktop\Working\LLM Week8\paper-rag-week1
```

---

### Step 1: Test the LLM API

```powershell
python src/test_llm.py
```

This checks whether the LLM API is working.

---

### Step 2: Build the Vector Index

```powershell
python src/build_index.py
```

This command will:

```text
1. Load all PDFs from data/papers/
2. Extract text from PDF pages
3. Split text into chunks
4. Generate embeddings
5. Store vectors in Chroma
```

After this step, the vector database will be saved in:

```text
chroma_db/
```

---

### Step 3: Test Retrieval

```powershell
python src/retrieve.py
```

This checks whether the retriever can find relevant chunks for a question.

---

### Step 4: Run RAG Question Answering

```powershell
python src/rag_qa.py
```

Example question:

```text
What is the main contribution of AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees? Please answer based on the abstract and introduction.
```

---

## 7. Example Demo

### Question

```text
What is the main contribution of AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees? Please answer based on the abstract and introduction.
```

### Answer

```text
The main contribution of AdaDetectGPT is an adaptive LLM-generated text detector that leverages external training data to learn a witness function, while using normal approximation for false negative rate control, thereby providing statistical guarantees not present in prior logits-based detectors.
```

### Explanation

```text
The abstract and introduction state that existing logits-based detectors are sub-optimal. AdaDetectGPT improves upon them by adaptively learning a witness function from training data to enhance detection effectiveness. It builds on Fast-DetectGPT and introduces statistical control for false negative rate, giving the method statistical guarantees.
```

### Retrieved Sources

```text
[Source 1] AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf, page 0, chunk 209
[Source 2] AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf, page 1, chunk 213
[Source 3] AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees.pdf, page 41, chunk 368
```

---

## 8. Current Progress

The following parts have been completed:

- PDF loading
- Text extraction
- Text chunking
- Embedding generation
- Chroma vector database construction
- Basic semantic retrieval
- RAG-based question answering
- Source display

The current RAG pipeline can answer questions based on retrieved paper chunks.

---

## 9. Current Limitations

The current system is still a basic RAG prototype.

Main limitations:

1. The retriever may return noisy chunks.
2. The system does not yet support selecting a specific paper before asking questions.
3. The system retrieves from all papers at once.
4. The system does not yet include reranking.
5. The system does not yet include systematic retrieval evaluation.
6. Some PDF pages may contain parsing warnings or noisy extracted text.
7. The current answer quality depends strongly on retrieval quality.

For example, if the question is too vague, such as:

```text
What is the main contribution of this paper?
```

the system may not know which paper the user refers to.

A better question is:

```text
What is the main contribution of AdaDetectGPT Adaptive Detection of LLM-Generated Text with Statistical Guarantees? Please answer based on the abstract and introduction.
```

---

## 10. Notes on PDF Parsing

Some PDFs may show warnings such as:

```text
Ignoring wrong pointing object
```

This is usually a PDF parsing warning caused by non-standard internal PDF objects.

It is not necessarily fatal as long as valid text chunks are created.

If a PDF produces empty text or unreadable chunks, possible solutions include:

1. Re-download the PDF.
2. Re-save the PDF using `Print to PDF`.
3. Use another PDF loader such as `PyMuPDFLoader`.
4. Temporarily remove problematic PDFs from `data/papers/`.

---

## 11. Notes on Embedding Errors

Some chunks may fail during embedding because of noisy PDF text, hidden characters, or abnormal extracted content.

The current implementation can skip problematic chunks and continue building the vector index.

If bad chunks are skipped, they will be recorded in:

```text
outputs/bad_chunks.txt
```

---

## 12. Next Steps

The next stage is retrieval optimization.

Planned improvements:

1. Add paper-level source filtering.
2. Allow the user to choose one paper before asking questions.
3. Compare different `top_k` values.
4. Compare different chunk sizes and overlaps.
5. Add query rewriting.
6. Add reranking.
7. Add retrieval evaluation.
8. Add answer citation checking.
9. Build a simple Streamlit or Gradio interface.

---

## 13. Week 1 Summary

In Week 1, I completed a basic RAG system for academic paper question answering.

The system can:

```text
load PDF papers
split them into chunks
build a Chroma vector index
retrieve relevant contexts
generate answers using an LLM
display retrieved sources
```

This completes the first-stage RAG pipeline.

The next focus is improving retrieval quality and making the system more reliable for multi-paper question answering.