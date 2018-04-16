# -*- coding:UTF-8 -*-

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    print(mail_body)
    f.close()
    msg =  MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header('麦田在线自动化测试报告','utf-8')

   # smtp = smtplib.SMTP()
   # smtp.connect('smtp.qq.com')
    smtp = smtplib.SMTP('smtp.qq.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login("1508430602@qq.com","englxtanrphjidaj")
    smtp.sendmail("1508430602@qq.com","wyfzgr@163.com",msg.as_string())
    smtp.quit()
    print("发送成功")

def new_report(testreport):
    #path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    #result_dir = path + '/report/'
    # 将文件都放到一个数组中
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport + "/" + fn))
    file_new = os.path.normpath(os.path.join(testreport,lists[-1]))
    #print(file_new)
    send_mail(file_new)
    #return file_new

if __name__=="__main__":
    test_report = "G:/Web_MaiTianOnLineAutoTest/report"
    new_report = new_report(test_report)
    #send_mail(new_report)