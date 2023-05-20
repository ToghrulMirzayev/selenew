"""
Module that contains methods to find elements by using different strategies
"""

from selenium.webdriver.common.by import By
from collections import namedtuple


class Strategy:
    LOCATOR = namedtuple("Locator", ["by", "value"])

    @staticmethod
    def find_by_id(value: str) -> LOCATOR:
        return Strategy.LOCATOR(By.ID, value)

    @staticmethod
    def find_by_css(value: str) -> LOCATOR:
        return Strategy.LOCATOR(By.CSS_SELECTOR, value)

    @staticmethod
    def find_by_xpath(value: str) -> LOCATOR:
        return Strategy.LOCATOR(By.XPATH, value)

    @staticmethod
    def find_by_class(value: str) -> LOCATOR:
        return Strategy.LOCATOR(By.CLASS_NAME, value)

    @staticmethod
    def find_by_name(value: str) -> LOCATOR:
        return Strategy.LOCATOR(By.NAME, value)

    @staticmethod
    def find_by_tag(value: str) -> LOCATOR:
        return Strategy.LOCATOR(By.TAG_NAME, value)
