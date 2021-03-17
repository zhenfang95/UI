# /!/usr/bin/python3
# *-*coding-utf8*-*
# Name:test_login
# Author:Administrator
# Time:2019/12/5
from selenium import webdriver
import unittest
import ddt
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas import Global_Datas as gd
from TestDatas import login_datas as ld


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Firefox()
        cls.driver.get(gd.web_login)
        cls.lp=LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


    # def setUp(self) -> None:
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://www.baidu.com")
    #     self.lp=LoginPage(self.driver)

    def tearDown(self) -> None:
        self.driver.refresh()

    # 正常案例
    def test_login_success(self):
        # 前置：
        # 步骤
        self.lp.login(ld.success['user'], ld.success['passwd'])

        self.assertTrue(IndexPage(self.driver).check_user_ele_exists())

    # 异常案例
    @ddt.data(*ld.wrong_datas)
    def test_login_noPassword(self,data):
        self.lp.login(data["user"],data["passwd"])
        self.assertEqual(self.lp.get_errorMsg(),data['check'])

if __name__ == '__main__':
    unittest.main()