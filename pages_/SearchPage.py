import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages_.basePage import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_button_locator = (By.ID, "add-to-cart-button")
        self.low_price_input = (By.ID, "low-price")
        self.high_price_input = (By.ID, "high-price")
        self.apply_filter_button = (By.ID, "a-auto-id-1-announce")

    def search_product(self, product_name):
        search_input = self.wait_for_element((By.ID, "twotabsearchtextbox"))
        search_input.send_keys(product_name)
        search_input.send_keys(Keys.RETURN)

    def click_first_result(self):
        first_result = self.wait_for_element((By.CSS_SELECTOR, ".s-result-item"))
        first_result.click()

    def add_to_cart(self):
        add_to_cart_button = self.wait_for_element(self.add_to_cart_button_locator)
        add_to_cart_button.click()

    def delete_all_from_cart(self):
        remove_buttons = self.wait_for_elements((By.CSS_SELECTOR, "[value='Delete']"))
        for remove_button in remove_buttons:
            remove_button.click()
            time.sleep(2)

    def set_price_range(self, min_price, max_price):
        low_price_input = self.wait_for_element(self.low_price_input)
        low_price_input.clear()
        low_price_input.send_keys(str(min_price))

        high_price_input = self.wait_for_element(self.high_price_input)
        high_price_input.clear()
        high_price_input.send_keys(str(max_price))

    def apply_price_filter(self):
        apply_button = self.wait_for_element(self.apply_filter_button)
        apply_button.click()