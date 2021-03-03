from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from features.steps.BaseTest import BaseTest


class BaseTools:
    @staticmethod
    def click_enter():
        BaseTest.static_driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').send_keys(Keys.ENTER)
