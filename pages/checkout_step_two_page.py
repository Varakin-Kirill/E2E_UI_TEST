from pages.basepage import BasePage
from selenium.webdriver.common.by import By


class CheckoutStepTwoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def finish_button_click(self):
        self.find(By.ID, "finish").click()
