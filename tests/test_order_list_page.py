import allure

from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from pages.profile_page import ProfilePage
from utils.user_genegator import generate_user_data


class TestOrderListPage:
    @allure.title('Order modal test')
    @allure.description('Get order information in order modal on order list page')
    def test_order_modal(self, driver, prepare_user, prepare_user_order):
        payload = generate_user_data()
        prepare_user(payload, driver)
        driver.refresh()

        prepare_user_order(driver)

        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)

        main_page.click_on_close_order_modal_button()
        main_page.click_on_order_list_button()
        order_list_page.wait_for_order_list_page()
        order_list_page.click_on_order(1)
        order_list_page.wait_for_order_list_details_modal()
        actual = order_list_page.get_order_modal_heading()

        assert actual == 'Cостав'

    @allure.title('Order from history in order list test')
    @allure.description('Check that order from history is on order list page')
    def test_order_number_in_order_list_from_history(self, driver, prepare_user, prepare_user_order):
        payload = generate_user_data()
        prepare_user(payload, driver)
        driver.refresh()

        prepare_user_order(driver)

        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)
        profile_page = ProfilePage(driver)

        main_page.click_on_close_order_modal_button()
        main_page.click_on_profile_button()
        profile_page.wait_for_order_history()
        profile_page.click_on_order_history_button()
        profile_page.wait_for_order_in_history()
        profile_history_order_number = profile_page.get_order_number()

        main_page.click_on_order_list_button()
        order_list_page.wait_for_order_list_page()

        actual = order_list_page.get_order_number_element_from_order_list(profile_history_order_number)

        assert actual is not None

    @allure.title('Total order counter test')
    @allure.description('Total order counter multiply after create new order')
    def test_total_order_counter(self, driver, prepare_user, prepare_user_order):
        payload = generate_user_data()
        prepare_user(payload, driver)
        driver.refresh()

        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)

        main_page.click_on_order_list_button()
        order_list_page.wait_for_order_list_page()
        total_before_new_order = order_list_page.get_total_counter_value()
        main_page.click_on_constructor_button()
        main_page.wait_for_main_page()

        prepare_user_order(driver)

        main_page.click_on_close_order_modal_button()
        main_page.click_on_order_list_button()
        order_list_page.wait_for_order_list_page()
        total_after_new_order = order_list_page.get_total_counter_value()

        assert int(total_before_new_order) < int(total_after_new_order)

    @allure.title('Today order counter test')
    @allure.description('Today order counter multiply after create new order')
    def test_today_order_counter(self, driver, prepare_user, prepare_user_order):
        payload = generate_user_data()
        prepare_user(payload, driver)
        driver.refresh()

        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)

        main_page.click_on_order_list_button()
        order_list_page.wait_for_order_list_page()
        today_before_new_order = order_list_page.get_today_counter_value()
        main_page.click_on_constructor_button()
        main_page.wait_for_main_page()

        prepare_user_order(driver)

        main_page.click_on_close_order_modal_button()
        main_page.click_on_order_list_button()
        order_list_page.wait_for_order_list_page()
        today_after_new_order = order_list_page.get_today_counter_value()

        assert int(today_before_new_order) < int(today_after_new_order)

    @allure.title('New order is in progress list test')
    @allure.description('New order number get in in_progress list')
    def test_order_modal(self, driver, prepare_user, prepare_user_order):
        payload = generate_user_data()
        prepare_user(payload, driver)
        driver.refresh()

        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)

        prepare_user_order(driver)

        main_page.wait_for_loading_modal_hide()
        new_order_number = main_page.get_order_number_from_approve_order_modal()
        main_page.click_on_close_order_modal_button()
        main_page.click_on_order_list_button()
        order_list_page.wait_for_order_list_page()

        actual = order_list_page.get_order_number_in_progress_list()

        assert new_order_number == actual