# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
import os
import time
import unittest
from testsuits.hotel_testsuits import HotelLogin
from framework import again_execute
from framework.send_email import send_email,new_file

# 项目相对路径
dir = os.path.dirname(os.path.abspath('.'))
# 测试报告保存路径
test_report_dir = dir + '/test_report/'
# 用例执行路径
test_dir = dir +'/testsuits/'

# 获取系统当前时间
now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式"HTMLtemplate.html"
HtmlFile = test_report_dir + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")

# 执行特定用例（执行失败重跑）
# suite = unittest.TestSuite()
suit = again_execute.Suit()
suit.addTest(HotelLogin('test_search1'))
# suite.addTest(HotelLogin('test_search1'))


# 执行所有用例
# suite = unittest.defaultTestLoader().discover(test_dir, pattern='test_*.py')

def createsuite():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)
    print(discover)
    for test_suite in discover:
        for testsuit in test_suite:
            testunit.addTest(testsuit)
    return testunit
# alltestnames = createsuite()

if __name__ == '__main__':
    print('=====AutoTest Start======')
    runner = HTMLTestRunner(stream=fp, title="测试项目报告", description="用例测试情况", verbosity=2)
    # runner = unittest.TextTestRunner(verbosity=2)
    runner.run(createsuite())
    fp.close()

    # 2.取最新测试报告
    new_report = new_file(test_report_dir)

    # 3.发送邮件，发送最新测试报告html
    send_email(new_report)
    print('=====AutoTest Over======')

