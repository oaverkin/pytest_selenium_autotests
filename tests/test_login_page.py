import settings
from pageobjects.base_page import BasePage
from pageobjects.login_page import LoginPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure
import pytest

login_title = "CameraIQ"
template_title = "Templates"


class TestLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)
        self.base_page = BasePage(self.driver)

    @pytest.mark.ui
    @allure.tag("login")
    @allure.title("Check title")
    def test_check_title(self):
        self.login_page.open(settings.get_url())
        assert self.login_page.get_title() == login_title

    @pytest.mark.ui
    @allure.tag("login")
    @allure.title("Login with wrong password")
    def test_login_with_wrong_password(self):
        self.login_page.open(settings.get_url())
        self.login_page.login_with_credentials(settings.get_login(), "bad_password")
        assert self.login_page.get_title() == login_title
        assert self.login_page.get_error_message("Invalid email or password") is True

    @pytest.mark.ui
    @allure.tag("login")
    @allure.title("Login with wrong username")
    def test_login_with_wrong_username(self):
        self.login_page.login_with_credentials("bad_username@email.com", settings.get_password())
        assert self.login_page.get_title() == login_title
        assert self.login_page.get_error_message("Invalid email or password") is True

    @pytest.mark.ui
    @allure.tag("login")
    @allure.title("Login with correct credentials")
    def test_login_with_correct_credentials(self):
        self.login_page.login_to_cameraiq()
        assert self.login_page.on_page() is True

    def teardown_method(self):
        self.driver.close()
