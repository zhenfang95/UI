# /!/usr/bin/python3
# *-*coding-utf8*-*
# Name:login_page_locatosr
# Author:Administrator
# Time:2019/12/5
from selenium.webdriver.common.by import By

class LoginPageLocator:
    user_loc = (By.XPATH, "//*[@name='phone']")
    passwd_loc = (By.XPATH, "//*[name='password']")
    login_button_loc = (By.XPATH, "//button")
    pageCenter_loc = (By.XPATH, "div[@class='form-error-info]")
    loginArea_loc = (By.XPATH, "//div[@class='error-info']")

