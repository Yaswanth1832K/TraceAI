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
