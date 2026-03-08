# TraceAI 🔍 — AI Mentor for Debugging Real-World Code

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![AWS Bedrock](https://img.shields.io/badge/AWS-Bedrock-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/bedrock/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

**TraceAI transforms any stack trace into a clear, senior-engineer-quality root-cause explanation with a working code fix — in seconds.**

[🚀 Quick Start](#️-setup--installation) · [🧠 How It Works](#-how-it-works) · [📡 API Reference](#-api-reference) · [🗺️ Roadmap](#-roadmap)

</div>

---

## 🏆 Hackathon Pitch

Debugging is the most time-consuming phase of software development. Junior developers lose hours chasing cryptic stack traces across multi-file codebases. **TraceAI** acts as an always-available senior engineer: you upload your codebase, paste an error, and TraceAI semantically retrieves the exact context that caused the bug, explaining it in plain English with a corrected snippet.

> **Built for:** Any developer who has ever stared at a `ZeroDivisionError` or `NullPointerException` at 2 AM.  
> **Powered by:** Amazon Bedrock (Titan Embeddings + Nova Lite) · OpenAI GPT-4o · FAISS · ChromaDB · FastAPI · Streamlit

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🧠 **RAG-Based Code Search** | Semantically retrieves the exact files and line ranges most relevant to your error |
| 🤖 **Dual LLM Modes** | AWS Bedrock (Nova Lite) for cloud-native analysis, or OpenAI GPT-4o for premium reasoning |
| 📦 **ZIP Upload** | Upload any Python/JS project as a ZIP — TraceAI handles extraction, chunking, and indexing automatically |
| 📐 **Structured Analysis** | Every bug gets: *What happened → Why → Where → How to fix → Corrected code* |
| ⚡ **FAISS + ChromaDB** | Two vector DB backends: FAISS for lightweight local use, ChromaDB for persistent multi-session storage |
| 🌐 **Dual Frontend** | Streamlit UI for quick demos; React + Vite frontend for production-ready experience |
| 🔒 **Secure Credential Handling** | All secrets via `.env` — no keys committed to source control |

---

## 🧠 How It Works

```
Your ZIP Project (Python / JS / TS / Go / Rust / JSON)
        ↓
   Extract source files
        ↓
   Split into semantic chunks (300–1000 lines each)
        ↓
   Embed via Amazon Titan V1  ──OR──  SentenceTransformer (all-MiniLM-L6-v2)
        ↓
   Store in FAISS Index  ──OR──  ChromaDB (persistent)
        ↓
   Paste error trace → top-5 semantic similarity search
        ↓
   Amazon Nova Lite (Bedrock)  ──OR──  GPT-4o (OpenAI)
        ↓
   Structured root-cause analysis + corrected code snippet
```

### Architecture Diagram

```
┌───────────────────────────────────┐
│           User Interface          │
│  Streamlit UI  ──or──  React/Vite │
└──────────────┬────────────────────┘
               │ HTTP (REST)
               ▼
┌───────────────────────────────────┐
│        FastAPI Backend            │
│  POST /upload   POST /analyze     │
│                                   │
│  ┌──────────┐   ┌──────────────┐  │
│  │ embedder │   │   analyzer   │  │
│  │  utils   │   │  retriever   │  │
│  └────┬─────┘   └──────┬───────┘  │
└───────┼─────────────────┼─────────┘
        ▼                 ▼
┌──────────────┐   ┌───────────────┐
│ FAISS / Chroma│  │ AWS Bedrock / │
│  Vector Store │  │   OpenAI API  │
└──────────────┘   └───────────────┘
```

---

## 📁 Project Structure

```
traceai/
├── backend/
│   ├── main.py          # FastAPI app entry point
│   ├── routes.py        # API endpoints (/upload, /analyze)
│   ├── embedder.py      # Amazon Titan Embeddings → FAISS index
│   ├── retriever.py     # Semantic similarity search (top-k)
│   ├── analyzer.py      # Amazon Nova Lite analysis engine
│   ├── engine.py        # Alternative: ChromaDB + GPT-4o pipeline
│   └── utils.py         # ZIP extraction + text chunking
├── frontend/
│   ├── app.py           # Streamlit UI (dark-mode, 2-column layout)
│   ├── src/
│   │   ├── App.jsx      # React root component
│   │   └── components/  # React UI components
│   ├── index.html       # Vite entry point
│   └── vite.config.js   # Vite configuration
├── example_project/     # Simple buggy Python project (for testing)
├── bigger_example/      # Multi-file e-commerce project (for testing)
├── .env.example         # Environment variable template
├── requirements.txt     # Python dependencies
└── README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.9+
- Node.js 18+ (for React frontend only)
- AWS Account with Bedrock access **or** OpenAI API key

---

### 1. Clone the Repository
```bash
git clone https://github.com/Yaswanth1832K/TraceAI.git
cd TraceAI
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Copy the example file and fill in your credentials:
```bash
cp .env.example .env
```

Edit `.env`:
```env
# AWS Bedrock (required for default mode)
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_REGION=us-east-1

# OpenAI (required for engine.py / GPT-4o mode)
OPENAI_API_KEY=your_openai_key_here
```

> ⚠️ **Never commit your `.env` file.** It is already listed in `.gitignore`.

---

### 4. Enable AWS Bedrock Model Access
Go to [AWS Bedrock Console](https://console.aws.amazon.com/bedrock/) → **Model access** and request access to:

| Model | Model ID |
|---|---|
| ✅ Amazon Titan Embeddings V1 | `amazon.titan-embed-text-v1` |
| ✅ Amazon Nova Lite | `amazon.nova-lite-v1:0` |

Ensure your IAM user has the **`AmazonBedrockFullAccess`** policy attached.

---

## ▶️ Running the Application

### Option A — Streamlit UI (Recommended for Demo)

Open **two terminals** in the project root:

**Terminal 1 — Backend:**
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8001 --reload
```

**Terminal 2 — Frontend:**
```bash
streamlit run frontend/app.py
```

Then open **[http://localhost:8501](http://localhost:8501)** in your browser.

---

### Option B — React + Vite UI

```bash
cd frontend
npm install
npm run dev
```

The React app will be available at **[http://localhost:5173](http://localhost:5173)**.

> Make sure the FastAPI backend is also running (Terminal 1 above).

---

## 🧪 Testing with Built-In Examples

### Example 1 — Simple Python Bug

1. Zip the `example_project/` folder
2. Upload in Streamlit → click **Index Repository**
3. Paste this trace:
```
Traceback (most recent call last):
  File "math_utils.py", line 18, in <module>
    process_data([])
  File "math_utils.py", line 4, in calculate_average
    average = total / len(numbers)
ZeroDivisionError: division by zero
```

**Expected Output:** TraceAI identifies the missing empty-list guard in `calculate_average` and provides a corrected version.

---

### Example 2 — Multi-File E-Commerce Project

1. Zip the `bigger_example/` folder
2. Upload and test with:
```
apply_discount(order, 10) returns a negative total price.
A 10% discount is resulting in the price going below zero.
File: order_service.py, function: apply_discount
```

**Expected Output:** TraceAI cross-references `order_service.py`, `database.py`, and `app.py` to trace the discount logic bug and suggest a fix with a guard clause.

---

## 📡 API Reference

Base URL: `http://localhost:8001`

### `POST /upload`
Upload a ZIP file to index the project codebase.

**Request:**
```bash
curl -X POST http://localhost:8001/upload \
  -F "file=@your_project.zip"
```

**Response:**
```json
{
  "message": "Project indexed successfully",
  "file_count": 4,
  "chunk_count": 23
}
```

---

### `POST /analyze`
Analyze an error trace against the indexed project.

**Request:**
```bash
curl -X POST http://localhost:8001/analyze \
  -H "Content-Type: application/json" \
  -d '{"error_trace": "ZeroDivisionError: division by zero at line 4 in math_utils.py"}'
```

**Response:**
```json
{
  "analysis": "## 1. What Happened\n...\n## 5. Corrected Code\n..."
}
```

Interactive docs available at **[http://localhost:8001/docs](http://localhost:8001/docs)** (Swagger UI).

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Backend API** | FastAPI + Uvicorn | High-performance REST API |
| **Frontend (Demo)** | Streamlit | Rapid UI with dark-mode styling |
| **Frontend (Production)** | React 18 + Vite | Full-featured web experience |
| **Embeddings (AWS)** | Amazon Titan Embed Text V1 | Code vectorization via Bedrock |
| **Embeddings (OSS)** | SentenceTransformer (MiniLM) | Local, no-API embedding fallback |
| **LLM (AWS)** | Amazon Nova Lite (Bedrock) | Root-cause analysis |
| **LLM (OpenAI)** | GPT-4o | Premium JSON-structured analysis |
| **Vector DB (Fast)** | FAISS (CPU) | Lightweight local similarity search |
| **Vector DB (Persistent)** | ChromaDB | Persistent multi-session storage |
| **Infrastructure** | AWS EC2 (optional) | Cloud deployment target |

---

## 📋 Requirements

```txt
fastapi
uvicorn
streamlit
boto3
faiss-cpu
numpy
python-multipart
pydantic
requests
python-dotenv
```

For the `engine.py` (ChromaDB + GPT-4o) pipeline, also install:
```bash
pip install chromadb langchain-chroma langchain-community langchain-text-splitters sentence-transformers openai
```

---

## 🗺️ Roadmap

- [x] ZIP upload → FAISS index → Bedrock analysis (v1 core)
- [x] ChromaDB persistent storage + GPT-4o integration (v2 engine)
- [x] Streamlit dark-mode UI
- [x] React + Vite alternative frontend
- [ ] GitHub URL input (no ZIP needed — clone & index directly)
- [ ] Support for Java, Go, Rust, TypeScript out of the box
- [ ] VS Code extension integration
- [ ] API Token authentication & rate-limiting
- [ ] CI/CD with GitHub Actions + EC2 auto-deploy

---

## 📄 License

MIT License — built as a hackathon prototype. See [LICENSE](LICENSE) for details.

---

<div align="center">

**If TraceAI saved you debugging time, give it a ⭐ on [GitHub](https://github.com/Yaswanth1832K/TraceAI)!**

</div>
