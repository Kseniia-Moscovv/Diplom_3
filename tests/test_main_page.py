import time

import allure

from constants.ingredient_constants import IngredientData
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from utils.user_genegator import generate_user_data


class TestMainPage:
    @allure.title('Go to constructor test')
    @allure.description('Click to constructor button in header')
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.click_on_profile_button()
        login_page.wait_for_login_page()
        main_page.click_on_constructor_button()
        main_page.wait_for_main_page()
        actual = main_page.get_main_page_heading()

        assert actual == 'Соберите бургер'

    @allure.title('Go to order list test')
    @allure.description('Click to order list button in header')
    def test_go_to_order_list(self, driver):
        main_page = MainPage(driver)
        order_list = OrderListPage(driver)

        main_page.click_on_order_list_button()
        order_list.wait_for_order_list_page()
        actual = order_list.get_order_list_page_heading()

        assert actual == 'Лента заказов'

    @allure.title('Open ingredient modal test')
    @allure.description('Open ingredient modal by click on ingredient')
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        main_page.click_on_ingredient(IngredientData.SECTION_NAME_BUN, IngredientData.INGREDIENT_INDEX_BUN)
        main_page.wait_for_ingredient_modal_heading()
        actual = main_page.get_ingredient_modal_heading()

        assert actual == 'Детали ингредиента'

    @allure.title('Close ingredient modal test')
    @allure.description('Close ingredient modal by click on close button')
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        main_page.click_on_ingredient(IngredientData.SECTION_NAME_BUN, IngredientData.INGREDIENT_INDEX_BUN)
        main_page.wait_for_ingredient_modal_heading()
        main_page.click_on_close_modal_button()
        actual = main_page.get_ingredient_modal_class_list()

        assert 'Modal_modal_opened' not in actual

    @allure.title('Ingredient counter test')
    @allure.description('Ingredient counter up after add ingredient to basket')
    def test_counter_ingredient(self, driver):
        main_page = MainPage(driver)

        main_page.add_ingredient_to_basket(IngredientData.SECTION_NAME_BUN, IngredientData.INGREDIENT_INDEX_BUN)
        main_page.wait_ingredient_in_basket()
        actual = main_page.get_data_from_counter_locator(IngredientData.SECTION_NAME_BUN, IngredientData.INGREDIENT_INDEX_BUN)

        assert actual == '2'

    @allure.title('Create order test')
    @allure.description('Create order after login user')
    def test_create_order(self, driver, prepare_user):
        payload = generate_user_data()
        prepare_user(payload, driver)
        driver.refresh()

        main_page = MainPage(driver)
        main_page.wait_to_load_ingredient()
        main_page.add_ingredient_to_basket(IngredientData.SECTION_NAME_BUN, IngredientData.INGREDIENT_INDEX_BUN)
        main_page.wait_ingredient_in_basket()
        main_page.add_ingredient_to_basket(IngredientData.SECTION_NAME_SAUCE, IngredientData.INGREDIENT_INDEX_SAUCE)
        main_page.wait_ingredient_in_basket()
        main_page.add_ingredient_to_basket(IngredientData.SECTION_NAME_FILLING, IngredientData.INGREDIENT_INDEX_FILLING)
        main_page.wait_ingredient_in_basket()
        main_page.click_on_order_button()
        main_page.wait_for_heading_approve_order_modal()
        actual = main_page.get_approve_order_modal_heading()

        assert actual == "Ваш заказ начали готовить"









