from pages.basepage import BasePage
from selenium.webdriver.common.by import By


class ProductsPage(BasePage):
    id = None

    def __init__(self, driver):
        super().__init__(driver)

    def set_item_id(self, id):
        self.id = id

    # добавить id для поиска любого товара
    @property
    def find_item_card(self):
        return self.find(By.XPATH, f'//*[@id="inventory_container"]/div/div[{self.id}]')

    @property
    def name_of_item(self):
        return self.find_item_card.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text

    # Depends on state of cart: could be "Add to cart" or "Remove"
    def click_item_button(self):
        self.find_item_card.find_element(By.TAG_NAME, "button").click()

    def click_to_cart(self):
        self.find(By.CLASS_NAME, "shopping_cart_link").click()
