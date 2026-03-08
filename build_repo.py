import os

files = {
    "mega_ecommerce_app/__init__.py": "",
    "mega_ecommerce_app/main.py": """\
import argparse
from engine.context import initialize_app
from engine.workflow import CheckoutWorkflow

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", type=int, default=1, help="Error scenario to trigger (1, 2, or 3)")
    args = parser.parse_args()

    app_context = initialize_app()
    workflow = CheckoutWorkflow(app_context)
    
    print(f"\\n=========================================")
    print(f"Starting E-Commerce Platform - Scenario {args.scenario}")
    print(f"=========================================\\n")
    workflow.run_checkout_scenario(args.scenario)

if __name__ == '__main__':
    main()
""",
    "mega_ecommerce_app/engine/__init__.py": "",
    "mega_ecommerce_app/engine/context.py": """\
from services.inventory_mgmt import InventoryService
from services.payment_gateway import PaymentGateway
from services.shipping_calculator import ShippingCalculator
from services.tax_service import TaxService
from dal.db_context import DatabaseContext

class AppContext:
    def __init__(self):
        self.db = DatabaseContext()
        self.inventory = InventoryService(self.db)
        self.payment = PaymentGateway()
        self.shipping = ShippingCalculator()
        self.tax = TaxService()

def initialize_app():
    return AppContext()
""",
    "mega_ecommerce_app/engine/workflow.py": """\
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
""",
    "mega_ecommerce_app/models/__init__.py": "",
    "mega_ecommerce_app/models/user.py": """\
class User:
    def __init__(self, user_id, name, country):
        self.user_id = user_id
        self.name = name
        self.country = country
""",
    "mega_ecommerce_app/models/order.py": """\
class Order:
    def __init__(self, order_id, user):
        self.order_id = order_id
        self.user = user
        self.items = []
        self.shipping_cost = 0.0
        self.tax_amount = 0.0
        self.discount_code = None
        self.payment_metadata = {}

    def add_item(self, item_dict):
        self.items.append(item_dict)

    def apply_discount_code(self, code):
        self.discount_code = code

    def set_shipping_cost(self, cost):
        self.shipping_cost = cost

    def set_tax_amount(self, tax):
        self.tax_amount = tax

    def subtotal(self):
        # If 'qty' is a string ("one"), multiplying string by float (9.99) throws TypeError
        # This perfectly simulates untyped/unsanitized data bypassing validations
        return sum(item['qty'] * item['price'] for item in self.items)

    def total(self):
        return self.subtotal() + self.shipping_cost + self.tax_amount
""",
    "mega_ecommerce_app/services/__init__.py": "",
    "mega_ecommerce_app/services/inventory_mgmt.py": """\
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
""",
    "mega_ecommerce_app/services/tax_service.py": """\
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
""",
    "mega_ecommerce_app/services/shipping_calculator.py": """\
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
""",
    "mega_ecommerce_app/services/payment_gateway.py": """\
from api_clients.stripe_client import StripeMockClient

class PaymentGateway:
    def __init__(self):
        self.client = StripeMockClient()

    def charge(self, user, amount, metadata):
        # Because we didn't sanitize 'payment_metadata', 'payment_method_id' is missing
        token = metadata.get("payment_method_id")
        
        response = self.client.process_transaction(user.user_id, amount, token)
        return response
""",
    "mega_ecommerce_app/dal/__init__.py": "",
    "mega_ecommerce_app/dal/db_context.py": """\
class DatabaseContext:
    def __init__(self):
        self.connected = True

    def query(self, sql):
        # Mock database response
        return [100] 
""",
    "mega_ecommerce_app/utils/__init__.py": "",
    "mega_ecommerce_app/utils/vat_calculator.py": """\
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
""",
    "mega_ecommerce_app/utils/geo_mapper.py": """\
def get_shipping_zone(country_code):
    if country_code in ["US", "CA"]:
        return "DOMESTIC"
    elif country_code in ["UK", "DE", "FR", "IT"]:
        return "INTERNATIONAL"
    return "UNKNOWN"
""",
    "mega_ecommerce_app/api_clients/__init__.py": "",
    "mega_ecommerce_app/api_clients/stripe_client.py": """\
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
"""
}

def create_structure():
    for filepath, content in files.items():
        dir_name = os.path.dirname(filepath)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    print("Mega project created successfully.")

if __name__ == '__main__':
    create_structure()
