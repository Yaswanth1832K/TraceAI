from invoice_generator import generate_final_invoice
from payment_gateway import process_stripe_charge

def execute_billing_pipeline(webhook_payload):
    """
    Coordinates building an invoice and processing a charge via Stripe.
    """
    user_id = webhook_payload.get("user_id")
    price = webhook_payload.get("base_price")
    tier = webhook_payload.get("tier")
    
    print(f"--- Pipeline start for {user_id} ({tier}) ---")
    
    # Generate structured invoice
    invoice = generate_final_invoice(user_id, price)
    
    # Extract total amount with tax
    total_due = invoice["total_amount"]
    
    # Process payment
    result = process_stripe_charge(user_id, total_due)
    
    if result["status"] == "success":
        print(f"[SUCCESS] Successfully charged {total_due} to {user_id}")
    else:
        print(f"[FAILED] Failed to charge {user_id}: {result['error']}")
