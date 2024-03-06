import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from utils.user_genegator import generate_user_data


class TestProfilePage:
    @allure.title('Go to profile test')
    @allure.description('Go to profile after login')
    def test_go_to_profile(self, driver, prepare_user):
        payload = generate_user_data()
        prepare_user(payload, driver)

        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)

        main_page.click_on_profile_button()
        profile_page.wait_for_logout_button()
        actual = profile_page.get_text_logout_button()

        assert actual == 'Выход'

    @allure.title('Go to order history section test')
    @allure.description('Go to order history section after login')
    def test_go_to_order_history_section(self, driver, prepare_user):
        payload = generate_user_data()
        prepare_user(payload, driver)

        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)

        main_page.click_on_profile_button()
        profile_page.wait_for_order_history()
        profile_page.click_on_order_history_button()
        actual = profile_page.get_order_history_class_list()

        assert 'Account_link_active' in actual

    @allure.title('Logout test')
    @allure.description('Click to logout button in profile and logout user')
    def test_logout_user(self, driver, prepare_user):
        payload = generate_user_data()
        prepare_user(payload, driver)

        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        login_page = LoginPage(driver)

        main_page.click_on_profile_button()
        profile_page.wait_for_logout_button()
        profile_page.click_on_logout_button()
        login_page.wait_for_login_page()
        actual = login_page.get_login_page_heading()

        assert actual == 'Вход'


