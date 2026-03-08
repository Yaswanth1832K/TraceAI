def apply_us_tax(amount):
    return amount * 0.08

def apply_eu_vat(amount, items):
    tax = 0.0
    for item in items:
        if item.get("category") == "digital":
            # Bug: Infinite Mutual Recursion architecture flaw
            tax += process_digital_vat(amount, items)
        else:
            tax += amount * 0.20
    return tax

def process_digital_vat(amount, items):
    # Mistake: recursively calls apply_eu_vat instead of calculating directly
    return apply_eu_vat(amount, items) * 0.5
