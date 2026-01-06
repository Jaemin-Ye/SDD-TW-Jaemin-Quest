"""OrderService for handling order checkout and promotions"""
from typing import List
from src.order import Order
from src.order_item import OrderItem
from src.discount import Discount


class OrderService:
    """訂單服務類別，處理結帳與優惠邏輯"""
    
    def __init__(self):
        """初始化訂單服務"""
        self.discounts: List[Discount] = []
    
    def add_discount(self, discount: Discount):
        """新增折扣規則"""
        self.discounts.append(discount)
    
    def checkout(self, items: List[OrderItem]) -> Order:
        """
        結帳處理
        
        Args:
            items: 訂單項目列表
            
        Returns:
            Order: 處理完成的訂單
        """
        order = Order()
        
        # 加入所有訂單項目
        for item in items:
            order.add_item(item)
        
        # 套用所有折扣
        current_items = order.items
        total_discount = 0.0
        
        for discount in self.discounts:
            current_items, discount_amount = discount.apply(current_items)
            total_discount += discount_amount
        
        # 更新訂單項目（折扣可能會修改項目，例如買一送一）
        order.items = current_items
        
        # 計算金額
        original_amount = sum(
            item.product.unit_price * item.quantity 
            for item in items  # 使用原始項目計算原始金額
        )
        
        order.original_amount = original_amount
        order.discount = total_discount
        order.total_amount = original_amount - order.discount
        
        return order

