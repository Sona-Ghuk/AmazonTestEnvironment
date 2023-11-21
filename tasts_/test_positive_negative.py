import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage


class loginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_positive_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("sona.ghukasyan@gmail.com", "hasiko07")

    def test_negative_login_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.login("sona.ghukasyan@gmail.com", "123456")
        expected_error_message = "password is incorrect"
        actual_error_message = expected_error_message
        self.assertEqual(actual_error_message, expected_error_message)

    def tearDown(self):
        self.driver.close()

