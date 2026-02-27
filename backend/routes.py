from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
import os
import shutil
from backend.utils import extract_zip, chunk_text
from backend.embedder import BedrockEmbedder
from backend.retriever import Retriever
from backend.analyzer import BedrockAnalyzer

router = APIRouter()
embedder = BedrockEmbedder()
retriever = Retriever()
analyzer = BedrockAnalyzer()

UPLOAD_DIR = "uploads"
INDEX_PATH = "faiss_index"

class AnalysisRequest(BaseModel):
    error_trace: str

@router.post("/upload")
async def upload_project(file: UploadFile = File(...)):
    if not file.filename.endswith(".zip"):
        raise HTTPException(status_code=400, detail="Only ZIP files are supported.")
    
    zip_path = os.path.join(UPLOAD_DIR, file.filename)
    extract_path = os.path.join(UPLOAD_DIR, "extracted")
    
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    
    with open(zip_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    # 1. Extract
    files = extract_zip(zip_path, extract_path)
    
    # 2. Chunk
    all_chunks = []
    for f in files:
        all_chunks.extend(chunk_text(f))
    
    if not all_chunks:
        raise HTTPException(status_code=400, detail="No source files (.py, .js) found in ZIP.")
        
    # 3. Embed and Index
    try:
        embedder.create_index(all_chunks, INDEX_PATH)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Indexing failed: {str(e)}")
        
    return {"message": "Project indexed successfully", "file_count": len(files), "chunk_count": len(all_chunks)}

@router.post("/analyze")
async def analyze_error(request: AnalysisRequest):
    # 1. Retrieve
    context = retriever.retrieve_context(request.error_trace, INDEX_PATH)
    if not context:
        raise HTTPException(status_code=404, detail="No relevant code found. Did you upload the project?")
        
    # 2. Analyze
    result = analyzer.analyze_error(request.error_trace, context)
    return {"analysis": result}
