import os
import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 创建截图和日志目录
SCREENSHOT_DIR = "screenshots"
LOG_DIR = "logs"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, "test.log")),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def take_screenshot(driver, test_name):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(SCREENSHOT_DIR, filename)
    driver.save_screenshot(filepath)
    logger.error(f"Screenshot saved: {filepath}")

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--disable-extensions')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    logger.info("Browser started")
    yield driver
    driver.quit()
    logger.info("Browser closed")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            take_screenshot(driver, item.name)
            logger.error(f"Test '{item.name}' failed.")