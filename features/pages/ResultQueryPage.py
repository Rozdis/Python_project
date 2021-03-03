from selenium.webdriver.common.by import By

from features.enteties.Book import Book
from features.steps.BaseTest import BaseTest
from features.steps.BaseTools import BaseTools


class ResultQueryPage(BaseTest, BaseTools):
    LOCATOR_NAME_BOOK = '//div[contains(@class, "s-result-list")]/div[contains(@class, "s-result-item") and contains(@data-component-type, "s-search-result")]//h2/a/span'
    LOCATOR_AUTHOR_BOOK = '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div'

    @staticmethod
    def get_list_of_books():
        list_of_books = list()
        for x in range(16):
            list_of_books.append(ResultQueryPage.get_book_by_index(x))
        return list_of_books

    @classmethod
    def get_name_by_index(cls, index):
        return BaseTest.static_driver.find_elements_by_xpath(ResultQueryPage.LOCATOR_NAME_BOOK).pop(index).text

    @classmethod
    def get_author_by_index(cls, index):
        return BaseTest.static_driver.find_elements_by_xpath(ResultQueryPage.LOCATOR_AUTHOR_BOOK).pop(index).text

    @staticmethod
    def get_book_by_index(index):
        return Book(ResultQueryPage.get_name_by_index(index), ResultQueryPage.get_author_by_index(index))

    @staticmethod
    def check_book_in_list(list_of_books, book):
        for x in list_of_books:
            if x.name == book.name:
                return True
        return False
