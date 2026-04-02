from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def fill_info(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def finish_order(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def get_success_message(self) -> str:
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        ).text