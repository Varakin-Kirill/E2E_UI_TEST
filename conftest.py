import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium import webdriver


@pytest.fixture()
def driver():
    service = Service(
        executable_path="chromedriver.exe"
    )
    driver = webdriver.Chrome(service=service, options=ChromeOptions())
    driver.implicitly_wait(10)
    yield driver
    driver.close()
