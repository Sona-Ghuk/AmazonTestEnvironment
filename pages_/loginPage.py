from selenium.webdriver.common.by import By

from pages_.basePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.login_button = (By.ID, "loginButton")

    def login(self, email, password):
        email_field = self.driver.find_element(By.ID, "ap_email")
        email_field.send_keys(email)
        self.driver.find_element(By.ID, "continue").click()
        password_field = self.driver.find_element(By.ID, "ap_password")
        password_field.send_keys(password)
        self.driver.find_element(By.ID, "signInSubmit").click()

    def fill_username(self, username):
        username_field = self.driver.find_element(By.ID, "username_field_id")
        username_field.send_keys(username)

    def click_continue(self):
        continue_button = self.driver.find_element(By.ID, "continue_button_id")
        continue_button.click()

    def fill_password(self, password):
        password_field = self.driver.find_element(By.ID, "password_field_id")
        password_field.send_keys(password)

    def click_signin(self):
        signin_button = self.driver.find_element(By.ID, "signin_button_id")
        signin_button.click()

    def test_negative_login_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.login("sona.ghukasyan@gmail.com", "123456")

        actual_error_message = login_page.get_error_message()

        expected_error_message = "password is incorrect"
        self.assertEqual(actual_error_message, expected_error_message, "Error message")
