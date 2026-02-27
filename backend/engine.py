import os
from typing import List, Dict
from chromadb.utils import embedding_functions
from langchain_chroma import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class TraceAIEngine:
    def __init__(self, persist_directory="./chroma_db", model_name="all-MiniLM-L6-v2"):
        self.persist_directory = persist_directory
        self.embedding_function = SentenceTransformerEmbeddings(model_name=model_name)
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
            separators=["\n\n", "\n", " ", ""]
        )
        self.vector_store = None
        self._init_db()

    def _init_db(self):
        self.vector_store = Chroma(
            collection_name="traceai_v2",
            embedding_function=self.embedding_function,
            persist_directory=self.persist_directory
        )

    def index_repository(self, path: str):
        """Recursively scan and index code files."""
        docs = []
        metadatas = []
        
        excluded_dirs = {'.git', 'node_modules', '__pycache__', 'venv', 'dist', 'build'}
        supported_extensions = {'.py', '.js', '.ts', '.tsx', '.jsx', '.json', '.md', '.go', '.rs'}

        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if d not in excluded_dirs]
            
            for file in files:
                if any(file.endswith(ext) for ext in supported_extensions):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            text = f.read()
                            chunks = self.text_splitter.split_text(text)
                            for i, chunk in enumerate(chunks):
                                docs.append(chunk)
                                metadatas.append({
                                    "source": os.path.relpath(file_path, path),
                                    "chunk": i
                                })
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

        if docs:
            self.vector_store.add_texts(texts=docs, metadatas=metadatas)
            return len(docs)
        return 0

    def query(self, error_log: str, top_k: int = 5):
        """Retrieve relevant code context."""
        results = self.vector_store.similarity_search(error_log, k=top_k)
        return results

    def analyze_with_llm(self, error_log: str, context: List[str]):
        """Call LLM to analyze error given context."""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return {
                "root_cause": "OpenAI API Key is missing.",
                "explanation": "TraceAI requires an OpenAI API key to perform high-level reasoning. Without it, I can only see your code but not explain the bug.",
                "suggested_fix": "Please add 'OPENAI_API_KEY=your_key_here' to a .env file in the backend folder, or set it in your terminal environment.",
                "relevant_files": []
            }

        client = OpenAI(api_key=api_key)
        
        context_block = "\n---\n".join([doc.page_content if hasattr(doc, 'page_content') else doc for doc in context])
        
        prompt = f"""
You are TraceAI v2.0, a premium software engineering assistant.
Analyze the following runtime error and the provided project context.

ERROR LOG:
{error_log}

PROJECT CONTEXT:
{context_block}

Produce a detailed JSON analysis including:
1. 'root_cause': Precise technical cause.
2. 'explanation': Detailed reasoning.
3. 'suggested_fix': Actionable code or command.
4. 'relevant_files': List of files involved.
"""
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        import json
        return json.loads(response.choices[0].message.content)
