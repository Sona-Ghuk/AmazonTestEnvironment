import unittest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import CustomListener
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages_.loginPage import LoginPage

custom_listener = CustomListener()
driver = webdriver.Chrome()
event_driver = EventFiringWebDriver(driver, custom_listener)


class LogInPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon"
            ".com%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select"
            "&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net"
            "%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("sona.ghukasyan@gmail.com", "hasiko07")

    def search_product(self):
        search_bar = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_bar.send_keys("adidas shoes women")
        search_bar.send_keys(Keys.RETURN)

    def test_price_filter(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "s-result-info")))
        price_filter = self.driver.find_element(By.ID, "low-price")
        price_filter.send_keys("50")
        price_filter = self.driver.find_element(By.ID, "high-price")
        price_filter.send_keys("100")
        self.driver.find_element(By.ID, "a-auto-id-1-announce").click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "s-results-list-atf")))

    def test_select_product(self):
        results = self.driver.find_elements(By.CSS_SELECTOR, "product_title")
        if results:
            results[0].click()

    def tearDown(self):
        self.driver.quit()
