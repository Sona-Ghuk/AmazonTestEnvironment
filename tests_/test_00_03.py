import unittest
import time
from selenium import webdriver


class AmazonLoginTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon"".com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess""%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        cls.login_page = webdriver

    def test_login(self):
        self.login_page.validate_continue_button_text()
        self.login_page.fill_username("sona.ghukasyan@gmail.com")
        self.login_page.validate_continue_button_text()
        self.login_page.click_continue_button()
        self.login_page.fill_password("hasiko07")
        self.login_page.click_signin()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
