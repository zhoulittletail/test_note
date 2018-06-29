import pytest
from appium import webdriver
import sys, os
sys.path.append(os.getcwd())
from base import init_driver
from page import NetWorkPage
from page.page import Page
class Test_network():
    def setup(self):

        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_mobile_network_2g(self):
        self.page.network.click_more()
        self.page.network.click_move_network()
        self.page.network.click_first_choose()
        self.page.network.click_2g()

    def test_mobile_network_3g(self):
        self.page.network.click_more()
        self.page.network.click_move_network()
        self.page.network.click_first_choose()
        self.page.network.click_3g()
