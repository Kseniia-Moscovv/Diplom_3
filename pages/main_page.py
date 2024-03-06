import allure

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators

from pages.base_page import BasePageStellarBurger


class MainPage(BasePageStellarBurger):
    @allure.step('Go to login page')
    def click_on_profile_button(self):
        self.click_on_element(BasePageLocators.profile_button_on_header)

    @allure.step('Go to main page')
    def click_on_constructor_button(self):
        self.click_on_element(BasePageLocators.constructor_button_on_header)

    @allure.step('Wait to load main page')
    def wait_for_main_page(self):
        self.visibility_of_element_located(MainPageLocators.main_page_heading)

    @allure.step('Wait to load ingredient')
    def wait_to_load_ingredient(self):
        self.visibility_of_element_located(MainPageLocators.first_ingredient_in_ingredients_list)

    @allure.step('Get main page heading text')
    def get_main_page_heading(self):
        return self.get_element_text(MainPageLocators.main_page_heading)

    @allure.step('Go to order list')
    def click_on_order_list_button(self):
        self.click_on_element(BasePageLocators.order_list_button_on_header)

    @allure.step('Click on ingredient to open details')
    def click_on_ingredient(self, text, index):
        self.click_on_element(MainPageLocators.get_ingredient_locator(text, index))

    @allure.step('Wait to open ingredient modal')
    def wait_for_ingredient_modal_heading(self):
        self.visibility_of_element_located(MainPageLocators.ingredient_modal_heading)

    @allure.step('Get ingredient modal heading')
    def get_ingredient_modal_heading(self):
        return self.get_element_text(MainPageLocators.ingredient_modal_heading)

    @allure.step('Close ingredient modal')
    def click_on_close_modal_button(self):
        self.click_on_element(MainPageLocators.close_modal_button)

    @allure.step('Add ingredient to basket')
    def add_ingredient_to_basket(self, text, index):
        from_ingredient_list = self.find_element(MainPageLocators.get_ingredient_locator(text, index))
        to_basket = self.find_element(MainPageLocators.basket)
        self.drag_and_drop_element(from_ingredient_list, to_basket)

    @allure.step('Wait ingredient in basket')
    def wait_ingredient_in_basket(self):
        self.visibility_of_element_located(MainPageLocators.basket)

    @allure.step('Get data from counter locator')
    def get_data_from_counter_locator(self, text, index):
        return self.get_element_text(MainPageLocators.get_ingredient_counter_locator(text, index))

    @allure.step('Click on order button')
    def click_on_order_button(self):
        self.click_on_element(MainPageLocators.order_button)

    @allure.step('Wait to order confirmed modal')
    def wait_for_heading_approve_order_modal(self):
        self.visibility_of_element_located(MainPageLocators.approve_order_modal_heading)

    @allure.step('Get approve order modal heading')
    def get_approve_order_modal_heading(self):
        return self.get_element_text(MainPageLocators.approve_order_modal_heading)

    @allure.step('Get order number from approve order modal')
    def get_order_number_from_approve_order_modal(self):
        return self.get_element_text(MainPageLocators.new_order_number_in_approve_order_modal)

    @allure.step('Click to close order modal')
    def click_on_close_order_modal_button(self):
        self.click_on_element(MainPageLocators.close_order_modal_button)

    @allure.step('Click on ingredient')
    def click_on_ingredient(self, text, index):
        self.click_on_element(MainPageLocators.get_ingredient_locator(text, index))

    @allure.step('Get ingredient modal class list')
    def get_ingredient_modal_class_list(self):
        modal_container = self.find_element(MainPageLocators.modal_section)
        return self.get_attribute(modal_container, 'class')

    @allure.step('Wait for loading modal to hide')
    def wait_for_loading_modal_hide(self):
        self.invisibility_of_element_located(MainPageLocators.loading_modal)

