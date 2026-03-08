import hashlib

class StripeMockClient:
    def process_transaction(self, customer_id, amount, token):
        try:
            # Token is None, causing .encode() to fail with AttributeError
            payload_hash = hashlib.sha256(token.encode('utf-8')).hexdigest()
        except AttributeError as e:
            # Exception Chaining: Wraps the original error masking the core issue
            raise RuntimeError(f"Payment processing failed for {customer_id}: Critical gateway error") from e
            
        return {"status": "success", "hash": payload_hash}
