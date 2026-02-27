from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int

@dataclass
class OrderItem:
    product: Product
    quantity: int

    def total_price(self):
        return self.product.price * self.quantity

@dataclass
class Order:
    id: int
    customer_email: str
    items: List[OrderItem]
    created_at: datetime = None
    status: str = "pending"

    def calculate_total(self):
        return sum(item.total_price() for item in self.items)

    def item_count(self):
        return sum(item.quantity for item in self.items)
