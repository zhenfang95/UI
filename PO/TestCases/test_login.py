# /!/usr/bin/python3
# *-*coding-utf8*-*

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
        cls.driver=webdriver.Chrome()
        cls.driver.get(gd.base_url)
        cls.lp=LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


    # 正常案例
    def test_login_success(self):
        # 前置：
        # 步骤
        self.lp.login(ld.success['user'], ld.success['passwd'])
        #断言
        #self.assertTrue(IndexPage(self.driver).check_user_ele_exists())

    # 异常案例
    @ddt.data(*ld.wrong_datas)
    def test_login_noPassword(self,data):
        self.lp.login(data["user"],data["passwd"])
        #self.assertEqual(self.lp.get_errorMsg(),data['check'])

if __name__ == '__main__':
    unittest.main()