from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class BasePageStellarBurger:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        self.find_element(locator).click()

    def get_element_text(self, locator):
        return self.find_element(locator).text

    def type_input_text(self, locator, text):
        input_element = self.find_element(locator)
        input_element.click()
        input_element.send_keys(text)

    def visibility_of_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def drag_and_drop_element(self, source_element, target_element):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    def get_attribute(self, element, attribute):
        return element.get_attribute(attribute)

    def invisibility_of_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    def refresh(self):
        self.driver.refresh()

