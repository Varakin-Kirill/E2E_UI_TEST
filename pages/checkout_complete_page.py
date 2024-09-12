from pages.basepage import BasePage
from selenium.webdriver.common.by import By


class CheckoutComplete(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def check_complete(self):
        return self.find(By.CLASS_NAME, "complete-header").text
