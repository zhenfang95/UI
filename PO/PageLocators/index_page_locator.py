# /!/usr/bin/python3
# *-*coding-utf8*-*
# Name:index_page_locator
# Author:Administrator
# Time:2019/12/5
from selenium.webdriver.common.by import By

class IndexPageLocator:
    user_link=(By.XPATH,"//a[contains(text(),’我的账户‘)]")

    home=(By.XPATH,"//a[text()='首页']")
