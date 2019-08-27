#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/8/26 17:50

import unittest,time
from comm.pubilc import *
from comm.sele_brower import PySele
from comm.read_yaml import *

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.ps=PySele("Firefox")

    def test_baiduSo(self):
        '''百度搜索'''
        self.ps.open(getRead("baidu","url"))
        self.ps.wait(5)
        self.ps.clear("id",getRead("baidu","so"))
        self.ps.send_key("id",getRead("baidu","so"),getRead("baidu","send"))
        self.ps.click("id",getRead("baidu","so_btm"))
        time.sleep(5)
        self.ps.get_screen(dir_screen("百度搜索截图"))

    def tearDown(self):
        self.ps.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)