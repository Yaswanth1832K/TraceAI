import os
import zipfile
import shutil
from typing import List, Dict

def extract_zip(zip_path: str, extract_to: str) -> List[str]:
    """Extracts a ZIP file and returns a list of paths to .py and .js files."""
    if os.path.exists(extract_to):
        shutil.rmtree(extract_to)
    os.makedirs(extract_to)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        
    extracted_files = []
    for root, _, files in os.walk(extract_to):
        for file in files:
            if file.endswith(('.py', '.js')):
                extracted_files.append(os.path.join(root, file))
    return extracted_files

def chunk_text(file_path: str, chunk_size: int = 300) -> List[Dict[str, str]]:
    """Reads a file and splits its content into chunks of around chunk_size lines."""
    chunks = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for i in range(0, len(lines), chunk_size):
            chunk_lines = lines[i : i + chunk_size]
            chunk_content = "".join(chunk_lines)
            chunks.append({
                "content": chunk_content,
                "metadata": {
                    "file": os.path.basename(file_path),
                    "path": file_path,
                    "start_line": i + 1,
                    "end_line": i + len(chunk_lines)
                }
            })
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        
    return chunks
