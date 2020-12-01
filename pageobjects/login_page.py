import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import settings
import allure


class LoginPage:
    login_input = (By.XPATH, "//input[@name='email']")
    password_input = (By.XPATH, "//input[@name='password']")
    next_button = (By.XPATH, "//span[normalize-space(text()) = 'Next']")
    forgot_password_link = (By.XPATH, "//a[normalize-space(text()) = 'Forgot Password?']")
    reset_password_title = (By.XPATH, "//p[normalize-space(text()) = 'Reset password']")
    forgot_email_link = (By.XPATH, "//a[normalize-space(text()) = 'Forgot Email?']")
    reset_password_input = (By.XPATH, "//input[@type='email']")

    driver = None

    def __init__(self, driver):
        self.driver = driver

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
    def login_to_cameraiq(self, login=None, password=None):
        self.open(settings.get_url())
        self.driver.find_element(*self.login_input).send_keys(login)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.next_button).click()

    @allure.step
    def at_page(self):
        try:
            elem = WebDriverWait(self.driver, 10) \
                .until(EC.presence_of_element_located(self.login_input))
            return elem.is_displayed()
        except TimeoutException:
            return False

    @allure.step
    def click_on_forgot_password_link(self):
        self.driver.find_element(*self.forgot_password_link).click()

    @allure.step
    def forgot_password_link_is_displayed(self):
        elem = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.forgot_password_link))
        return elem.is_displayed()

    @allure.step
    def reset_password_title_is_displayed(self):
        elem = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.reset_password_title))
        return elem.is_displayed()

    @allure.step
    def forgot_email_link_is_displayed(self):
        elem = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.forgot_email_link))
        return elem.is_displayed()

    @allure.step
    def reset_password_input_is_displayed(self):
        elem = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.reset_password_input))
        return elem.is_displayed()

    @allure.step
    def open(self, url):
        self.driver.get(url)
        return self
