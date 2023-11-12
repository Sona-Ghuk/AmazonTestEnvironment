from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
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