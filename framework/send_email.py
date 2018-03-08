#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: taojiaoa
@software: PyCharm
@file: demo03.py
@time: 2018/3/8 10:56

邮件发送功能
"""
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

dir = os.path.dirname(os.path.abspath('.'))
test_dir = dir + '/testsuits'
test_report_dir = dir + '/test_report'

# 取最新测试报告
def new_file(test_dir):
    dir = os.path.dirname(os.path.abspath('.'))
    test_report_dir = dir + '/test_report'
    # 列举test_dir目录下的所有文件，结果以列表形式返回。
    lists = os.listdir(test_report_dir)
    # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn: os.path.getmtime(test_report_dir + '\\' + fn))
    # 获取最新文件的绝对路径
    file_path = os.path.join(test_report_dir, lists[-1])
    return file_path


# 发送邮件，发送最新测试报告html
def send_email(newfile):
    f = open(newfile, 'rb')
    mail_body = f.read()
    f.close()

    # 邮件服务器配置
    smtpserver = 'smtp.163.com'
    sender = 'jxjt_1990@163.com'
    receiver = ['314782553@qq.com']
    # 登录账户
    user = 'jxjt_1990@163.com'
    password = 'Wohuai85849188'
    # 邮件主题
    subject = '自动定时发送测试报告20160808'

    # 邮件对象
    msg = MIMEMultipart('mixed')
    msg['From'] = 'jxjt_1990@163.com <jxjt_1990@163.com>'
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject, 'utf-8')

    # 邮件正文（html类型）
    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)

    # 附件一（测试报告）
    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)

    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


# if __name__ == '__main__':
#     print('=====AutoTest Start======')
#     discover = unittest.defaultTestLoader.discover(test_dir, pattern='hotel_*.py')
#     # suite = unittest.TestLoader().discover(test_dir, pattern='hotel_*.py')
#     now = time.strftime('%Y-%m-%d_%H_%M_%S_')
#     filename = test_report_dir + '\\' + now + 'result.html'
#     fp = open(filename, 'wb')
#     # 需屏蔽fp中的中文文字说明。否则在windows下执行会报：UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 553: ordinal not in range(128)
#     runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
#     runner.run(discover)
#     # 注意：调用函数一定要加括号，一个括号害死个人，哎，查了几天的问题，才发现导致html文件始终显示空白，就是因为close函数调用不正确，漏了括号。
#     fp.close()
#
#     # 2.取最新测试报告
#     new_report = new_file(test_report_dir)
#     # 调试用的
#     #    print new_report
#
#     # 3.发送邮件，发送最新测试报告html
#     send_email(new_report)
#     print('=====AutoTest Over======')
