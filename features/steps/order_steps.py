"""Step definitions for order feature"""
from behave import given, when, then
from src.product import Product
from src.order_item import OrderItem
from src.order_service import OrderService
from src.discount import ThresholdDiscount, BuyOneGetOneDiscount


@given('no promotions are applied')
def step_no_promotions(context):
    """設定無促銷活動"""
    context.order_service = OrderService()
    context.promotions = []


@given('the threshold discount promotion is configured:')
def step_threshold_discount_configured(context):
    """設定門檻折扣促銷"""
    # 如果還沒有 order_service，則創建一個
    if not hasattr(context, 'order_service'):
        context.order_service = OrderService()
    
    # 從表格中讀取門檻折扣設定
    for row in context.table:
        threshold = float(row['threshold'])
        discount = float(row['discount'])
        context.order_service.add_discount(ThresholdDiscount(threshold, discount))


@given('the buy one get one promotion for cosmetics is active')
def step_bogo_cosmetics_active(context):
    """設定化妝品買一送一促銷"""
    # 如果還沒有 order_service，則創建一個
    if not hasattr(context, 'order_service'):
        context.order_service = OrderService()
    
    context.order_service.add_discount(BuyOneGetOneDiscount('cosmetics'))


@when('a customer places an order with:')
def step_customer_places_order(context):
    """客戶下訂單"""
    items = []
    
    for row in context.table:
        product_name = row['productName']
        quantity = int(row['quantity'])
        unit_price = float(row['unitPrice'])
        category = row.get('category', '')
        
        product = Product(name=product_name, unit_price=unit_price, category=category)
        order_item = OrderItem(product=product, quantity=quantity)
        items.append(order_item)
    
    context.order = context.order_service.checkout(items)


@then('the order summary should be:')
def step_order_summary_should_be(context):
    """驗證訂單摘要"""
    row = context.table[0]
    
    if 'totalAmount' in row.headings:
        expected_total = float(row['totalAmount'])
        assert context.order.total_amount == expected_total, \
            f"Expected total amount {expected_total}, but got {context.order.total_amount}"
    
    if 'originalAmount' in row.headings:
        expected_original = float(row['originalAmount'])
        assert context.order.original_amount == expected_original, \
            f"Expected original amount {expected_original}, but got {context.order.original_amount}"
    
    if 'discount' in row.headings:
        expected_discount = float(row['discount'])
        assert context.order.discount == expected_discount, \
            f"Expected discount {expected_discount}, but got {context.order.discount}"


@then('the customer should receive:')
def step_customer_should_receive(context):
    """驗證客戶收到的商品"""
    expected_items = {}
    for row in context.table:
        product_name = row['productName']
        quantity = int(row['quantity'])
        expected_items[product_name] = quantity
    
    actual_items = {}
    for item in context.order.items:
        product_name = item.product.name
        if product_name in actual_items:
            actual_items[product_name] += item.quantity
        else:
            actual_items[product_name] = item.quantity
    
    assert actual_items == expected_items, \
        f"Expected items {expected_items}, but got {actual_items}"

