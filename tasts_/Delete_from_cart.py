import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages_.loginPage import LoginPage
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import CustomListener


class LogInPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.driver, CustomListener())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_login(self):
        loginPage = LoginPage()
        loginPage.fill_username("sona.ghukasyan@gmail.com")
        loginPage.click_continue_button()
        loginPage.fill_password("hasiko07")
        loginPage.click_signin()
        time.sleep(10)

    def search_product(self):
        search_input = self.driver.find_element_by_id("twotabsearchtextbox")
        search_input.send_keys("laptop")
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)

        first_result = self.driver.find_element(By.CSS_SELECTOR, ".s-result-item")
        first_result.click()
        time.sleep(5)

    def add_to_cart(self):
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        add_to_cart_button.click()
        time.sleep(5)

        self.driver.get("https://www.amazon.com/gp/cart/view.html")

    def delete_from_cart(self):
        delete_button = self.driver.find_element(By.CSS_SELECTOR, "[value='Delete']")
        delete_button.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()
