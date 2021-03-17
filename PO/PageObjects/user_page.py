# /!/usr/bin/python3
# *-*coding-utf8*-*
# Name:user_page
# Author:Administrator
# Time:2019/12/5
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class BidPage:
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def get_user_leftMoney(self):
        pass

    def get_bid_money(self):
        pass

    def invwst(self,money):
        pass

    def click_activeButton_on_sucess_popUp(self):
        pass