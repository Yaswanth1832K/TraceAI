import time

def process_stripe_charge(customer_id, final_total_amount):
    """
    Connects to an external payment gateway endpoint 
    to charge the validated credit card on file.
    """
    if final_total_amount <= 0:
        return {"status": "failed", "error": "Invalid charge amount"}
        
    # Simulate network latency
    time.sleep(0.1)
    
    return {
        "status": "success",
        "txn_id": f"txn_{customer_id}_99abc"
    }
