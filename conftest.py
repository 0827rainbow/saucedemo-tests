import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--disable-extensions')
    options.add_argument('--incognito')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
    '''yield 使得该函数成为一个生成器。
    当作为 pytest fixture 使用时，yield 之前的代码属于 setup 阶段（启动浏览器），
    yield 返回的 driver 对象会传递给测试函数；测试执行完毕后，会继续执行 yield 之后的代码。'''