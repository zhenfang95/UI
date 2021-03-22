# /!/usr/bin/python3
# *-*coding-utf8*-*

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.logger import log1
import time
from common.dir_config import screenshot_dir

class BasePage:
    def __init__(self,driver:WebDriver):
        self.driver=driver
        self.driver.maximize_window()

    def wait_eleVisible(self,loc,timeout=30,frequency=0.5,doc=""):
        start=time.time()
        try:
            WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(loc))
        except:
            log1.error("等待{}元素可见，超时！".format(loc))
            raise
        else:
            end=time.time()
            duration=end-start
            log1.info("等待{}可见，等待时长为：{}".format(loc,duration))

    def get_element(self,loc,doc=""):
        try:
            ele=self.driver.find_element(*loc)
        except:
            log1.error("等待{}元素存在，失败！".format(loc))
            self.save_img(doc)
            raise
        else:
            log1.info("查找{}的元素{}成功。".format(doc,loc))
        return ele

    def input_text(self,loc,value,timeout=30,frequency=0.5,doc=""):
        self.wait_eleVisible(loc,timeout,frequency,doc)
        ele=self.get_element(loc,doc)
        try:
            ele.send_keys(value)
        except:
            log1.error("向元素{}输入{}失败".format(loc,value))
            self.save_img(doc)
            raise
        else:
            log1.info("向元素{}输入{}成功".format(loc,value))

    def click(self,loc,timeout=30,frequency=0.5,doc=""):
        self.wait_eleVisible(loc,timeout,frequency,doc)
        ele=self.get_element(loc,doc)
        try:
            ele.click()
        except:
            log1.error("向元素{}点击操作失败".format(loc))
            self.save_img(doc)
            raise
        else:
            log1.info("向元素{}点击操作成功".format(loc))

    def get_element_text(self,loc,timeout=30,frequency=0.5,doc=""):
        self.wait_eleVisible(loc,timeout,frequency,doc)
        ele=self.get_element(loc,doc)
        try:
            ele.click()
        except:
            log1.error("向元素{}点击操作失败".format(loc))
            self.save_img(doc)
            raise
        else:
            log1.info("向元素{}点击操作成功".format(loc))

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
            log1.error("截图失败")
        else:
            log1.info("截图成功，截图存储路径为：{}".format(file))