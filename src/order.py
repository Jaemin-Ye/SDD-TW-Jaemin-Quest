"""Order entity"""
from dataclasses import dataclass, field
from typing import List
from src.order_item import OrderItem


@dataclass
class Order:
    """訂單實體類別"""
    items: List[OrderItem] = field(default_factory=list)
    original_amount: float = 0.0
    discount: float = 0.0
    total_amount: float = 0.0

