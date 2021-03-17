# /!/usr/bin/python3
# *-*coding-utf8*-*
# Name:index_page
# Author:Administrator
# Time:2019/12/5
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.index_page_locator import IndexPageLocator as loc

class IndexPage:

    def __init__(self,driver:WebDriver):

        self.driver=driver

    def check_user_ele_exists(self):
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(loc.home))  #等待元素加载

        try:
            self.driver.find_element(*loc.user_link)   #定位元素
        except:
            return False
        else:
            return True

    def click_bid_button(self):
        pass