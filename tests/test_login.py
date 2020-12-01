import settings
from pageobjects.home_menu_page import HomeMenu
from pageobjects.login_page import LoginPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure
import pytest


class TestLogin:
    login_title = "CameraIQ"
    template_title = "Templates"

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)
        self.home_menu = HomeMenu(self.driver)

    @allure.tag("login")
    @allure.title("Check title")
    def test_check_login_page_title(self):
        self.login_page.open(settings.get_url())
        assert self.login_page.get_title() == self.login_title
        assert self.login_page.forgot_password_link_is_displayed() is True

    @allure.tag("login")
    @allure.title("Login with correct credentials")
    def test_login_to_cameraiq(self):
        self.login_page.login_to_cameraiq(settings.get_login(), settings.get_password())
        assert self.home_menu.at_page() is True

    @allure.tag("login")
    @allure.title("Login with wrong password")
    def test_login_with_wrong_password(self):
        self.login_page.open(settings.get_url())
        self.login_page.login_to_cameraiq(settings.get_login(), "bad_password")
        assert self.login_page.get_title() == self.login_title
        assert self.login_page.get_error_message("Invalid email or password") is True

    @allure.tag("login")
    @allure.title("Login with wrong username")
    def test_login_with_wrong_username(self):
        self.login_page.login_to_cameraiq("bad_username@email.com", settings.get_password())
        assert self.login_page.get_title() == self.login_title
        assert self.login_page.get_error_message("Invalid email or password") is True

    @allure.tag("login")
    @allure.title("Log out")
    def test_logout_from_cameraiq(self):
        self.login_page.login_to_cameraiq(settings.get_login(), settings.get_password())
        self.home_menu.log_out()
        assert self.login_page.at_page() is True

    @allure.tag("login")
    @allure.title("Forgot password")
    def test_forgot_password_page(self):
        self.login_page.open(settings.get_url())
        self.login_page.click_on_forgot_password_link()
        assert self.login_page.reset_password_title_is_displayed() is True
        assert self.login_page.forgot_email_link_is_displayed() is True
        assert self.login_page.reset_password_input_is_displayed() is True

    def teardown_method(self):
        self.driver.close()
