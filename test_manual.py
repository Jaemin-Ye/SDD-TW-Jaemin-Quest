"""Manual test script to verify the code works"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.product import Product
from src.order_item import OrderItem
from src.order_service import OrderService


def test_single_product_without_promotions():
    """Test the first scenario manually"""
    print("Testing: Single product without promotions")
    
    # Given no promotions are applied
    order_service = OrderService()
    
    # When a customer places an order with T-shirt (1, 500)
    product = Product(name="T-shirt", unit_price=500)
    order_item = OrderItem(product=product, quantity=1)
    order = order_service.checkout([order_item])
    
    # Then the order summary should be totalAmount: 500
    print(f"  Total Amount: {order.total_amount} (expected: 500)")
    
    # And the customer should receive T-shirt: 1
    print(f"  Items in order: {len(order.items)}")
    for item in order.items:
        print(f"    - {item.product.name}: {item.quantity}")
    
    # Check assertions
    assert order.total_amount == 500, f"Expected 500, got {order.total_amount}"
    assert len(order.items) == 1, f"Expected 1 item, got {len(order.items)}"
    assert order.items[0].product.name == "T-shirt", f"Expected T-shirt"
    assert order.items[0].quantity == 1, f"Expected quantity 1"
    
    print("  ✓ Test passed!\n")


if __name__ == "__main__":
    try:
        test_single_product_without_promotions()
        print("All tests passed!")
    except AssertionError as e:
        print(f"✗ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

