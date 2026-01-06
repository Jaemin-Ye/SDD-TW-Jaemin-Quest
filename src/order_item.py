"""OrderItem entity"""
from src.product import Product


class OrderItem:
    """訂單項目實體類別"""
    
    def __init__(self, product: Product, quantity: int):
        """
        初始化訂單項目
        
        Args:
            product: 商品
            quantity: 數量
        """
        if quantity <= 0:
            raise ValueError("數量必須大於 0")
        
        self.product = product
        self.quantity = quantity

