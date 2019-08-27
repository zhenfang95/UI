#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/8/26 16:10

import os
def get_cwd():
    '''文件路径'''
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path

def dir_screen(name):
    '''截图存放路径'''
    path=get_cwd()+"\\resultpng\\"+name+".png"
    return path
