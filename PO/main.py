# /!/usr/bin/python3
# *-*coding-utf8*-*
# Name:main
# Author:Administrator
# Time:2019/12/6
import unittest
import os
from common.HTMLTestRunner import HTMLTestRunner
from common.dir_config import *

s=unittest.TestSuite()
loader=unittest.TestLoader()
s.addTests(loader.discover(testcases_dir))
fp=open(htmlreport_dir+"/autoTest_report.html",'wb')
runner=HTMLTestRunner(
    stream=fp,
    title="测试报告",
    description='单元测试报告'
)
runner.run(s)