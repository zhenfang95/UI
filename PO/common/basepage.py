# /!/usr/bin/python3
# *-*coding-utf8*-*
# Name:basepage
# Author:Administrator
# Time:2019/12/5
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time
from common.dir_config import screenshot_dir

class BasePage:
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def wait_eleVisible(self,loc,timeout=30,frequency=0.5,doc=""):
        start=time.time()
        try:
            WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(loc))
        except:
            logging.exception("等待{}元素可见，超时！".format(loc))
            raise
        else:
            end=time.time()
            duration=end-start
            logging.info("等待{}可见，等待时长为：{}".format(loc,duration))

    def get_element(self,loc,doc=""):
        try:
            ele=self.driver.find_element(*loc)
        except:
            logging.exception("等待{}元素存在，失败！".format(loc))
            self.save_img(doc)
            raise
        else:
            logging.info("查找{}的元素{}成功。".format(doc,loc))

    def input_text(self,loc,value,timeout=30,frequency=0.5,doc=""):
        self.wait_eleVisible(loc,timeout,frequency,doc)
        ele=self.get_element(loc,doc)
        try:
            ele.send_keys(value)
        except:
            logging.exception("向元素{}输入{}失败".format(loc,value))
            self.save_img(doc)
            raise
        else:
            logging.info("向元素{}输入{}成功".format(loc,value))

    def click(self,loc,timeout=30,frequency=0.5,doc=""):
        self.wait_eleVisible(loc,timeout,frequency,doc)
        ele=self.get_element(loc,doc)
        try:
            ele.click()
        except:
            logging.exception("向元素{}点击操作失败".format(loc))
            self.save_img(doc)
            raise
        else:
            logging.info("向元素{}点击操作成功".format(loc))

    def get_element_text(self,loc,timeout=30,frequency=0.5,doc=""):
        self.wait_eleVisible(loc,timeout,frequency,doc)
        ele=self.get_element(loc,doc)
        try:
            ele.click()
        except:
            logging.exception("向元素{}点击操作失败".format(loc))
            self.save_img(doc)
            raise
        else:
            logging.info("向元素{}点击操作成功".format(loc))

    def get_element_attr(self):
        pass

    def switch_frame(self,locator,timeout):
        try:
            WebDriverWait(self.driver,timeout).until(EC.frame_to_be_available_and_switch_to_it(locator))
        except:
            pass

    def switch_window(self,index):
        if index == "new":
            pass
        elif index == "main":
            pass
        else:
            pass

    def save_img(self,doc=""):
        cur_time=""
        file=screenshot_dir+"/{}_{}.png".format(doc,cur_time)
        try:
            self.driver.save_screenshot(file)
        except:
            logging.exception("截图失败")
        else:
            logging.info("截图成功，截图存储路径为：{}".format(file))