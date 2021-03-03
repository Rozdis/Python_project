from selenium.webdriver.common.by import By

from features.steps import BaseTools
from features.steps.BaseTest import BaseTest


class SearchBox(BaseTest):
    LOCATOR_AMAZON_SEARCH_FIELD = (By.XPATH, '//*[@id="twotabsearchtextbox"]')
    LOCATOR_CHOOSE_BOOK_IN_FILTERS_BUTTON = (By.XPATH, '//*[@id="searchDropdownBox"]/option[6]')

    def __init__(self):
        pass

    @staticmethod
    def choose_filter_book():
        BaseTest.static_driver.find_element(*SearchBox.LOCATOR_CHOOSE_BOOK_IN_FILTERS_BUTTON).click()

    @staticmethod
    def type_in_search_field(text):
        BaseTest.static_driver.find_element(*SearchBox.LOCATOR_AMAZON_SEARCH_FIELD).send_keys(text)
        BaseTools.BaseTools.click_enter()
