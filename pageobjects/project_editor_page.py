from datetime import datetime
from time import sleep

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProjectEditor:
    CREATE_PROJECT = (By.XPATH, "//div[contains(@class, 'create-project-card')]")
    PROJECT_TITLE = (By.XPATH, "//div[normalize-space(text()) = 'PROJECTS']")
    PROJECT_INFO = (By.XPATH, "//div[normalize-space(text()) = 'Project Info']")
    LOADING_BAR_DISABLED = (By.XPATH, "//div[contains(@class, 'q-loading-bar--top') and @aria-hidden='true']")

    # project actions
    PROJECT_ACTION_BUTTON = (By.XPATH, "//input[@class='component-name']/following::button[1]")
    SAVE_AS_TEMPLATE = (By.XPATH, "//div[normalize-space(text()) = 'Save as template']")
    RENAME_LINK = (By.XPATH, "//div[normalize-space(text()) = 'Rename']")
    DELETE_LINK = (By.XPATH, "//div[normalize-space(text()) = 'Delete']")
    # rename project window
    SAVE_PROJECT_BUTTON = (By.XPATH, "//span[normalize-space(text()) = 'Save']")
    CANCEL_BUTTON = (By.XPATH, "//span[normalize-space(text()) = 'Cancel']")
    RENAME_INPUT_FIELD = (By.XPATH, "//input[@name='rename']")
    # delete project window
    DELETE_PROJECT_BUTTON = (By.XPATH, "//span[normalize-space(text()) = 'Delete']")

    driver = None

    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def create_project(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOADING_BAR_DISABLED))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CREATE_PROJECT)).click()

    @allure.step
    def get_project_info(self):
        elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PROJECT_INFO))
        return elem.is_displayed()

    @allure.step
    def get_project_name(self):
        new_project_name = self.driver.title
        return new_project_name

    @allure.step
    def click_project_action_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PROJECT_ACTION_BUTTON))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PROJECT_ACTION_BUTTON)).click()

    @allure.step
    def click_rename_project_link(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.RENAME_LINK)).click()

    @allure.step
    def click_delete_project_link(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.DELETE_LINK)).click()

    @allure.step
    def click_delete_project_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.DELETE_PROJECT_BUTTON))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.DELETE_PROJECT_BUTTON))
        self.driver.find_element(*self.DELETE_PROJECT_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOADING_BAR_DISABLED))

    @allure.step
    def add_new_project_name(self, project_name):
        elem = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.RENAME_INPUT_FIELD))
        elem.send_keys(Keys.BACKSPACE)
        sleep(0.5)
        elem.send_keys(project_name)

    @allure.step
    def click_save_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SAVE_PROJECT_BUTTON)).click()

    @allure.step
    def rename_project(self):
        random = datetime.now().strftime("%M%S")
        new_project_name = f"Autobot_{random}"
        self.click_project_action_button()
        self.click_rename_project_link()
        self.add_new_project_name(new_project_name)
        self.click_save_button()
        return new_project_name

    @allure.step
    def delete_project(self):
        self.click_project_action_button()
        self.click_delete_project_link()
        self.click_delete_project_button()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOADING_BAR_DISABLED))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CREATE_PROJECT))

    def wait_for_loading_bar_disappear(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOADING_BAR_DISABLED))

    def at_page(self):
        try:
            elem = WebDriverWait(self.driver, 10) \
                .until(EC.presence_of_element_located(self.PROJECT_TITLE))
            return elem.is_displayed()
        except TimeoutException:
            return False
