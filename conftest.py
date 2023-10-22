import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    service = Service()
    driver = webdriver.Chrome(options=options, service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
