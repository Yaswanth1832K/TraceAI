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
