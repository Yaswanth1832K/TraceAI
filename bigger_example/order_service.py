from models import Order, OrderItem, Product
from database import get_product, save_order, update_product_stock, get_orders_by_email
from datetime import datetime
from typing import List, Dict

class InsufficientStockError(Exception):
    pass

class ProductNotFoundError(Exception):
    pass

def create_order(customer_email: str, cart: List[Dict]) -> Order:
    """
    cart: list of {"product_id": int, "quantity": int}
    """
    order_items = []

    for item in cart:
        product = get_product(item["product_id"])
        if product is None:
            raise ProductNotFoundError(f"Product {item['product_id']} not found")

        if product.stock < item["quantity"]:
            raise InsufficientStockError(
                f"Only {product.stock} units of {product.name} available"
            )

        order_items.append(OrderItem(product=product, quantity=item["quantity"]))

    order = Order(
        id=0,
        customer_email=customer_email,
        items=order_items,
        created_at=datetime.now()
    )

    saved_order = save_order(order)

    # Update stock for each item
    for item in cart:
        update_product_stock(item["product_id"], item["quantity"])

    return saved_order


def get_order_history(email: str) -> List[Order]:
    return get_orders_by_email(email)


def apply_discount(order: Order, discount_percent: float) -> float:
    """Returns discounted total."""
    total = order.calculate_total()
    # BUG: discount_percent treated as decimal already (e.g. 10 means 1000% off)
    discount_amount = total * discount_percent
    return total - discount_amount


def get_order_summary(order: Order) -> Dict:
    return {
        "order_id": order.id,
        "customer": order.customer_email,
        "items": order.item_count(),
        "total": f"${order.calculate_total():.2f}",
        "status": order.status,
        "created_at": order.created_at.strftime("%Y-%m-%d %H:%M") if order.created_at else None
    }
