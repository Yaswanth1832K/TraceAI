class ErrorAnalyzer:
    """
    Utilizes an LLM to reason over error logs and retrieved code context.
    """
    def __init__(self, model="gpt-4o"):
        self.model = model

    def generate_fix(self, error_log, code_context):
        """
        Constructs a prompt and calls the LLM.
        """
        # Mocking an AI response for the hackathon prototype
        return {
            "root_cause": "The module 'express' is being imported but is not listed in package.json.",
            "explanation": "Your index.js requires express, but your dependencies are empty. Node.js cannot find the package in node_modules.",
            "suggested_fix": "Run 'npm install express' to add the dependency to your project.",
            "relevant_files": ["index.js", "package.json"]
        }
