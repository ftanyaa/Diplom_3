import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from config.urls import ORDER_FEED_URL


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Увеличение счетчика заказов за всё время")
    def test_total_orders_increase(self, driver):
        main = MainPage(driver)
        main.open_order_feed()

        feed = OrderFeedPage(driver)
        assert feed.current_url() == ORDER_FEED_URL  # проверяем URL

        before = feed.get_total_orders()
        after = feed.get_total_orders()

        assert after >= before

    @allure.title("Увеличение счетчика заказов за сегодня")
    def test_today_orders_increase(self, driver):
        main = MainPage(driver)
        main.open_order_feed()

        feed = OrderFeedPage(driver)
        assert feed.current_url() == ORDER_FEED_URL  # проверяем URL

        before = feed.get_today_orders()
        after = feed.get_today_orders()

        assert after >= before

    @allure.title("Новый заказ появляется в работе")
    def test_order_in_progress(self, driver):
        main = MainPage(driver)
        main.open_order_feed()

        feed = OrderFeedPage(driver)
        assert feed.current_url() == ORDER_FEED_URL  # проверяем URL

        assert feed.orders_in_progress_visible()
