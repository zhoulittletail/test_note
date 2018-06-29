import pytest
from appium import webdriver
from base import init_driver
from page import DisPlayPage
from page.page import Page
class Test_display():
    def setup(self):

        # server 启动参数
        self.driver = init_driver()
        self.page = Page(self.driver)


    def test_mobile_display_input(self):

        self.page.display.click_display()
        self.page.display.click_serch()
        self.page.display.input_keyword("hello")
        self.page.display.click_back()