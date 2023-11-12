import time
import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import CustomListener


class LogInPage(unittest.TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.BasePage = None

    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, CustomListener())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com" "%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0" "%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F""%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_login_successful(self):
        loginPage = LoginPage(self.BasePage)
        loginPage.fill_username("sona.ghukasyan@gmail.com")
        loginPage.click_continue_button()
        loginPage.fill_password("hasiko07")
        loginPage.click_signin()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()
