# TraceAI 🔍 – AI Mentor for Debugging Real-World Code

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128+-green.svg)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45+-red.svg)](https://streamlit.io)
[![AWS Bedrock](https://img.shields.io/badge/AWS-Bedrock-orange.svg)](https://aws.amazon.com/bedrock/)

TraceAI is an AI-powered debugging assistant that analyzes your codebase and explains bugs like a senior software engineer. Upload your project, paste a stack trace, and get an instant root-cause explanation with a corrected code snippet.

---

## 🚀 How It Works

```
Your ZIP project
      ↓
Extract .py / .js files
      ↓
Split into code chunks (300 lines each)
      ↓
Amazon Bedrock Titan Embeddings → FAISS vector index
      ↓
Paste error trace → find top 5 relevant chunks
      ↓
Amazon Nova Lite (via Bedrock) → root-cause analysis + fix
```

---

## 📁 Project Structure

```
traceai/
├── backend/
│   ├── main.py          # FastAPI entry point
│   ├── routes.py        # API endpoints (/upload, /analyze)
│   ├── embedder.py      # Bedrock Titan Embeddings + FAISS index
│   ├── retriever.py     # Semantic similarity search
│   ├── analyzer.py      # Amazon Nova Lite analysis
│   └── utils.py         # ZIP extraction + text chunking
├── frontend/
│   └── app.py           # Streamlit UI
├── example_project/     # Simple buggy Python project for testing
├── bigger_example/      # Multi-file e-commerce project for testing
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Yaswanth1832K/TraceAI.git
cd TraceAI
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure AWS Credentials
Create a `.env` file in the root directory:
```env
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_REGION=us-east-1
```

> ⚠️ **Never commit your `.env` file to Git.** It is included in `.gitignore`.

### 4. Enable Bedrock Model Access
Go to [AWS Bedrock Console](https://console.aws.amazon.com/bedrock/) → **Model access** and enable:
- ✅ **Titan Embeddings V1** (amazon.titan-embed-text-v1)
- ✅ **Nova Lite** (amazon.nova-lite-v1:0)

Make sure your IAM user has the `AmazonBedrockFullAccess` policy attached.

---

## ▶️ Running the Application

Open **two separate terminals** in the project root:

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

## 🧪 Testing with Examples

### Simple Example
1. Zip the `example_project/` folder
2. Upload the ZIP in Streamlit → click **Index Repository**
3. Paste this error:
```
Traceback (most recent call last):
  File "math_utils.py", line 18, in <module>
    process_data([])
  File "math_utils.py", line 4, in calculate_average
    average = total / len(numbers)
ZeroDivisionError: division by zero
```

### Multi-File Example
1. Zip the `bigger_example/` folder (4-file e-commerce order system)
2. Upload and test with:
```
apply_discount(order, 10) returns a negative total price.
A 10% discount is resulting in the price going below zero.
File: order_service.py, function: apply_discount
```

---

## 📡 API Reference

| Endpoint | Method | Description |
|---|---|---|
| `/upload` | POST | Upload a ZIP file to index the project |
| `/analyze` | POST | Analyze an error trace against the indexed project |

### `/upload`
```bash
curl -X POST http://localhost:8001/upload \
  -F "file=@your_project.zip"
```

### `/analyze`
```bash
curl -X POST http://localhost:8001/analyze \
  -H "Content-Type: application/json" \
  -d '{"error_trace": "ZeroDivisionError: division by zero"}'
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI + Uvicorn |
| Frontend | Streamlit |
| Embeddings | Amazon Bedrock (Titan Embed Text V1) |
| LLM | Amazon Bedrock (Nova Lite) |
| Vector DB | FAISS (local) |
| Cloud | AWS (EC2 for deployment) |

---

## 📋 Requirements

See [requirements.txt](./requirements.txt):
```
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

---

## 🔮 Future Enhancements
- Support for more languages (Java, TypeScript, Go)
- GitHub URL input instead of ZIP upload
- History of past analyses
- EC2 deployment with a public domain
- Multi-file cross-reference debugging

---

## 📄 License
MIT License — built as a hackathon prototype.
