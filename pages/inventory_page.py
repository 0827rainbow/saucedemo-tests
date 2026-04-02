from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    # 商品标题定位（用来判断是否在商品页）
    TITLE = (By.CLASS_NAME, "title")
    # 第一个商品的“添加到购物车”按钮（这里用动态定位，实际可以用 class 或 data-test）
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def is_on_inventory_page(self) -> bool:
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.TITLE)
            ).is_displayed()
        except:
            return False

    def add_first_item_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BTN).click()

    def go_to_cart(self):
        self.driver.find_element(*self.SHOPPING_CART).click()