import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password,expected_error", [
    ("standard_user", "wrongpass", "Username and password do not match any user in this service"),
    ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
    ("", "", "Username is required"),
])
def test_login_with_invalid_credentials(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    error = login_page.get_error_message()
    assert expected_error in error