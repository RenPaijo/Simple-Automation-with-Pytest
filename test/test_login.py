import pytest
from pages.Login_pages import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:
    @pytest.mark.positivetest
    def test_positive_login(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.enter_username("aldan")  
        login_page.enter_password("Aldan123!")
        login_page.click_login_button()
        delete_button = login_page.get_delete_button()
        assert delete_button == "Delete Account"

    @pytest.mark.negativetest
    @pytest.mark.parametrize(
        "username, password, expected_error",
        [
            ("invalid_username", "valid_password", "Invalid username or password!"),
            ("valid_username", "invalid_password", "Invalid username or password!"),
            ("invalid_username", "invalid_password", "Invalid username or password!"),
        ],
    )
    def test_negative_login(self, username, password, expected_error):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()
        error_message = login_page.get_error_message()
        assert expected_error in error_message
