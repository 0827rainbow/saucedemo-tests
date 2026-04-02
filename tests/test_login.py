from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url     #断言

def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    error = login_page.get_error_message()
    assert "Sorry, this user has been locked out." in error


import allure


@allure.feature("登录功能")
@allure.story("正常登录")
def test_valid_login(driver):
    with allure.step("打开登录页面"):
        login_page = LoginPage(driver)
        login_page.open()
    with allure.step("输入用户名和密码"):
        login_page.login("standard_user", "secret_sauce")
    with allure.step("验证登录成功"):
        assert "inventory.html" in driver.current_url