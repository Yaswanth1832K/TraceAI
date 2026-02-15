TraceAI – System Design Document

This document was initially generated using Kiro and then reviewed and refined by our team to align with the working prototype.

Project Name: TraceAI
Team Members: Yaswanth Jallipalli,Kanishkhan,Prakyath Nandigam,Nikshith Gurram

1. System Overview

TraceAI is an AI-assisted debugging tool that analyzes a software project together with runtime error messages to determine the probable cause of a bug and recommend a fix.

The system follows a Retrieval Augmented Generation (RAG) pipeline.
Project files are converted into searchable embeddings. When an error log is submitted, relevant code sections are retrieved and provided to a language model, which produces an explanation and suggested fix.

2. Architecture Components
1. Web Interface

Upload repository

Accept error messages

Display diagnosis and fix suggestions

2. Backend Server

Handles user requests

Coordinates analysis pipeline

Communicates with AI services

3. Code Loader

Reads project files

Splits files into smaller code sections

4. Embedding Generator

Converts code into vector representations

Enables semantic search in the project

5. Vector Database

Stores embeddings

Retrieves relevant code sections for an error

6. LLM Analyzer

Receives error log and retrieved code

Produces root-cause explanation and fix recommendation

3. Data Flow

User uploads repository

System extracts files

Files converted to embeddings

Stored in vector database

User pastes error log

Relevant code retrieved

AI analyzes error + code

Diagnosis returned to user

4. Why AI is Required

Traditional debugging tools rely on predefined rules and cannot interpret natural language errors or developer intent across multiple files.

TraceAI combines retrieval with a language model to reason over both code and error descriptions. This allows the system to identify probable root causes rather than only syntax mistakes.

5. Technology Stack

Frontend: React (or Flutter)
Backend: Node.js / Python
AI Model: Large Language Model API
Embeddings: Embedding API or sentence transformer
Vector Database: FAISS or Chroma

6. Future Improvements

Support additional programming languages

IDE plugin integration

Continuous integration debugging support

Automatic documentation generation

7. AI Processing Pipeline (RAG)

TraceAI uses a Retrieval Augmented Generation approach:

Source code files are divided into small sections.

Each section is converted into vector embeddings.

Embeddings are stored in a vector database.

When an error is submitted, a semantic search retrieves relevant code.

Retrieved code and the error message are provided to the language model.

The model produces a diagnosis and fix suggestion.

This method ensures the AI reasons using the actual project rather than general training knowledge.

8. System Limitations

The prototype works best on small to medium projects.

Analysis depends on clarity of the error message.

Some complex logical bugs may not be identified.

The system currently focuses on JavaScript-based environments.

9. Future Deployment Possibility

TraceAI can be extended into:

IDE plugin (VS Code extension)

Classroom teaching assistant

Open-source onboarding helper
