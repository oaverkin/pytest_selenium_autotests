
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomeMenu:
    menu_templates = (By.XPATH, "//div[normalize-space(text()) = 'Templates']")
    menu_projects = "//div[normalize-space(text()) = 'Projects']"
    menu_publish_manager = "//div[normalize-space(text()) = 'Publish Manager']"
    menu_resources = "//div[normalize-space(text()) = 'Resources']"
    menu_settings = "//div[normalize-space(text()) = 'Settings']"
    logout_menu = (By.XPATH, "//div[@class='logout-control']")
    logout_button = (By.XPATH, "//button[contains(@class, 'btn-logout')]")
    login_title = (By.XPATH, "//title[normalize-space(text()) = 'CameraIQ']")

    driver = None

    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def log_out(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.logout_menu)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logout_button)).click()

    def at_page(self):
        try:
            elem = WebDriverWait(self.driver, 10) \
                .until(EC.presence_of_element_located(self.menu_templates))
            return elem.is_displayed()
        except TimeoutException:
            return False
