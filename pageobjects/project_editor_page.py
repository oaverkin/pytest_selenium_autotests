from datetime import datetime

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProjectEditor:
    create_project = (By.XPATH, "//div[contains(@class, 'create-project-card')]")
    projects_title = (By.XPATH, "//div[normalize-space(text()) = 'PROJECTS']")
    project_info = (By.XPATH, "//div[normalize-space(text()) = 'Project Info']")

    # project actions
    project_action_button = (By.XPATH, "//input[@class='component-name']/following::button[1]")
    save_as_template = (By.XPATH, "//div[normalize-space(text()) = 'Save as template']")
    rename = (By.XPATH, "//div[normalize-space(text()) = 'Rename']")
    delete = (By.XPATH, "//div[normalize-space(text()) = 'Delete']")

    driver = None

    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def click_create_project(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.create_project)).click()

    @allure.step
    def get_project_info(self):
        elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.project_info))
        return elem.is_displayed()

    @allure.step
    def click_project_action_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.project_action_button)).click()

    @allure.step
    def click_rename_project(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.rename)).click()

    @allure.step
    def rename_project(self):
        random = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        project_name = f"Autobot{random}"

        return project_name

    def at_page(self):
        try:
            elem = WebDriverWait(self.driver, 10) \
                .until(EC.presence_of_element_located(self.projects_title))
            return elem.is_displayed()
        except TimeoutException:
            return False
