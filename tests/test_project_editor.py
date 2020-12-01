import settings
from pageobjects.home_menu_page import HomeMenu
from pageobjects.login_page import LoginPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure

from pageobjects.project_editor_page import ProjectEditor


class TestLogin:
    title = "PROJECTS"

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)
        self.home_menu = HomeMenu(self.driver)
        self.project_editor = ProjectEditor(self.driver)
        self.login_page.login_to_cameraiq(settings.get_login(), settings.get_password())

    @allure.tag("Projects page")
    @allure.title("Create Project")
    def test_new_project(self):
        self.home_menu.open_projects()
        self.project_editor.click_create_project()
        assert self.project_editor.get_project_info() is True

    @allure.tag("Project editor")
    @allure.title("Rename Project")
    def test_rename_project(self):
        self.home_menu.open_projects()
        self.project_editor.click_create_project()
        self.project_editor.click_project_action_button()
        self.project_editor.click_rename_project()
        assert self.project_editor.get_project_info() is True

    def teardown_method(self):
        self.driver.close()
