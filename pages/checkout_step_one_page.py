from pages.basepage import BasePage
from selenium.webdriver.common.by import By


class CheckoutStepOnePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def find_first_name_input(self):
        return self.find(By.ID, "first-name")

    def enter_first_name(self, first_name):
        self.find_first_name_input.send_keys(first_name)

    @property
    def find_last_name_input(self):
        return self.find(By.ID, "last-name")

    def enter_last_name(self, last_name):
        self.find_last_name_input.send_keys(last_name)

    @property
    def find_postal_code_input(self):
        return self.find(By.ID, "postal-code")

    def enter_postal_code(self, postal_code):
        self.find_postal_code_input.send_keys(postal_code)

    def continue_button_click(self):
        self.find(By.ID, "continue").click()
