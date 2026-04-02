
import os
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service


@pytest.fixture
def driver():
    # 判断是否在 CI 环境中运行（GitHub Actions 会自动设置 CI=true）
    if os.getenv('CI'):
        # CI 环境中，EdgeDriver 已经在 PATH 里，直接创建驱动
        driver = webdriver.Edge()
    else:
        # 本地开发：使用 webdriver-manager 自动下载匹配的驱动
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)

    driver.maximize_window()
    yield driver
    driver.quit()
    '''yield 使得该函数成为一个生成器。
    当作为 pytest fixture 使用时，yield 之前的代码属于 setup 阶段（启动浏览器），
    yield 返回的 driver 对象会传递给测试函数；测试执行完毕后，会继续执行 yield 之后的代码。'''