from selenium.webdriver.common.by import By


class OrderListPageLocators:
    order_list_page_heading = [By.XPATH, './/h1[text()="Лента заказов"]']
    order_details_modal = [By.CLASS_NAME, 'Modal_modal_opened__3ISw4']
    order_modal_heading = [By.XPATH, './/p[text()="Cостав"]']
    total_order_counter = [By.XPATH, './/div[@class="undefined mb-15"]/p[2]']
    today_order_counter = [By.XPATH, './/p[text()="Выполнено за сегодня:"]/following-sibling::p']
    order_in_progress = [By.XPATH, './/ul[contains(@class,"OrderFeed_orderListReady__1YFem")]/li[1]']

    @staticmethod
    def get_order_locator_in_details_modal(index):
        return [By.XPATH, f'.//div[@class="OrderFeed_contentBox__3-tWb"]/ul/li[{index}]']

    @staticmethod
    def get_order_number_in_order_list(order_number):
        return [By.XPATH, f'.//p[text()="{order_number}"]']

    @staticmethod
    def get_order_number_in_progress_list(order_number_in_progress):
        return [By.XPATH, f'.//ul[contains(@class,"OrderFeed_orderList__cBvyi")]/li[text()="{order_number_in_progress}"]']
