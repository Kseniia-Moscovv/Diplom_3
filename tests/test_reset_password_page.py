import allure

from constants.user_constants import UserData
from pages.common import CommonSteps
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage


class TestResetPasswordPage:
    @allure.title('Reset password link test')
    @allure.description('Go to reset password page from main page')
    def test_go_to_reset_pass_page(self, driver):
        common = CommonSteps(driver)
        login_page = LoginPage(driver)
        reset_pass_page = ResetPasswordPage(driver)

        common.go_to_reset_page()
        login_page.click_on_reset_password_button()
        reset_pass_page.wait_for_reset_pass_heading()

        actual = reset_pass_page.get_reset_pass_heading()

        assert actual == 'Восстановление пароля'

    @allure.title('Reset password button on reset password form test')
    @allure.description('Go to reset password form')
    def test_go_to_reset_pass_form(self, driver):
        common = CommonSteps(driver)
        login_page = LoginPage(driver)
        reset_pass_page = ResetPasswordPage(driver)

        common.go_to_reset_page()
        login_page.click_on_reset_password_button()
        reset_pass_page.wait_for_reset_pass_heading()
        reset_pass_page.input_email(UserData.USER_EMAIL)
        reset_pass_page.click_on_reset_password_button()
        reset_pass_page.wait_for_input_pass()

        actual = reset_pass_page.get_password_field_element()

        assert actual == 'Пароль'

    @allure.title('Reset password input test')
    @allure.description('Check hide password button')
    def test_hide_password_button(self, driver):
        common = CommonSteps(driver)
        login_page = LoginPage(driver)
        reset_pass_page = ResetPasswordPage(driver)

        common.go_to_reset_page()
        login_page.click_on_reset_password_button()
        reset_pass_page.wait_for_reset_pass_heading()
        reset_pass_page.input_email(UserData.USER_EMAIL)
        reset_pass_page.click_on_reset_password_button()
        reset_pass_page.wait_for_input_pass()
        reset_pass_page.input_pass(UserData.USER_PASS)
        reset_pass_page.click_on_hide_password_button()

        actual = reset_pass_page.get_password_input_class_list()

        assert 'input_status_active' in actual


