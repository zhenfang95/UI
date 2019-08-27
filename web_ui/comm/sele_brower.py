#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/8/26 16:26

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  #是显式等待，等待的时间是固定的
from selenium.webdriver.common.by import By  #定位器分类
from selenium.webdriver.support import expected_conditions as EC   #判断页面元素
#ActionChains是自动执行交互的一种方式，例如：鼠标移动，鼠标点按，键盘操作，文本操作等
from selenium.webdriver.common.action_chains import ActionChains
from comm.logs import log1

class PySele():
    def __init__(self,brower):
        '''初始化浏览器'''
        if brower == 'Firefox' or brower == 'firefox' or brower == 'f' or brower == 'F':
            driver=webdriver.Firefox()
        elif brower == 'Chrome' or brower == 'chrome' or brower =='Ch' or brower == 'ch':
            driver=webdriver.Chrome()
        elif brower == 'Ie' or brower == 'ie' or brower == 'I' or brower == 'i':
            driver=webdriver.Ie
        else:
            log1.error("打开浏览器失败")
            raise NameError('只能输入Firefox,Ie,Chrome')  #抛出NameError异常，后面的代码将不再执行
        self.driver=driver
        log1.info("打开%s浏览器" %brower)

    def element(self,fangfa,dingwei):
        '''元素定位'''
        if fangfa == 'id':
            element=self.driver.find_element_by_id(dingwei)
        elif fangfa == 'name':
            element=self.driver.find_element_by_name(dingwei)
        elif fangfa == 'class':
            element=self.driver.find_element_by_class_name(dingwei)
        elif fangfa == 'xpath':
            element=self.driver.find_element_by_xpath(dingwei)
        elif fangfa == 'link_text':
            element=self.driver.find_element_by_link_text(dingwei)
        elif fangfa == 'tag':
            element=self.driver.find_element_by_tag_name(dingwei)
        elif fangfa == 'css':
            element=self.driver.find_element_by_css_selector(dingwei)
        else:
            log1.error("没有找到元素")
            raise NameError("请输入定位元素方法,如'id','name','class','link_text','xpath','css','tag'")
        log1.info("元素定位成功，定位方法：%s，元素值：%s" %(fangfa,dingwei))
        return element

    def element_wait(self, fangfa, dingwei, wati=6):
        '''等待元素加载'''
        #每隔1s调用一次until中的方法（这个方法可以是用于判断某个元素是否存在的方法，存在返回true，否则返回false），最长等待6秒，6秒后继续执行下一步
        if fangfa == "id":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.ID, dingwei)))
        elif fangfa == "name":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.NAME, dingwei)))
        elif fangfa == "class":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.CLASS_NAME, dingwei)))
        elif fangfa == "link_text":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.LINK_TEXT, dingwei)))
        elif fangfa == "xpath":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.XPATH, dingwei)))
        elif fangfa == "css":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, dingwei)))
        else:
            log1.error("没有找到元素或元素加载超时")
            raise NameError("请输入定位元素方法,如,'id','name','class','link_text','xpath','css'.")

    def open(self, url):
        '''打开网页'''
        self.driver.get(url)
        log1.info("打开url：%s" %url)

    def make_maxwindow(self):
        '''最大化浏览器'''
        self.driver.maximize_window()
        log1.info("最大化浏览器")

    def set_winsize(self, wide, hight):
        '''设置窗口大小'''
        self.driver.set_window_size(wide, hight)
        log1.info("设置浏览器窗口大小为：wide=%s，hight=%s" %(wide,hight))

    def send_key(self, fangfa, dingwei, text):
        '''输入内容'''
        try:
            e1 = self.element(fangfa, dingwei)
            e1.clear()
            e1.send_keys(text)
            log1.info("输入的测试内容：%s" %text)
        except Exception as e:
            log1.error("输入测试内容异常，原因：%s" %e)

    def clear(self, fangfa, dingwei):
        '''清空'''
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        e1.clear()
        log1.info("清空输入框内容")

    def click(self, fangfa, dingwei):
        '''单击'''
        try:
            self.element_wait(fangfa, dingwei)
            e1 = self.element(fangfa, dingwei)
            e1.click()
            log1.info("点击元素成功")
        except Exception as e:
            log1.info("点击元素异常，原因：%s"%e)

    def right_click(self, fangfa, dingwei):
        '''右击'''
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        ActionChains(self.driver).context_click(e1).perform()

    def move_element(self, fangfa, dingwei):
        '''移动到'''
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        ActionChains(self.driver).move_to_element(e1).perform()

    def double_click(self, dingwei, fangfa):
        '''双击'''
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        ActionChains(self.driver).double_click(e1).perform()

    def drag_and_drop(self, fangfa1, e1, fangfa2, e2):
        '''从e1到e2'''
        self.element_wait(fangfa1, e1)
        eme1 = self.element(fangfa1, e1)
        self.element_wait(fangfa2, e2)
        eme2 = self.element(fangfa2, e2)
        ActionChains(self.driver).drag_and_drop(eme1, eme2).perform()

    def click_text(self, text):
        '''点击文字'''
        self.driver.find_element_by_link_text(text).click()
        log1.info("点击文本内容:%s"%text)

    def close(self):
        '''关闭'''
        self.driver.close()
        log1.info("关闭浏览器")

    def quit(self):
        '''退出'''
        self.driver.quit()
        log1.info("退出浏览器")

    def sublimit(self, fangfa, dingwei):
        '''提交'''
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        e1.sublimit()

    def f5(self):
        '''刷新'''
        self.driver.refresh()
        log1.info("刷新浏览器")

    def js(self, sprit):
        '''执行js'''
        try:
            self.driver.execute_script(sprit)
            log1.info("执行js成功，js内容为：%s" %sprit)
        except Exception as e:
            log1.error("执行js报错，原因：%s" %e)

    def get_attribute(self, fangfa, dingwei, attribute):
        e1 = self.element(fangfa, dingwei)
        return e1.get_attribute(attribute)

    def get_text(self, fangfa, dingwei):
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        return e1.text

    def get_is_dis(self, fangfa, dingwei):
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        return e1.is_displayed()

    def get_title(self):
        '''获取title'''
        tt=self.driver.title
        log1.info("获取到当前窗口title是：%s" %tt)
        return tt

    def get_screen(self, file_path):
        '''截图'''
        try:
            self.driver.get_screenshot_as_file(file_path)
            log1.info("截图保存成功，保存路径为：%s" %file_path)
        except Exception as e:
            log1.error("截图失败，原因：%s" %e)

    def wait(self,s):
        '''等待'''
        self.driver.implicitly_wait(s)

    def accpet(self):
        '''允许'''
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, fangfa, dingwei):
        '''切换框架'''
        try:
            self.element_wait(fangfa, dingwei)
            if1 = self.element(fangfa, dingwei)
            self.driver.switch_to.frame(if1)
            log1.info("切换frame成功")
        except Exception as e:
            log1.error("切换frame失败，原因：%s" %e)

    def asset(self, fangfa, dingwei):
        '''查找元素文本(断言用)'''
        try:
            self.element_wait(fangfa, dingwei)
            e1=self.element(fangfa, dingwei).text
            log1.info("断言成功")
            return e1
        except Exception as e:
            log1.error("断言失败，原因：%s" %e)