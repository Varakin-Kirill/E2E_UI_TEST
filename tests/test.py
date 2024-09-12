from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cartpage import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutComplete


def test_open(driver):

    loginpage = LoginPage(driver)
    loginpage.enter_username("standard_user")
    loginpage.enter_password("secret_sauce")
    loginpage.click_login_button()

    productpage = ProductsPage(driver)
    productpage.set_item_id(1)
    productpage.click_item_button()
    name_of_item = productpage.name_of_item
    productpage.click_to_cart()

    cartpage = CartPage(driver)
    assert name_of_item == cartpage.check_item
    cartpage.checkout_button_click()

    checkout_step_one = CheckoutStepOnePage(driver)
    checkout_step_one.enter_first_name("Kirill")
    checkout_step_one.enter_last_name("Varakin")
    checkout_step_one.enter_postal_code("123456")
    checkout_step_one.continue_button_click()

    checkout_step_two = CheckoutStepTwoPage(driver)
    checkout_step_two.finish_button_click()

    checkout_complete = CheckoutComplete(driver)
    assert checkout_complete.check_complete == "Thank you for your order!"
