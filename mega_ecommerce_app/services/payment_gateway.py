from api_clients.stripe_client import StripeMockClient

class PaymentGateway:
    def __init__(self):
        self.client = StripeMockClient()

    def charge(self, user, amount, metadata):
        # Because we didn't sanitize 'payment_metadata', 'payment_method_id' is missing
        token = metadata.get("payment_method_id")
        
        response = self.client.process_transaction(user.user_id, amount, token)
        return response
