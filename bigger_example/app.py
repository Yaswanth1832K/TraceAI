from order_service import create_order, get_order_history, apply_discount, get_order_summary
from database import get_all_products

def display_products():
    products = get_all_products()
    print("\n--- Available Products ---")
    for p in products:
        print(f"  [{p.id}] {p.name} - ${p.price:.2f} (stock: {p.stock})")

def place_sample_order():
    cart = [
        {"product_id": 1, "quantity": 1},  # 1x Laptop
        {"product_id": 2, "quantity": 2},  # 2x Mouse
    ]
    order = create_order("user@example.com", cart)
    print(f"\nOrder placed! Summary:")
    print(get_order_summary(order))
    return order

def test_discount(order):
    # BUG TRIGGER: passing 10 instead of 0.10 for 10% discount
    discounted = apply_discount(order, 10)
    print(f"\nDiscounted total: ${discounted:.2f}")

def test_order_history():
    # BUG TRIGGER: comparing Order object to string
    history = get_order_history("user@example.com")
    print(f"\nOrder history: {history}")

if __name__ == "__main__":
    display_products()
    order = place_sample_order()
    test_discount(order)
    test_order_history()
