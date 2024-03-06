from selenium.webdriver.common.by import By


class BasePageLocators:
    profile_button_on_header = [By.XPATH, './/a[@href="/account"]']
    constructor_button_on_header = [By.XPATH, './/nav[@class="AppHeader_header__nav__g5hnF"]/ul/li[1]']
    order_list_button_on_header = [By.XPATH, './/nav[@class="AppHeader_header__nav__g5hnF"]/ul/li[2]']
