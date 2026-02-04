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
