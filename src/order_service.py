"""OrderService for handling order checkout and promotions"""
from typing import List
from src.order import Order
from src.order_item import OrderItem
from src.discount import Discount


class OrderService:
    """訂單服務類別，處理結帳與優惠邏輯"""
    
    def __init__(self, promotions: List[Discount] = None):
        """初始化訂單服務
        
        Args:
            promotions: 促銷活動列表
        """
        self.promotions = promotions if promotions is not None else []
    
    def checkout(self, items: List[OrderItem]) -> Order:
        """
        結帳處理
        
        Args:
            items: 訂單項目列表
            
        Returns:
            Order: 處理完成的訂單
        """
        order = Order(items=items)
        order.original_amount = sum(item.subtotal for item in items)
        order.total_amount = order.original_amount

        for promotion in self.promotions:
            order = promotion.apply(order)

        return order

