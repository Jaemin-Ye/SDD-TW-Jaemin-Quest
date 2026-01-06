"""OrderItem entity"""
from dataclasses import dataclass
from src.product import Product


@dataclass
class OrderItem:
    """訂單項目實體類別"""
    product: Product
    quantity: int

    @property
    def subtotal(self) -> float:
        """計算小計"""
        return self.product.unit_price * self.quantity

