# /!/usr/bin/python3
# *-*coding-utf8*-*

from selenium.webdriver.common.by import By

class IndexPageLocator:
    user_link=(By.XPATH,"//a[contains(text(),’我的账户‘)]")
    home=(By.XPATH,"//a[text()='首页']")
