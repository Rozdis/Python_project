# -*- coding: utf-8 -*-
from behave import *
from selenium import webdriver

from features.pages import SearchBox


class BaseTest:

    static_driver = webdriver.Chrome(executable_path='D:\\PythonProjects\\features\\driver\\chromedriver.exe')

    #def __init__(self):
        #self.static_driver = webdriver.Chrome(executable_path='D:\\PythonProjects\\features\\driver\\chromedriver.exe')

    @given('website "{url}"')
    def step(context, url):
        BaseTest.static_driver.maximize_window()
        BaseTest.static_driver.get(url)

    @then('close connection')
    def close(context):
        BaseTest.static_driver.quit()

    @staticmethod
    def get_driver():
        return BaseTest.static_driver