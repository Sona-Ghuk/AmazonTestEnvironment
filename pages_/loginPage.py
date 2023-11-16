from time import sleep

from basepage import BasePage
from pages_.productSearchPage import ProductSearchPage
from pages_.shoppingCartPage import ShoppingCartPage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._usernameFieldLocator = (By.ID, "ap_email")
        self._continueButtonLocator = (By.ID, "continue")
        self._passwordButtonLocator = (By.ID, "ap_password")
        self._signInButtonLocator = (By.ID, "signInSubmit")
        self._product_search_page = ProductSearchPage(driver)
        self._shopping_cart_page = ShoppingCartPage(driver)

    def fill_username(self, username):
        username_field = self.driver.find_element(self._usernameFieldLocator)
        username_field.clear()
        username_field.send_keys(username)

    def click_continue_button(self):
        continue_button = self.driver.find_element(self._continueButtonLocator)
        continue_button.click()

    def fill_password(self, password):
        password_field = self.driver.find_element(self._passwordButtonLocator)
        password_field.clear()
        password_field.send_keys(password)

    def click_signin(self):
        signin_button = self.driver.find_element(self._signInButtonLocator)
        signin_button.click()

    def test_login(self, username, password):
        self.fill_username(username)
        self.click_continue_button()
        self.fill_password(password)
        self.click_signin()
        sleep(10)

    def search_product(self, product_name):
        self._product_search_page.fill_search_input(product_name)
        self._product_search_page.submit_search()

    def add_to_cart(self):
        self._shoping_cart_page.add_to_cart()
