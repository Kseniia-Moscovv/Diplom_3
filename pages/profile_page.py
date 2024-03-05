import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePageStellarBurger


class ProfilePage(BasePageStellarBurger):
    @allure.step('Wait to load profile page')
    def wait_for_logout_button(self):
        self.visibility_of_element_located(ProfilePageLocators.logout_button)

    @allure.step('Wait to load order history')
    def wait_for_order_history(self):
        self.visibility_of_element_located(ProfilePageLocators.order_history_button)

    @allure.step('Wait to load order in history')
    def wait_for_order_in_history(self):
        self.visibility_of_element_located(ProfilePageLocators.order_number_in_profile_history)

    @allure.step('Click to order history section')
    def click_on_order_history_button(self):
        self.click_on_element(ProfilePageLocators.order_history_button)

    @allure.step('Click to logout button')
    def click_on_logout_button(self):
        self.click_on_element(ProfilePageLocators.logout_button)

    @allure.step('Get element text logout button')
    def get_text_logout_button(self):
        return self.get_element_text(ProfilePageLocators.logout_button_element)

    @allure.step('Get user order number')
    def get_order_number(self):
        return self.get_element_text(ProfilePageLocators.text_order_number_in_profile_history)

    @allure.step('Get order history input class list')
    def get_order_history_class_list(self):
        order_history_link_container = self.find_element(ProfilePageLocators.order_history_button)
        return self.get_attribute(order_history_link_container, 'class')