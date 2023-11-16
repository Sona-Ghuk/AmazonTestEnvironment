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
