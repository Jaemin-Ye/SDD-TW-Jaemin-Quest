"""Discount abstract class and implementations"""
from abc import ABC, abstractmethod
from typing import List
from src.order_item import OrderItem


class Discount(ABC):
    """折扣抽象類別"""
    
    @abstractmethod
    def apply(self, items: List[OrderItem]) -> tuple[List[OrderItem], float]:
        """
        套用折扣
        
        Args:
            items: 訂單項目列表
            
        Returns:
            tuple: (更新後的訂單項目列表, 折扣金額)
        """
        pass


class ThresholdDiscount(Discount):
    """門檻折扣 - 當訂單金額達到門檻時，給予固定折扣"""
    
    def __init__(self, threshold: float, discount_amount: float):
        """
        初始化門檻折扣
        
        Args:
            threshold: 門檻金額
            discount_amount: 折扣金額
        """
        self.threshold = threshold
        self.discount_amount = discount_amount
    
    def apply(self, items: List[OrderItem]) -> tuple[List[OrderItem], float]:
        """
        套用門檻折扣
        
        如果訂單總金額達到門檻，則給予折扣
        """
        # 計算原始金額
        total = sum(item.product.unit_price * item.quantity for item in items)
        
        # 判斷是否達到門檻
        if total >= self.threshold:
            return items, self.discount_amount
        else:
            return items, 0.0


class BuyOneGetOneDiscount(Discount):
    """買一送一折扣 - 針對特定類別的商品，買一送一"""
    
    def __init__(self, category: str):
        """
        初始化買一送一折扣
        
        Args:
            category: 適用的商品類別
        """
        self.category = category
    
    def apply(self, items: List[OrderItem]) -> tuple[List[OrderItem], float]:
        """
        套用買一送一折扣
        
        針對符合類別的每個商品項目，贈送 1 個相同商品
        （不是數量加倍，而是每個商品項目贈送 1 個）
        """
        new_items = []
        
        for item in items:
            if item.product.category == self.category:
                # 符合買一送一條件，原數量 + 贈送 1 個
                new_item = OrderItem(item.product, item.quantity + 1)
                new_items.append(new_item)
            else:
                # 不符合條件，保持原樣
                new_items.append(item)
        
        # 買一送一不影響金額（贈品不收費）
        return new_items, 0.0

