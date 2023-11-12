from selenium.webdriver.support.events import AbstractEventListener
from common_.utilities_.customLogger import logger


class CustomListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        logger.info(f"Navigating to {url}")

    def before_click(self, element, driver):
        logger.info(f"Clicking on {element}")

    def after_click(self, element, driver):
        logger.info(f"Clicked on {element}")

    def before_find(self, by, value, driver):
        logger.info(f"Trying to find element by: {by} with value: {value}")

    def after_find(self, by, value, driver):
        logger.info(f"Found element by: {by} with value: {value}")
