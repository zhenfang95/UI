#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/8/27 15:15

import os
import configparser
from comm import pubilc

path=pubilc.get_cwd()+"\\config"
config_path=os.path.join(path,"config.ini")
config=configparser.ConfigParser()
config.read(config_path)

smtp_server=config.get("email","smtp_server")
port=config.get("email","port")
sender=config.get("email","sender")
psw=config.get("email","psw")
receiver=config.get("email","receiver")
username=config.get("email","username")

