def get_shipping_zone(country_code):
    if country_code in ["US", "CA"]:
        return "DOMESTIC"
    elif country_code in ["UK", "DE", "FR", "IT"]:
        return "INTERNATIONAL"
    return "UNKNOWN"
