"""Order entity"""
from typing import List
from src.order_item import OrderItem


class Order:
    """訂單實體類別"""
    
    def __init__(self):
        """初始化訂單"""
        self.items: List[OrderItem] = []
        self.original_amount: float = 0.0
        self.discount: float = 0.0
        self.total_amount: float = 0.0
    
    def add_item(self, item: OrderItem):
        """新增訂單項目"""
        self.items.append(item)

