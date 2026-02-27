import boto3
import json
from typing import List, Dict

class BedrockAnalyzer:
    def __init__(self, region_name="us-east-1"):
        self.bedrock = boto3.client(
            service_name="bedrock-runtime",
            region_name=region_name
        )
        # Amazon Nova Lite — current-gen Amazon model, no Marketplace billing required
        self.model_id = "amazon.nova-lite-v1:0"

    def analyze_error(self, error_trace: str, context: List[Dict]) -> str:
        """Sends error trace and context to Amazon Nova Lite for analysis."""

        context_str = "\n\n".join([
            f"File: {c['file']} (Lines {c['start_line']}-{c['end_line']})\nContent:\n{c['content']}"
            for c in context
        ])

        prompt = (
            "You are a senior software architect helping a junior developer debug a bug.\n\n"
            "Analyze the provided code snippets and the error message/stack trace.\n"
            "Provide a structured response with these sections:\n"
            "1. What happened\n"
            "2. Why it happened\n"
            "3. Where in code (file and line number)\n"
            "4. How to fix\n"
            "5. Corrected code snippet\n\n"
            f"Error message/stack trace:\n{error_trace}\n\n"
            f"Relevant code context:\n{context_str}"
        )

        body = json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": [{"text": prompt}]
                }
            ],
            "inferenceConfig": {
                "maxTokens": 1024,
                "temperature": 0.5
            }
        })

        try:
            response = self.bedrock.invoke_model(
                body=body,
                modelId=self.model_id,
                accept="application/json",
                contentType="application/json"
            )
            response_body = json.loads(response.get("body").read())
            return response_body["output"]["message"]["content"][0]["text"]
        except Exception as e:
            return f"Error analyzing with Bedrock: {str(e)}"
