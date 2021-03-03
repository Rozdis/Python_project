from behave import *

from features.pages.ResultQueryPage import ResultQueryPage
from features.pages.SearchBox import SearchBox
from features.steps import BaseTest


class Tests:

    @then('Filter should be selected : Book')
    def select_book(context):
        SearchBox.choose_filter_book()

    @then('Type in search field : {text}')
    def type_in_search_field(context, text):
        SearchBox.type_in_search_field(text)

    @then('Check book on page')
    def check(self):
       assert ResultQueryPage.check_book_in_list(ResultQueryPage.get_list_of_books(), ResultQueryPage.get_book_by_index(1))
