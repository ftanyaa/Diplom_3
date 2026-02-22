import allure
from pages.main_page import MainPage
from config.urls import BASE_URL, ORDER_FEED_URL

@allure.feature("Основной функционал")
class TestMainFunctionality:

    @allure.title("Переход по клику на Конструктор")
    def test_open_constructor(self, driver):
        page = MainPage(driver)
        page.open_constructor()
        assert page.current_url() == BASE_URL

    @allure.title("Переход по клику на Лента заказов")
    def test_open_order_feed(self, driver):
        page = MainPage(driver)
        page.open_order_feed()
        assert page.current_url() == ORDER_FEED_URL

    @allure.title("Открытие модального окна ингредиента")
    def test_open_ingredient_modal(self, driver):
        page = MainPage(driver)
        page.click_ingredient()
        assert page.modal_visible()

    @allure.title("Закрытие модального окна")
    def test_close_modal(self, driver):
        page = MainPage(driver)
        page.click_ingredient()
        page.close_modal()
        assert not page.modal_visible()

    @allure.title("Увеличение счётчика ингредиента")
    def test_counter_increase(self, driver):
        page = MainPage(driver)
        before = page.get_counter()
        page.click_ingredient()
        page.close_modal()
        after = page.get_counter()
        assert after >= before

