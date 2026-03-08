from utils.vat_calculator import apply_eu_vat, apply_us_tax

class TaxService:
    def compute_tax(self, order):
        country = order.user.country
        
        # We catch the error deep in the calculation graph
        subtotal = order.subtotal()
        
        if country == "US":
            return apply_us_tax(subtotal)
        elif country == "EU_VAT_ZONE":
            return apply_eu_vat(subtotal, order.items)
        return 0.0
