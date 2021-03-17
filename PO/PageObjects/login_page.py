# /!/usr/bin/python3
# *-*coding-utf8*-*
# Name:login_page
# Author:Administrator
# Time:2019/12/5
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.login_page_locatosr import LoginPageLocator as loc
from common.basepage import BasePage


class LoginPage(BasePage):

    def login(self,username,password):
        # 等待元素出现
        self.wait_eleVisible(loc.user_loc,doc="等待密码框出现")
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.user_loc))
        # 输入账号
        self.input_text(loc.user_loc,username,doc="登陆页面输入用户名")
        self.wait_eleVisible(loc.user_loc,password,doc="等待密码框出现")
        self.input_text(loc.user_loc,password,doc="输入用户名密码")
        # self.driver.find_element(*loc.user_loc).send_keys(username)
        self.click(loc.login_button_loc,doc="点击登陆按钮")

        # WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(loc.passwd_loc))

        # 输入密码
        # self.driver.find_element(*loc.passwd_loc).send_keys(password)
        #
        # self.driver.find_element(*loc.login_button_loc).click()
    # 获取登陆区错误信息
    def  get_errorMsg(self):
        self.wait_eleVisible(loc.loginArea_loc)
        # WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.loginArea_loc))
        # return self.driver.find_element(*loc.loginArea_loc).text
        return self.get_element(loc.loginArea_loc,doc="dddd")
    def get_error_pageMsg(self):
        WebDriverWait(self.driver,30,0.1).until(EC.visibility_of_element_located(loc.pageCenter_loc))
        return self.driver.find_element(*loc.pageCenter_loc).text