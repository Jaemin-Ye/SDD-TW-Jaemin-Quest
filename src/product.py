"""Product entity"""


class Product:
    """商品實體類別"""
    
    def __init__(self, name: str, unit_price: float, category: str = ""):
        """
        初始化商品
        
        Args:
            name: 商品名稱
            unit_price: 單價
            category: 商品類別（如 cosmetics, apparel 等）
        """
        self.name = name
        self.unit_price = unit_price
        self.category = category

