from utils.geo_mapper import get_shipping_zone

class ShippingCalculator:
    def calculate(self, order):
        zone = get_shipping_zone(order.user.country)
        base_rate = 10.0
        
        if zone == "DOMESTIC":
            return base_rate
        elif zone == "INTERNATIONAL":
            return base_rate * 3.5
        elif zone == "UNKNOWN":
            return base_rate * 5.0
