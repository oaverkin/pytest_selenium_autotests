import time
from selenium.webdriver.common.by import By

import settings
from pageobjects.base_page import BasePage
import allure

# login page
login_form_id = "//input[@name='email']"
password_form_id = "//input[@name='password']"
next_button_id = "//span[normalize-space(text()) = 'Next']"
login_error = "Invalid email or password"
# home menu
menu_templates_link = "//div[normalize-space(text()) = 'Templates']"
menu_projects_link = "//div[normalize-space(text()) = 'Projects']"
menu_publish_manager_link = "//div[normalize-space(text()) = 'Publish Manager']"
menu_resources_link = "//div[normalize-space(text()) = 'Resources']"
menu_settings_link = "//div[normalize-space(text()) = 'Settings']"
logout_menu_link = "//div[@class='logout-control']"
login_error_message = "//span[text()='Invalid email or password']"


class LoginPage(BasePage):

    @allure.step
    def get_title(self):
        return self.driver.title

    @allure.step
    def get_error_message(self, message):
        for i in range(10):
            time.sleep(0.3)
            if self.driver.find_elements(By.XPATH, f"//span[text()='{message}']"):
                return True
        return False

    @allure.step
    def login_with_credentials(self, login, password):
        self.open(settings.get_url())
        self.type_to_elem(login_form_id, By.XPATH, login)
        self.type_to_elem(password_form_id, By.XPATH, password)
        self.click_elem(next_button_id, By.XPATH)

    @allure.step
    def login_to_cameraiq(self):
        self.open(settings.get_url())
        self.type_to_elem(login_form_id, By.XPATH, settings.get_login())
        self.type_to_elem(password_form_id, By.XPATH, settings.get_password())
        self.click_elem(next_button_id, By.XPATH)

    @allure.step
    def on_page(self):
        return self.at_page(menu_templates_link)

    @allure.step
    def open(self, url):
        self.driver.get(url)
        return self
