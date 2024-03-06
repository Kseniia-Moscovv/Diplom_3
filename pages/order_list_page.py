import allure

from locators.order_list_page_locators import OrderListPageLocators
from pages.base_page import BasePageStellarBurger


class OrderListPage(BasePageStellarBurger):
    @allure.step('Wait to load order list page')
    def wait_for_order_list_page(self):
        self.visibility_of_element_located(OrderListPageLocators.order_list_page_heading)

    @allure.step('Open order details')
    def click_on_order(self, index):
        self.click_on_element(OrderListPageLocators.get_order_locator_in_details_modal(index))

    @allure.step('Wait to order details modal')
    def wait_for_order_list_details_modal(self):
        self.visibility_of_element_located(OrderListPageLocators.order_details_modal)

    @allure.step('Get order modal heading')
    def get_order_modal_heading(self):
        return self.get_element_text(OrderListPageLocators.order_modal_heading)

    @allure.step('Get order number from order list')
    def get_order_number_element_from_order_list(self, number):
        return self.find_element(OrderListPageLocators.get_order_number_in_order_list(number))

    @allure.step('Get total counter value')
    def get_total_counter_value(self):
        return self.get_element_text(OrderListPageLocators.total_order_counter)

    @allure.step('Get today counter value')
    def get_today_counter_value(self):
        return self.get_element_text(OrderListPageLocators.today_order_counter)

    @allure.step('Get today counter value')
    def get_today_counter_value(self):
        return self.get_element_text(OrderListPageLocators.today_order_counter)

    @allure.step('Get order number from progress list')
    def get_order_number_element_from_progress_list(self, number):
        return self.find_element(OrderListPageLocators.get_order_number_in_progress_list(number))

    @allure.step('Get order list page heading text')
    def get_order_list_page_heading(self):
        return self.get_element_text(OrderListPageLocators.order_list_page_heading)

    @allure.step('Get order number in progress list')
    def get_order_number_in_progress_list(self):
        return self.get_element_text(OrderListPageLocators.order_in_progress)
