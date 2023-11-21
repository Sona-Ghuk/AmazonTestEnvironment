

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from pages_.basePage import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def search_product(self, product_name):
        search_input = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_input.send_keys(product_name)
        search_input.send_keys(Keys.RETURN)
        self.wait_for_page_load()

    def select_first_search_result(self):
        first_result = self.driver.find_element(By.CSS_SELECTOR, ".s-result-item")
        first_result.click()
        self.wait_for_page_load()

    def add_to_cart(self):
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-button")
        self.click_and_wait(add_to_cart_button)

    def filter_by_price(self, low_price, high_price):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "s-results-list-atf")))
        price_filter_low = self.driver.find_element(By.ID, "low-price")
        price_filter_low.send_keys(str(low_price))

        price_filter_high = self.driver.find_element(By.ID, "high-price")
        price_filter_high.send_keys(str(high_price))

        self.driver.find_element(By.ID, "a-auto-id-1-announce").click()

