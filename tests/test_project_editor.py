import pytest

import settings
from pageobjects.home_menu_page import HomeMenu
from pageobjects.login_page import LoginPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure

from pageobjects.project_editor_page import ProjectEditor


class TestProjectEditor:
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
        self.project_editor.create_project()
        assert self.project_editor.get_project_info() is True
        self.project_editor.delete_project()

    @pytest.mark.xfail(reason="CIB-2936: Frontend: Project Editor: Project action window should be closed when user "
                              "renamed project")
    @allure.tag("Project editor")
    @allure.title("Rename Project")
    def test_rename_project(self):
        self.home_menu.open_projects()
        self.project_editor.create_project()
        new_project_name = self.project_editor.rename_project()
        assert self.project_editor.get_project_name() == new_project_name
        self.project_editor.delete_project()

    def teardown_method(self):
        self.driver.close()
