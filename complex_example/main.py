import time
from data_pipeline import DataPipeline

def main():
    print("Starting Main Application...")
    time.sleep(0.5)
    
    pipeline = DataPipeline()
    
    # Mock data payloads
    payloads = [
        {"id": 101, "event": "login", "user": "alice", "metadata": {"ip": "192.168.1.1"}},
        {"id": 102, "event": "purchase", "user": "bob", "metadata": {"item": "laptop", "price": 1200}},
        # This payload is missing the 'metadata' key which will cause an error deep in the pipeline
        {"id": 103, "event": "logout", "user": "charlie"}
    ]
    
    print(f"Loaded {len(payloads)} payloads for processing.")
    
    for payload in payloads:
        pipeline.process_event(payload)

if __name__ == "__main__":
    main()
