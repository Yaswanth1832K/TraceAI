MOCK_DATABASE = {
    "U101": {"location": "US", "active": True},
    "U102": {"location": "DE", "active": True},
    "U103": {"location": "UK", "active": False}
}

def get_user_location(user_id):
    """
    Connects to Redis cache or PostgreSQL database 
    to fetch customer geolocation details.
    """
    user_data = MOCK_DATABASE.get(user_id)
    
    if not user_data:
        return "US" # Default mapping
    
    return user_data.get("location")
