"""Discount abstract class and implementations"""
from abc import ABC, abstractmethod
from typing import List
from src.order_item import OrderItem
from src.order import Order
from src.product import Product


class Discount(ABC):
    """折扣抽象類別"""
    
    @abstractmethod
    def apply(self, order: Order) -> Order:
        """套用折扣到訂單
        
        Args:
            order: 訂單物件
            
        Returns:
            Order: 套用折扣後的訂單
        """
        pass


class ThresholdDiscount(Discount):
    """門檻折扣 - 當訂單金額達到門檻時，給予固定折扣"""
    
    def __init__(self, threshold: float, discount_amount: float):
        """初始化門檻折扣
        
        Args:
            threshold: 門檻金額
            discount_amount: 折扣金額
        """
        self.threshold = threshold
        self.discount_amount = discount_amount
    
    def apply(self, order: Order) -> Order:
        """套用門檻折扣
        
        如果訂單總金額達到門檻，則給予折扣
        """
        current_subtotal = sum(item.subtotal for item in order.items)
        if current_subtotal >= self.threshold:
            order.discount += self.discount_amount
            order.total_amount -= self.discount_amount
        return order


class BuyOneGetOneDiscount(Discount):
    """買一送一折扣 - 針對特定類別的商品，買一送一"""
    
    def __init__(self, category: str):
        """初始化買一送一折扣
        
        Args:
            category: 適用的商品類別
        """
        self.category = category
    
    def apply(self, order: Order) -> Order:
        """套用買一送一折扣
        
        針對符合類別的每個商品項目，贈送 1 個相同商品
        贈品不計入金額，但會增加客戶收到的數量
        """
        new_items = []
        for item in order.items:
            new_items.append(item)  # Keep original item
            if item.product.category == self.category:
                # Add a free item for each item in the category
                new_items.append(OrderItem(product=item.product, quantity=1))
        order.items = new_items
        # Original amount stays the same (free items don't add cost)
        # Total amount stays the same
        return order
