import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
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
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon"
            ".com%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select"
            "&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net"
            "%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("sona.ghukasyan@gmail.com", "hasiko07")
        time.sleep(5)

    def test_product_search(self):
        self.search_page.search_product("adidas shoes women")
        time.sleep(5)

    def test_price_filter(self):
        self.search_page.set_price_range(50, 100)
        self.search_page.apply_price_filter()
        time.sleep(5)

    def test_select_product(self):
        results = self.driver.find_elements(By.CSS_SELECTOR, "product_title")
        if results:
            results[0].click()

    def tearDown(self):
        self.driver.quit()
