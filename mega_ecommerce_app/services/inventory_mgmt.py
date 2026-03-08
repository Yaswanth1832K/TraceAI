class InventoryService:
    def __init__(self, db_context):
        self.db = db_context

    def reserve_items(self, items):
        for it in items:
            prod_id = it.get('product_id')
            qty = it.get('qty')
            # Mock DB fetch
            stock = self.db.query(f"SELECT stock FROM inventory WHERE product_id='{prod_id}'")
            
            # Flawed validation allows invalid data to pass deeper into the engine
            try:
                int_qty = int(qty)
            except (ValueError, TypeError):
                # We quietly pass the error to simulate logging fatigue
                continue 
