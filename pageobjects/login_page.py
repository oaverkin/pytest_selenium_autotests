import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import settings
import allure


class LoginPage:
    LOGIN_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    NEXT_BUTTON = (By.XPATH, "//span[normalize-space(text()) = 'Next']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[normalize-space(text()) = 'Forgot Password?']")
    RESET_PASSWORD_TITLE = (By.XPATH, "//p[normalize-space(text()) = 'Reset password']")
    FORGOT_EMAIL_LINK = (By.XPATH, "//a[normalize-space(text()) = 'Forgot Email?']")
    RESET_PASSWORD_INPUT = (By.XPATH, "//input[@type='email']")

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
        self.driver.find_element(*self.LOGIN_INPUT).send_keys(login)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.NEXT_BUTTON).click()

    @allure.step
    def at_page(self):
        try:
            elem = WebDriverWait(self.driver, 10) \
                .until(EC.presence_of_element_located(self.LOGIN_INPUT))
            return elem.is_displayed()
        except TimeoutException:
            return False

    @allure.step
    def click_on_forgot_password_link(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()

    @allure.step
    def forgot_password_link_is_displayed(self):
        elem = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.FORGOT_PASSWORD_LINK))
        return elem.is_displayed()

    @allure.step
    def reset_password_title_is_displayed(self):
        elem = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.RESET_PASSWORD_TITLE))
        return elem.is_displayed()

    @allure.step
    def forgot_email_link_is_displayed(self):
        elem = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.FORGOT_EMAIL_LINK))
        return elem.is_displayed()

    @allure.step
    def reset_password_input_is_displayed(self):
        elem = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.RESET_PASSWORD_INPUT))
        return elem.is_displayed()

    @allure.step
    def open(self, url):
        self.driver.get(url)
        return self
