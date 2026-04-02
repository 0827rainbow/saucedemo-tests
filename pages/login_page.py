from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # 页面元素定位器
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"


# open 方法只是对这个操作做了简单的封装，
# 使调用者只需 login_page.open() 就能打开登录页面，而无需关心具体的 URL。

    def open(self):
        self.driver.get(self.url)

    def login(self, username: str, password: str):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # EC是 expected_conditions模块的常见别名，提供预定义的条件。
    # visibility_of_element_located条件：等待元素在DOM中出现并且可见（宽高 > 0，且未隐藏）。
    def get_error_message(self) -> str:
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            ).text
        except:
            return ""