# Ask-Your-PDF — Retrieval-Augmented Generation (RAG)

## Overview
Ask-Your-PDF is a **Retrieval-Augmented Generation (RAG)** application that allows users to upload a PDF document and ask questions about its contents.  
The system retrieves relevant sections from the document and generates answers **strictly based on retrieved context**, preventing hallucinations.

This project demonstrates how modern GenAI systems combine **information retrieval** with **language models** to produce grounded, reliable answers.

---

## Problem Statement
Large Language Models (LLMs) can generate fluent responses but often hallucinate when asked about documents they have not explicitly seen.  
Relying solely on model memory leads to inaccurate or misleading answers.

This project solves the problem by:
- Extracting text directly from PDFs
- Retrieving only relevant document chunks
- Forcing the model to answer **only using retrieved content**

---

## Core Design Principle
> **No retrieval = no answer.**  
If the answer is not present in the PDF, the system responds with:  
> *“The document does not contain this information.”*

---

## Architecture
PDF Document
↓
Text Extraction
↓
Chunking (overlapping)
↓
Embeddings
↓
Vector Store (FAISS)
↓
Top-K Retrieval
↓
LLM Answer (Context-only)


---

## Features
- Upload and process PDF documents
- Ask natural language questions about the document
- Context-aware answers grounded in document text
- Local execution (no API keys, no paid services)
- Hallucination-resistant by design
- Modular, extensible architecture

---

## Tech Stack
- Python
- Streamlit (UI)
- Ollama (`llama3.2:3b`) — Local LLM or any small llm
- SentenceTransformers — Embeddings
- FAISS — Vector similarity search
- PDFPlumber / PyPDF — PDF text extraction

---

## Repository Structure

ask-your-pdf/
├── app.py # Streamlit UI
├── pdf_loader.py # PDF text extraction
├── chunker.py # Text chunking logic
├── embedder.py # Embedding generation
├── retriever.py # Vector search
├── llm_answerer.py # Context-grounded answering
├── requirements.txt
└── README.md


---

## How It Works
1. User uploads a PDF file
2. Text is extracted from the document
3. Text is split into overlapping chunks
4. Each chunk is converted into an embedding
5. Embeddings are stored in a FAISS vector index
6. User question is embedded
7. Most relevant chunks are retrieved
8. Retrieved chunks + question are sent to the LLM
9. LLM answers **only using the provided context**

---

## Why This Project Matters
Ask-Your-PDF demonstrates a **production-grade pattern** used in real-world AI systems: Retrieval-Augmented Generation (RAG).  
Instead of trusting a language model’s internal knowledge, the system **grounds every answer in verifiable document content**.

This mirrors how enterprise tools (legal search, internal knowledge bases, compliance systems) are built—making this project highly relevant for **applied GenAI and data engineering roles**.

---

## Key Design Decisions

### 1. Strict Context Enforcement
The LLM is explicitly instructed to:
- Use **only** retrieved chunks
- Decline to answer when information is missing

This eliminates hallucinations and ensures predictable, auditable outputs.

### 2. Chunking with Overlap
Documents are split into overlapping chunks to:
- Preserve semantic continuity across sections
- Avoid cutting off important context mid-sentence
- Improve retrieval accuracy for long PDFs

### 3. Lightweight Local Models
The system runs entirely **offline** using:
- Small open-source LLMs via Ollama
- Local embedding models

This keeps the project:
- Cost-free
- Privacy-friendly
- Deployable on modest hardware

---

## Example Interaction

**User Question:**  
> What is the refund policy mentioned in the document?

**System Behavior:**
- Retrieves the most relevant PDF sections
- Generates an answer only if the policy text exists
- Otherwise responds:  
  > *The document does not contain this information.*

This behavior is intentional and central to the project’s reliability.

---

## Limitations
- Performance depends on PDF text quality (scanned PDFs may require OCR)
- Not optimized for very large document collections (single-PDF focus)
- No conversational memory across questions (by design)

These tradeoffs keep the system **simple, transparent, and educational**.

---

## Possible Extensions
- Add OCR support for scanned PDFs
- Support multi-document querying
- Introduce metadata-aware retrieval (page numbers, sections)
- Add source citation highlighting in answers
- Swap FAISS for a persistent vector database

---

## Learning Outcomes
This project demonstrates hands-on understanding of:
- Retrieval-Augmented Generation (RAG)
- Vector embeddings and similarity search
- Prompt control to prevent hallucinations
- Modular AI system design
- Local-first GenAI tooling

---

## Who This Is For
- Data Analysts transitioning into GenAI
- ML / AI engineering beginners
- Developers building document Q&A tools
- Anyone learning **practical, non-hype GenAI**
