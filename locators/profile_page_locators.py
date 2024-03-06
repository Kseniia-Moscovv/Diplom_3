from selenium.webdriver.common.by import By


class ProfilePageLocators:
    order_history_button = [By.XPATH, './/a[text()="История заказов"]']
    logout_button = [By.XPATH, './/nav[@class="Account_nav__Lgali"]/ul/li[3]/button']
    logout_button_element = [By.XPATH, './/button[text()="Выход"]']
    order_number_in_profile_history = [By.XPATH, './/div[@class="OrderHistory_orderHistory__qy1VB"]/ul/li[1]']
    text_order_number_in_profile_history = [By.XPATH, './/div[@class="OrderHistory_orderHistory__qy1VB"]/ul/li[1]/a/div/p[1]']