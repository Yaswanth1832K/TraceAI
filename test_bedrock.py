from dotenv import load_dotenv
import os
import boto3

load_dotenv()
print("AK:", os.environ.get("AWS_ACCESS_KEY_ID"))
print("Session Token:", os.environ.get("AWS_SESSION_TOKEN"))

try:
    bedrock = boto3.client(
        service_name="bedrock-runtime",
        region_name=os.environ.get("AWS_REGION", "us-east-1")
    )
    response = bedrock.invoke_model(
        body='{"inputText": "hello"}',
        modelId="amazon.titan-embed-text-v1",
        accept="application/json",
        contentType="application/json"
    )
    print("Success")
except Exception as e:
    print("Error:", e)
