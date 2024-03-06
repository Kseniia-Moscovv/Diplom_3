from selenium.webdriver.common.by import By


class ResetPassPageLocators:
    heading_reset_password_page = [By.XPATH, './/h2[text()="Восстановление пароля"]']
    email_input = [By.NAME, 'name']
    reset_button = [By.CLASS_NAME, 'button_button__33qZ0']
    password_label = [By.XPATH, './/label[text()="Пароль"]']
    password_input = [By.NAME, 'Введите новый пароль']
    password_input_container = [By.XPATH, './/label[text()="Пароль"]/parent::div']
    hide_password_button = [By.CLASS_NAME, 'input__icon']
