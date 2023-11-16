import time
import unittest
from selenium import webdriver
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
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon"".com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess""%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        self.login_page = webdriver
        time.sleep(15)

    def test_login(self):
        loginPage = LoginPage()
        loginPage.fill_username("sona.ghukasyan@gmail.com")
        loginPage.click_continue_button()
        loginPage.fill_password("hasiko07")
        loginPage.click_signin()
        time.sleep(10)

    def search_product(self):
        search_input = self.driver.find_element_by_id("twotabsearchtextbox")
        search_input.send_keys("Computer Chair")
        search_input.submit()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()
