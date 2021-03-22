# /!/usr/bin/python3
# *-*coding-utf8*-*

from selenium.webdriver.common.by import By

class LoginPageLocator:
    user_loc = (By.XPATH, "//input[@name='username']")
    passwd_loc = (By.XPATH, "//input[@name='password']")
    login_button_loc = (By.XPATH, "//button")
    pageCenter_loc = (By.XPATH, "div[@class='form-error-info]")
    loginArea_loc = (By.XPATH, "//div[@class='error-info']")

