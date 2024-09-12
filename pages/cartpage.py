from pages.basepage import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def check_item(self):
        return self.find(By.CLASS_NAME, "inventory_item_name").text

    def checkout_button_click(self):
        self.find(By.ID, "checkout").click()
