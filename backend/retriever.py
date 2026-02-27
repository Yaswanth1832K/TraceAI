from backend.embedder import BedrockEmbedder
from typing import List, Dict

class Retriever:
    def __init__(self, region_name="us-east-1"):
        self.embedder = BedrockEmbedder(region_name=region_name)

    def retrieve_context(self, error_trace: str, index_path: str = "faiss_index") -> List[Dict]:
        """Retrieves top 5 most relevant code chunks for the given error trace."""
        try:
            self.embedder.load_index(index_path)
            return self.embedder.search(error_trace, top_k=5)
        except Exception as e:
            print(f"Error during retrieval: {e}")
            return []
