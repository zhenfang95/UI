# /!/usr/bin/python3
# *-*coding-utf8*-*
# Name:logger
# Author:Administrator
# Time:2019/12/5
import logging
from logging.handlers import RotatingFileHandler
import os
import time
from common import dir_config
fmt="%(asctime)s %(levelname)s %(filename)s %(funcName)s [line:%(lineno)d ] %(message)"
datefmt='%a,%b,%Y,%H:%M:%S'
handler_1=logging.StreamHandler()
curTime=time.strftime("%Y-%m-%d",time.localtime())
handler_2=RotatingFileHandler(dir_config.logs_dir+"/Web_Autotest_{0}.log".format(curTime),backupCount=20,encoding='utf-8')
logging.basicConfig(fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_1,handler_2])
logging.info("hehehe")