import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    @allure.step("Получить количество выполненных заказов за всё время")
    def get_total_orders(self):
        return int(self.get_text(OrderFeedLocators.TOTAL_ORDERS))

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders(self):
        return int(self.get_text(OrderFeedLocators.TODAY_ORDERS))

    @allure.step("Проверить наличие заказа в работе")
    def orders_in_progress_visible(self):
        return self.find(OrderFeedLocators.ORDERS_IN_PROGRESS).is_displayed()
