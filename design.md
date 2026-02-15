# TraceAI – System Design

## 1. System Overview
TraceAI uses a Retrieval-Augmented Generation (RAG) architecture to provide contextual debugging assistance. By combining code indexing with LLM reasoning, it identifies the root cause of bugs based on actual project source code rather than generic patterns.

## 2. Architecture Components

### 2.1 Web Interface (Frontend)
- Simple dashboard for uploading repositories and pasting error logs.
- Visual display of the "Reasoning Path" and suggested fixes.

### 2.2 Backend Server
- API entry point (FastAPI/Flask).
- Manages the interaction between the file system, vector database, and the AI model.

### 2.3 Code Loader & Embedder
- **Code Loader:** Reads the repository, ignores irrelevant files (.git, node_modules), and chunks code into logical blocks (functions, classes).
- **Embedder:** Converts code chunks into high-dimensional vectors representing their semantic meaning.

### 2.4 Vector Database
- Stores the code embeddings.
- Provides fast similarity search to find code snippets related to the user's error message.

### 2.5 LLM Analyzer
- The "Brain" of the system.
- Receives the error log + retrieved code context.
- Outputs a detailed explanation and a specific fix suggestion.

## 3. Data Flow
1. **Ingestion:** User uploads a repo → System chunks and embeds the code → Vectors stored in DB.
2. **Query:** User pastes error log → System embeds the error log query.
3. **Retrieval:** System finds the top-3 most relevant code blocks from the Vector DB.
4. **Generation:** Error + Code Context → LLM → Diagnosis and Fix.

## 4. Why AI is Necessary
Traditional debuggers point to a line of code but often miss the *reason* why that line failed (e.g., a missing configuration in another file). TraceAI's LLM can reason across multiple files to find the missing link.

## 5. Technology Stack
- **Languages:** Python (Backend), JavaScript (Frontend/Sample Apps)
- **Frameworks:** FastAPI, React
- **Vector Search:** ChromaDB
- **Models:** gpt-4o or equivalent

## 6. System Limitations
- Currently optimized for text-based source code (no compiled binaries).
- Performance scales with repository size; very large repos may require more advanced chunking.

## 7. Future Improvements
- VS Code Extension for real-time debugging.
- Support for complex multi-language projects.
- Integration with CI/CD logs.
