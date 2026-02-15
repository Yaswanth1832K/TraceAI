# TraceAI – System Design Document

**Project Name:** TraceAI

## 1. System Overview
TraceAI utilizes a **Retrieval-Augmented Generation (RAG)** architecture to provide project-specific debugging assistance. Unlike generic LLMs, TraceAI "sees" your local code before it tries to solve your bug.

## 2. Architecture Components

### 2.1 Web Interface (Frontend)
- **Built with:** React or Flutter.
- **Purpose:** Handles file uploads, displays error analysis, and provides a "copy-to-clipboard" feature for fixes.

### 2.2 Backend API
- **Built with:** Python (FastAPI).
- **Purpose:** Coordinates the analysis pipeline and manages communication between the DB and the LLM.

### 2.3 RAG Processing Pipeline
1. **Code Loader:** Recursively reads source files, ignoring non-code assets.
2. **Chunker:** Splits files into small, context-aware segments (classes/functions).
3. **Embedder:** Converts text chunks into 1536-dimension vectors using OpenAI/SentenceTransformers.
4. **Vector Database:** (ChromaDB) Stores and queries code embeddings.

### 2.4 LLM Analysis Engine
- **Engine:** GPT-4o or Claude 3.5.
- **Logic:** Combines the user's error log with retrieved code context to generate a "Root Cause Diagnosis."

## 3. Data Flow Diagram (Text-based)
```
User Upload -> Code Ingestion -> Local Vector DB (Index)
User Error  -> Semantic Search -> Relevant Code Snippets
Relevant Code + Error Log -> LLM Prompt -> Diagnosis & Fix
```

## 4. Why AI is Required
Debugging often requires matching a high-level error (e.g., `ModuleNotFound`) with a low-level cause (e.g., a missing field in `package.json`). Conventional tools only show the crash site; TraceAI's AI finds the *missing ingredients* that caused the crash.

## 5. Technology Stack
- **Frontend:** React / Tailwind CSS
- **Backend:** Python / FastAPI
- **Database:** ChromaDB (Vector Store)
- **AI/ML:** OpenAI Embeddings & GPT-4 API
- **Version Control:** Git

## 6. System Limitations
- Optimized for text-based languages (JS, Python, TS).
- Does not currently support debugging compiled binaries or low-level assembly.

## 7. Future Roadmap
- VS Code Extension integration.
- Automated PR creation for bug fixes.
- Support for complex microservice architectures.

---
*Note: This system design was generated using an AI-assisted workflow and manually refined for TraceAI.*
