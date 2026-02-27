from models import Product, Order, OrderItem
from typing import List, Dict, Optional

# Simulated in-memory database
_products: Dict[int, Product] = {
    1: Product(id=1, name="Laptop", price=999.99, stock=10),
    2: Product(id=2, name="Mouse", price=29.99, stock=50),
    3: Product(id=3, name="Keyboard", price=79.99, stock=30),
}

_orders: Dict[int, Order] = {}
_order_counter = 1

def get_product(product_id: int) -> Optional[Product]:
    return _products.get(product_id)

def get_all_products() -> List[Product]:
    return list(_products.values())

def save_order(order: Order) -> Order:
    global _order_counter
    order.id = _order_counter
    _order_counter += 1
    _orders[order.id] = order
    return order

def get_order(order_id: int) -> Optional[Order]:
    return _orders.get(order_id)

def get_orders_by_email(email: str) -> List[Order]:
    # BUG: comparing Order object directly instead of its attribute
    return [o for o in _orders.values() if o == email]

def update_product_stock(product_id: int, quantity_sold: int):
    product = _products.get(product_id)
    if product:
        product.stock -= quantity_sold
