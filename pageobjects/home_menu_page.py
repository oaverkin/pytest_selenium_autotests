import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomeMenu:
    templates = (By.XPATH, "//div[normalize-space(text()) = 'Templates']")
    projects = (By.XPATH, "//div[normalize-space(text()) = 'Projects']")
    publish = (By.XPATH, "//div[normalize-space(text()) = 'Publish Manager']")
    resources = (By.XPATH, "//div[normalize-space(text()) = 'Resources']")
    settings = (By.XPATH, "//div[normalize-space(text()) = 'Settings']")
    logout_menu = (By.XPATH, "//div[@class='logout-control']")
    logout_button = (By.XPATH, "//button[contains(@class, 'btn-logout')]")

    driver = None

    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def log_out(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.logout_menu)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logout_button)).click()

    @allure.step
    def open_projects(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.projects)).click()

    @allure.step
    def at_page(self):
        try:
            elem = WebDriverWait(self.driver, 10) \
                .until(EC.presence_of_element_located(self.templates))
            return elem.is_displayed()
        except TimeoutException:
            return False
