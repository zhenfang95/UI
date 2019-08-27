#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/8/26 16:30

import yaml
from comm import pubilc

def getRead(title,name):
    '''读取yaml文件数据'''
    path=pubilc.get_cwd()
    readfile=open(path+"\\data\\page_data.yaml","r",encoding="utf-8")
    dict1=yaml.load(readfile)
    data=dict1[title].get(name)
    return data
