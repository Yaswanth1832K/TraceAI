from tax_auditor import calculate_tax_liability
from subscription_manager import get_user_location

def generate_final_invoice(user, subtotal):
    """
    Looks up a user's geographical location to determine regional taxes,
    then adds up fees and generates an invoice hash.
    """
    
    # Get regional code for tax laws
    country_code = get_user_location(user)
    
    # Calculate tax based on location
    tax_amount = calculate_tax_liability(subtotal, country_code)
    
    # Build complete total
    total = subtotal + tax_amount
    
    return {
        "invoice_id": f"INV-{user}-998",
        "subtotal": subtotal,
        "tax": tax_amount,
        "total_amount": total
    }
