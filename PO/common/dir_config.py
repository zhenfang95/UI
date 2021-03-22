# /!/usr/bin/python3
# *-*coding-utf8*-*


import os
base_dir=os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir=os.path.join(base_dir,"TestDatas")

testcases_dir=os.path.join(base_dir,"TestCases")

htmlreport_dir=os.path.join(base_dir,"Outputs/report")
logs_dir=os.path.join(base_dir,"Outputs/logs")
screenshot_dir=os.path.join(base_dir,"Outputs/screenshots")