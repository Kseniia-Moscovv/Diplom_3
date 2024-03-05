import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage


class CommonSteps(MainPage, LoginPage):
    @allure.step('Go to reset page')
    def go_to_reset_page(self):
        self.click_on_profile_button()
        self.wait_for_login_page()
