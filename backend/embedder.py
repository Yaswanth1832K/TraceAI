import boto3
import json
import numpy as np
import faiss
import os
import pickle
from typing import List, Dict

class BedrockEmbedder:
    def __init__(self, region_name="us-east-1"):
        self.bedrock = boto3.client(
            service_name="bedrock-runtime",
            region_name=region_name
        )
        self.model_id = "amazon.titan-embed-text-v1"
        self.index = None
        self.metadata = []

    def get_embedding(self, text: str) -> List[float]:
        body = json.dumps({"inputText": text})
        response = self.bedrock.invoke_model(
            body=body,
            modelId=self.model_id,
            accept="application/json",
            contentType="application/json"
        )
        response_body = json.loads(response.get("body").read())
        return response_body.get("embedding")

    def create_index(self, chunks: List[Dict[str, str]], index_path: str = "faiss_index"):
        embeddings = []
        self.metadata = []
        
        for chunk in chunks:
            embedding = self.get_embedding(chunk["content"])
            embeddings.append(embedding)
            self.metadata.append(chunk["metadata"])
            self.metadata[-1]["content"] = chunk["content"]

        embeddings_np = np.array(embeddings).astype("float32")
        dimension = embeddings_np.shape[1]
        
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings_np)
        
        # Save index and metadata
        faiss.write_index(self.index, f"{index_path}.index")
        with open(f"{index_path}.metadata", "wb") as f:
            pickle.dump(self.metadata, f)

    def load_index(self, index_path: str = "faiss_index"):
        if os.path.exists(f"{index_path}.index"):
            self.index = faiss.read_index(f"{index_path}.index")
            with open(f"{index_path}.metadata", "rb") as f:
                self.metadata = pickle.load(f)
        else:
            raise FileNotFoundError("Index files not found.")

    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        if self.index is None:
            self.load_index()
            
        query_embedding = np.array([self.get_embedding(query)]).astype("float32")
        distances, indices = self.index.search(query_embedding, top_k)
        
        results = []
        for idx in indices[0]:
            if idx != -1 and idx < len(self.metadata):
                results.append(self.metadata[idx])
        return results
