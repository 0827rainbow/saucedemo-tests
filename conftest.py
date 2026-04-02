import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

@pytest.fixture
def driver():
    # 手动指定 EdgeDriver 路径
    service = Service(executable_path="E:\\TestSturdy\\saucedemo_tests\\drivers\\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    '''yield 使得该函数成为一个生成器。
    当作为 pytest fixture 使用时，yield 之前的代码属于 setup 阶段（启动浏览器），
    yield 返回的 driver 对象会传递给测试函数；测试执行完毕后，会继续执行 yield 之后的代码。'''
    driver.quit()