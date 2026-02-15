from embedder import CodeEmbedder
from retriever import CodeRetriever
from analyzer import ErrorAnalyzer

class TraceAIRAG:
    """
    Orchestrates the Retrieval-Augmented Generation pipeline for TraceAI.
    """
    def __init__(self):
        self.embedder = CodeEmbedder()
        self.retriever = CodeRetriever()
        self.analyzer = ErrorAnalyzer()

    def index_project(self, repo_path):
        """
        Step 1: Load code, chunk it, and store in vector DB.
        """
        print(f"Indexing project at: {repo_path}")
        # Logic to read files and generate embeddings
        # self.retriever.add_to_index(embeddings)
        pass

    def analyze(self, error_log):
        """
        Step 2: Retrieve relevant code and generate fix suggestions.
        """
        print(f"Analyzing error: {error_log[:50]}...")
        
        # 1. Find relevant code blocks
        context = self.retriever.search(error_log)
        
        # 2. Use LLM to diagnose based on context
        analysis = self.analyzer.generate_fix(error_log, context)
        
        return analysis
