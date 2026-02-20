from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[contains(@href,'feed')]")

    INGREDIENT = (By.XPATH, "(//a[contains(@class,'BurgerIngredient')])[1]")
    INGREDIENT_COUNTER = (By.XPATH, "(//p[contains(@class,'counter_counter')])[1]")

    MODAL = (By.XPATH, "//section[contains(@class,'Modal_modal')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
