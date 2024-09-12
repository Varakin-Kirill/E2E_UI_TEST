from pages.basepage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.saucedemo.com/")

    # def open(self, url):
    #     self.driver.get("https://www.saucedemo.com/")

    @property
    def find_username_input(self):
        return self.find(By.ID, "user-name")

    def enter_username(self, username):
        self.find_username_input.send_keys(username)

    @property
    def find_password_input(self):
        return self.find(By.ID, "password")

    def enter_password(self, password):
        self.find_password_input.send_keys(password)

    @property
    def find_login_button(self):
        return self.find(By.ID, "login-button")

    def click_login_button(self):
        self.find_login_button.click()
