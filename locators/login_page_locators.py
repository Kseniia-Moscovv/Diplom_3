from selenium.webdriver.common.by import By


class LoginPageLocators:
    heading_login_page = [By.XPATH, './/h2[text()="Вход"]']
    reset_password_button = [By.XPATH, './/a[@href="/forgot-password"]']

