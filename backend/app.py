from flask import Flask, request, jsonify
from rag_pipeline import TraceAIRAG

app = Flask(__name__)
rag = TraceAIRAG()

@app.route('/upload', methods=['POST'])
def upload_repo():
    """
    Endpoint to receive project repository path or files.
    """
    data = request.json
    repo_path = data.get('path')
    if not repo_path:
        return jsonify({"error": "No path provided"}), 400
    
    rag.index_project(repo_path)
    return jsonify({"message": "Project indexed successfully"}), 200

@app.route('/analyze', methods=['POST'])
def analyze_error():
    """
    Endpoint to receive error log and return analysis.
    """
    data = request.json
    error_log = data.get('error_log')
    if not error_log:
        return jsonify({"error": "No error log provided"}), 400
    
    result = rag.analyze(error_log)
    return jsonify(result), 200

if __name__ == '__main__':
    print("TraceAI Backend Running on http://localhost:5000")
    app.run(debug=True, port=5000)
