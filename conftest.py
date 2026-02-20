import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        path = ChromeDriverManager().install()

        if "THIRD_PARTY_NOTICES" in path:
            path = os.path.join(os.path.dirname(path), "chromedriver")

        service = ChromeService(executable_path=path)
        driver = webdriver.Chrome(service=service)

    else:
        path = "/usr/local/bin/geckodriver"
        service = FirefoxService(executable_path=path)
        driver = webdriver.Firefox(service=service)


    driver.maximize_window()
    driver.get("https://stellarburgers.education-services.ru/")

    yield driver
    driver.quit()
