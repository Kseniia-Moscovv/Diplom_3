import pytest

from constants.ingredient_constants import IngredientData
from pages.main_page import MainPage


@pytest.fixture(scope='function')
def prepare_user_order():
    def _prepare_user_order(driver):
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

    return _prepare_user_order