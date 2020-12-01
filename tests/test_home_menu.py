import settings
from pageobjects.home_menu_page import HomeMenu
from pageobjects.login_page import LoginPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure
import pytest


class TestLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)
        self.home_menu = HomeMenu(self.driver)

    def teardown_method(self):
        self.driver.close()
