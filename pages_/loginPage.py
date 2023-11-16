<<<<<<< HEAD
from time import sleep

from basepage import BasePage
from pages_.productSearchPage import ProductSearchPage
from pages_.shoppingCartPage import ShoppingCartPage
from selenium.webdriver.common.by import By
=======
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
>>>>>>> 31075c5ab09785575637e004ab9d66bc749ac07c


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
<<<<<<< HEAD
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
=======
        self.login_page = None
        self.driver = driver

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to= ...")
        self.login_page = LoginPage(self.driver)

    def test_login(self, email, password):
        email_field = self.driver.find_element(By.ID, "ap_email")
        email_field.send_keys(email)
        self.driver.find_element(By.ID, "continue").click()

        password_field = self.driver.find_element(By.ID, "ap_password")
        password_field.send_keys(password)
        self.driver.find_element(By.ID, "signInSubmit").click()

    def fill_username(self, param):
        pass

    def click_continue_button(self):
        pass

    def fill_password(self, param):
        pass

    def click_signin(self):
        pass

    def get(self):
        pass

    def click_continue(self):
        pass

    def tearDown(self):
        self.driver.quit()


def click_continue():
    return None


def fill_password(param):
    return None


def click_signin():
    return None
>>>>>>> 31075c5ab09785575637e004ab9d66bc749ac07c
