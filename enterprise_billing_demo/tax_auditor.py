TAX_ZONES = {
    "US": 0.08,    # 8% State Tax
    "UK": 0.20,    # 20% VAT
    "DE": 0.19,    # 19% MwSt
    "AU": 0.10     # 10% GST
}

def calculate_tax_liability(base_amount, country_code):
    """
    Applies the specific regional tax rate to the user's base subscription amount.
    """
    tax_rate = TAX_ZONES.get(country_code, 0.0)
    
    # If base_amount is mistakenly passed as a string (e.g. from JSON payload),
    # this multiplication will fail because you can't multiply a sequence by a non-int (float).
    tax_cost = base_amount * tax_rate
    
    return tax_cost
