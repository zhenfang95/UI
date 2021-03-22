# /!/usr/bin/python3
# *-*coding-utf8*-*

import logging
import time
from common import dir_config

def get_log(logger_name):
    # 创建一个logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # 设置日志存放路径，日志文件名
    # 获取本地时间，转换为设置的格式
    curTime=time.strftime("%Y-%m-%d",time.localtime())
    # 设置所有日志存放路径
    path = dir_config.logs_dir
    log_name = path + "/Web_Autotest_{0}.log".format(curTime)

    # 创建handler
    # 创建一个handler写入所有日志
    fh = logging.FileHandler(log_name,encoding='utf-8')
    fh.setLevel(logging.INFO)
    # 创建一个handler输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # 定义日志输出格式
    # 以时间-日志器名称-日志级别-日志内容的形式展示
    all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 将定义好的输出形式添加到handler
    fh.setFormatter(all_log_formatter)
    ch.setFormatter(all_log_formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

log1=get_log("Web_Autotest")
