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
    login_error = "Invalid email or password"
    login_error_message = "//span[text()='Invalid email or password']"
    login_title = (By.XPATH, "//title[normalize-space(text()) = 'CameraIQ']")

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
    def open(self, url):
        self.driver.get(url)
        return self
