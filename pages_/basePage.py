from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_present(self, locator, timeout=10):
        try:
            element_present = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element_present
        except TimeoutException:
            raise NoSuchElementException(f"Element with locator {locator} not found within {timeout} seconds.")

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        try:
            element_clickable = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element_clickable
        except TimeoutException:
            raise NoSuchElementException(f"Element with locator {locator} not clickable within {timeout} seconds.")

    def wait_for_page_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def click_and_wait(self, element):
        element.click()
        try:
            WebDriverWait(self.driver, 10).until(EC.staleness_of(element))
        except StaleElementReferenceException:
            pass

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_to_cart_button(self, locator, timeout=10):
        cart_button = self.wait_for_element_to_be_clickable(locator, timeout)
        self.click_and_wait(cart_button)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.amazon.com")
        self.driver.maximize_window()

    def click_continue_button(self, locator, timeout=10):
        continue_button = self.wait_for_element_to_be_clickable(locator, timeout)
        self.click_and_wait(continue_button)

    def perform_cart_button_click(self, locator):
        cart_button_locator = (By.ID, "cart_button_id")
        self.click_to_cart_button(cart_button_locator)

    def setup_initial_state(self, locator=None):
        self.setUp()
        self.perform_cart_button_click(locator)

    def tearDown(self):
        self.driver.quit()
