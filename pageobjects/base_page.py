import time
import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step
    def wait_for_element(self, element, selector_type: By):
        self.wait.until(EC.presence_of_element_located((selector_type, element)))
        self.wait.until(EC.visibility_of_element_located((selector_type, element)))
        self.wait.until(EC.element_to_be_clickable((selector_type, element)))

    @allure.step
    def click_elem(self, element, selector_type: By):
        self.wait.until(EC.presence_of_element_located((selector_type, element)))
        self.wait.until(EC.visibility_of_element_located((selector_type, element)))
        self.wait.until(EC.element_to_be_clickable((selector_type, element)))
        elem = self.driver.find_element(selector_type, element)
        elem.click()

    @allure.step
    def type_to_elem(self, element, selector_type: By, text, clean=True, click_enter=False, type_delay=False):
        self.wait.until(EC.presence_of_element_located((selector_type, element)))
        self.wait.until(EC.visibility_of_element_located((selector_type, element)))
        self.wait.until(EC.element_to_be_clickable((selector_type, element)))
        elem = self.driver.find_element(selector_type, element)
        elem.click()
        if clean:
            elem.clear()
        if type_delay:
            for i in text:
                elem.send_keys(i)
                time.sleep(0.1)
        elem.send_keys(text)
        if click_enter:
            elem.send_keys(Keys.ENTER)

    @allure.step
    def get_field_data(self, element, selector_type: By):
        self.wait.until(EC.presence_of_element_located((selector_type, element)))
        self.wait.until(EC.visibility_of_element_located((selector_type, element)))
        elem = self.driver.find_element(selector_type, element)
        return elem.get_attribute('value')

    @allure.step
    def at_page(self, element):
        try:
            elem = WebDriverWait(self.driver, 10) \
                .until(EC.presence_of_element_located((By.XPATH, element)))
            return elem.is_displayed()
        except TimeoutException:
            return False

    @allure.step
    def count_issues(self, element, selector_type: By):
        return self.driver.find_elements(selector_type, element)

    @allure.step
    def browser_refresh(self):
        self.driver.refresh()
