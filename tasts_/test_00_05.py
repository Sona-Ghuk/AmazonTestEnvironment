import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages_.loginPage import LoginPage


class LogIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_positive_login(self):
        login_page = LoginPage()
        login_page.fill_username("sona.ghukasyan@gmail.com")
        login_page.click_continue()
        login_page.fill_password("hasiko07")
        login_page.click_signin()

    def test_negative_login(self):
        login_page = LoginPage()
        login_page.fill_username("sona.ghukasyan@gmail.com")
        login_page.validate_continue_button_text()
        login_page.click_continue()
        login_page.fill_password("12345678")

        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='auth-error-message-box']//span")))

        expected_error_message = "Your password is incorrect"
        self.assertIn(expected_error_message.lower(), error_message_element.text.lower())

        with self.assertRaises(AssertionError, msg="Expected error message not found"):
            self.assertIn(expected_error_message, error_message_element.text)

    def tearDown(self):
        self.driver.close()
