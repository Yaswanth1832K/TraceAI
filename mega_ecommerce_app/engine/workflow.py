from models.order import Order
from models.user import User

class CheckoutWorkflow:
    def __init__(self, ctx):
        self.ctx = ctx

    def run_checkout_scenario(self, scenario_id):
        user = User(user_id="U8891", name="Alice Jensen", country="US")
        order = Order(order_id="ORD-992-XYZ", user=user)

        if scenario_id == 1:
            # Scenario 1: Deep Dictionary / Type Bug (TypeError deep in aggregation)
            order.add_item({"product_id": "P-101", "qty": 2, "price": 45.0})
            order.add_item({"product_id": "P-102", "qty": 1, "price": 12.5})
            # A corrupted JSON object payload is mistakenly parsed as a string quantity
            order.add_item({"product_id": "P-103", "qty": "one", "price": 9.99}) 
        
        elif scenario_id == 2:
            # Scenario 2: Mutual Recursion / Infinite Loop in tax calculator
            order.add_item({"product_id": "P-201", "qty": 1, "price": 100.0, "category": "digital"})
            user.country = "EU_VAT_ZONE"
            
        elif scenario_id == 3:
            # Scenario 3: Null Reference hidden by Exception Chaining in External Client
            order.add_item({"product_id": "P-301", "qty": 5, "price": 200.0})
            order.apply_discount_code("BROKEN_PROMO")
            
        print("[System] Validating Inventory Levels...")
        self.ctx.inventory.reserve_items(order.items)
        
        print("[System] Calculating Shipping Zone Rates...")
        shipping_cost = self.ctx.shipping.calculate(order)
        order.set_shipping_cost(shipping_cost)
        
        print("[System] Computing Regional Tax...")
        tax_amount = self.ctx.tax.compute_tax(order)
        order.set_tax_amount(tax_amount)
        
        print(f"[System] Cart Subtotal & Validation...")
        total_amt = order.total()
        
        print(f"[System] Total Amount: ${total_amt:.2f}")
        print("[System] Initiating Payment Gateway Handshake...")
        self.ctx.payment.charge(user, total_amt, order.payment_metadata)
        
        print("✅ Checkout Complete!")
