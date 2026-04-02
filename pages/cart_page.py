from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def proceed_to_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()