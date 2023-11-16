from common_.utilities_.customLogger import logger
from selenium.webdriver.support.events import AbstractEventListener


class CustomListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        logger.info(f"Before navigating to: {url}")

    def after_navigate_to(self, url, driver):
        logger.info(f"After navigating to: {url}")

    def before_click(self, element, driver):
        logger.info(f"Before clicking on element: {element}")

    def after_click(self, element, driver):
        logger.info(f"After clicking on element: {element}")

    def after_quit(self, driver):
        logger.info("After quitting the driver")

    def on_exception(self, exception, driver):
        logger.error(f"Exception encountered: {exception}")