#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/8/27 15:36

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from comm import pubilc,read_config
from comm.logs import log1
import time,os

time1=time.strftime("%Y%m%d",time.localtime(time.time())) #获取本地时间
sender=read_config.sender  #发件人邮箱账号
psw=read_config.psw        #发件人邮箱密码
username=read_config.username #发件人姓名
users_email=read_config.receiver  #收件人邮箱

path=pubilc.get_cwd()
file=os.path.join(path,'report/最新UI自动化测试报告.html')

def mail():
    try:
        #创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = formataddr([username,sender]) #发件人邮箱昵称、发件人邮箱账号
        log1.info('发件人姓名：%s' % username)
        log1.info('发件人邮箱：%s' %sender)
        message['To'] = ';'.join(users_email)  #收件人的邮箱，存在多个邮箱用“;”分离
        log1.info('收件人邮箱：%s'%users_email)
        message['Subject'] = time1 + "最新UI自动化测试报告"  #邮件主题

        #邮件正文内容
        message.attach(MIMEText('附件为最新UI自动化测试报告','plain','utf-8'))

        #添加附件
        att = MIMEText(open(file,'rb').read(),'base64','utf-8')
        log1.info('读取附件')
        att['Content-Type'] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att.add_header("Content-Disposition", "attachment", filename=("gbk", "", "最新UI自动化框架测试报告.html"))
        # 附件名称非中文时的写法
        # att["Content-Disposition"] = 'attachment; filename="test.html")'
        message.attach(att)
        log1.info('添加附件')

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
        log1.info('连接QQ邮箱smtp服务')
        server.login(sender, psw)  # 括号中对应的是发件人邮箱账号、邮箱密码
        log1.info('连接成功')
        server.sendmail(sender, users_email, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        log1.info("邮件发送成功")

    except Exception as e:
        log1.error("邮件发送失败,异常信息：%s" %e)


