import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_purchase(driver):
    # 1. 登录
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    # 2. 商品页
    inventory = InventoryPage(driver)
    assert inventory.is_on_inventory_page()
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    # 3. 购物车
    cart = CartPage(driver)
    cart.proceed_to_checkout()

    # 4. 填写信息并完成购买
    checkout = CheckoutPage(driver)
    checkout.fill_info("John", "Doe", "12345")
    checkout.finish_order()

    # 5. 验证成功消息
    success_msg = checkout.get_success_message()
    assert "Thank you for your order!" in success_msg