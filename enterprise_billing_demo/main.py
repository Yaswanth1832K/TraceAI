from pipeline import execute_billing_pipeline
import logging

logging.basicConfig(level=logging.INFO)

def run_monthly_batch():
    """
    Simulates a cron job pulling subscriptions from a message queue
    and passing them to the billing pipeline.
    """
    logging.info("Starting Enterprise Billing Batch Job")
    
    # Simulating data ingestion from an external API or queue
    # The 'base_price' for U102 was ingested incorrectly as a string instead of a float
    messages = [
        {"user_id": "U101", "tier": "Pro", "base_price": 99.99},
        {"user_id": "U102", "tier": "Enterprise", "base_price": "499.00"}, 
        {"user_id": "U103", "tier": "Basic", "base_price": 19.99}
    ]
    
    for msg in messages:
        execute_billing_pipeline(msg)

if __name__ == "__main__":
    run_monthly_batch()
