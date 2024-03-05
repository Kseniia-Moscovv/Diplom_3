import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePageStellarBurger


class LoginPage(BasePageStellarBurger):
    @allure.step('Go to reset password page')
    def click_on_reset_password_button(self):
        self.click_on_element(LoginPageLocators.reset_password_button)

    @allure.step('Wait to load login page')
    def wait_for_login_page(self):
        self.visibility_of_element_located(LoginPageLocators.heading_login_page)

    @allure.step('Get login page heading text')
    def get_login_page_heading(self):
        return self.get_element_text(LoginPageLocators.heading_login_page)
