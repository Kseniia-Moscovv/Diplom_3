import allure

from locators.reset_password_page_locators import ResetPassPageLocators
from pages.base_page import BasePageStellarBurger


class ResetPasswordPage(BasePageStellarBurger):
    @allure.step('Wait to load reset password page')
    def wait_for_reset_pass_heading(self):
        self.visibility_of_element_located(ResetPassPageLocators.heading_reset_password_page)

    @allure.step('Get reset password heading')
    def get_reset_pass_heading(self):
        return self.get_element_text(ResetPassPageLocators.heading_reset_password_page)

    @allure.step('Input email for reset password')
    def input_email(self, email):
        self.type_input_text(ResetPassPageLocators.email_input, email)

    @allure.step('Click to reset password button')
    def click_on_reset_password_button(self):
        self.click_on_element(ResetPassPageLocators.reset_button)

    @allure.step('Wait to input password')
    def wait_for_input_pass(self):
        self.visibility_of_element_located(ResetPassPageLocators.password_input)

    @allure.step('Get password field element')
    def get_password_field_element(self):
        return self.get_element_text(ResetPassPageLocators.password_label)

    @allure.step('Input password')
    def input_pass(self, password):
        self.type_input_text(ResetPassPageLocators.password_input, password)

    @allure.step('Click to hide password button')
    def click_on_hide_password_button(self):
        self.click_on_element(ResetPassPageLocators.hide_password_button)

    @allure.step('Get password input class list')
    def get_password_input_class_list(self):
        input_container = self.find_element(ResetPassPageLocators.password_input_container)
        return self.get_attribute(input_container, 'class')
