# coding=utf-8
import HTMLTestRunner
import os
import time
import unittest
from testsuits.hotel_testsuits import HotelLogin
from framework import again_execute

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.'))+'/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式"HTMLtemplate.html"
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")

# 执行特定用例
# suite = unittest.TestSuite()
suit = again_execute.Suit()
suit.addTest(HotelLogin('test_search1'))
# suite.addTest(HotelLogin('test_search1'))

# test_dir = 'C:\\Users\\allonshore\\PycharmProjects\\gm-test\\testsuits\\hotel_testsuits.py'


# 执行所有用例
# suite = unittest.TestLoader().discover(test_dir, pattern='test*.py')


if __name__ == '__main__':
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试项目报告", description="用例测试情况")
    # runner = unittest.TextTestRunner()
    runner.run(suit)
    fp.close()

