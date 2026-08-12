Retrieval-Augmented Generation LLM

A Retrieval-Augmented Generation (RAG) system built from scratch without relying on AI coding assistants such as autocomplete or GitHub Copilot. The project implements the core RAG pipeline, including document parsing, text preprocessing, chunking, embeddings, SQLite storage, semantic retrieval, and question answering.

Setup
Activate the virtual environment:
.venv\Scripts\Activate
Configure your Python interpreter to:
.venv\Scripts\python.exe
Add source documents to the documents/ folder. Supported formats include:
.pdf
.docx
.txt
Textbooks and other technical documents can be used as the source material.
Run ollama3 after install all dependencies.
ollama run llama3


Step 1: Document Preprocessing

Run Main.py to preprocess the documents in the documents/ folder.

The preprocessing pipeline:

Documents
    ↓
Parsing
    ↓
Text Cleaning
    ↓
Tokenization
    ↓
100-Word Chunking
    ↓
Embeddings
    ↓
SQLite Database

To run the preprocessing tests and inspect the resulting database:

python -m pytest tests/test_preprocessing_main.py -v -s

The test output displays information such as:

Documents:
The document ID, filename, and number of pages for each processed document.

Chunks per document:
The document ID and number of 100-word chunks stored in the SQLite database.

Step 2: Semantic Retrieval

Run:

python retriever.py

The retriever will take a user's question, generate an embedding for the question, compare it against the stored document embeddings using cosine similarity, and return the most relevant document chunks.

Project Goal

The goal of this project is to understand and implement the fundamental components of a RAG system rather than relying on high-level frameworks to abstract away the underlying concepts.