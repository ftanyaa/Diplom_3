import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Открыть конструктор")
    def open_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Открыть ленту заказов")
    def open_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть ингредиент")
    def click_ingredient(self):
        self.click(MainPageLocators.INGREDIENT)

    @allure.step("Проверить модальное окно")
    def modal_visible(self):
        try:
            return self.driver.find_element(*MainPageLocators.MODAL).is_displayed()
        except NoSuchElementException:
            return False

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.CLOSE_MODAL_BUTTON)
        try:
            self.wait.until(EC.invisibility_of_element_located(MainPageLocators.MODAL))
        except TimeoutException:
            pass 

    @allure.step("Получить счетчик")
    def get_counter(self):
        return int(self.get_text(MainPageLocators.INGREDIENT_COUNTER))

    @allure.step("Получить текущий URL")
    def current_url(self):
        return self.driver.current_url
