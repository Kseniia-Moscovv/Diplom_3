from selenium.webdriver.common.by import By


class MainPageLocators:
    main_page_heading = [By.XPATH, './/h1[text()="Соберите бургер"]']
    first_ingredient_in_ingredients_list = [By.XPATH, './/h2[text()="Булки"]/following-sibling::ul[1]/a[1]']
    ingredient_modal_heading = [By.XPATH, './/h2[text()="Детали ингредиента"]']
    close_modal_button = [By.XPATH, './/section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]/div/button']
    modal_section = [By.XPATH, './/h2[text()="Детали ингредиента"]/ancestor::section[@class="Modal_modal__P3_V5"]']
    basket = [By.XPATH, './/section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]/ul']
    order_button = [By.XPATH, './/button[text()="Оформить заказ"]']
    approve_order_modal_heading = [By.XPATH, './/p[text()="Ваш заказ начали готовить"]']
    new_order_number_in_approve_order_modal = [By.XPATH, './/section[contains(@class,"Modal_modal_opened__3ISw4")]//h2']
    close_order_modal_button = [By.CLASS_NAME, 'Modal_modal__close__TnseK']
    loading_modal = [By.XPATH, './/img[@class="Modal_modal__loading__3534A"]/parent::div']

    @staticmethod
    def get_ingredient_locator(text, index):
        return [By.XPATH, f'.//h2[text()="{text}"]/following-sibling::ul[1]/a[{index}]']

    @staticmethod
    def get_ingredient_counter_locator(text, index):
        return [By.XPATH, f'.//h2[text()="{text}"]/following-sibling::ul[1]/a[{index}]/div[1]/p']


