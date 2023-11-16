from selenium.webdriver.common.by import By
<<<<<<< HEAD
from selenium.webdriver.common.keys import Keys
=======
>>>>>>> 31075c5ab09785575637e004ab9d66bc749ac07c
from pages_.basePage import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
<<<<<<< HEAD

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

=======
        self.__cartButtonLocator = (By.ID, "nav-cart-count-container")

    def click_to_cart_button(self, cardbuttonElement=None):
        self._find_element(self.__cartButtonLocator)
        self._click(cardbuttonElement)

    def _find_element(self, __cartButtonLocator):
        pass

    def _click(self, cardbuttonElement):
        pass

    def click_cart_button(self):
        pass
>>>>>>> 31075c5ab09785575637e004ab9d66bc749ac07c
