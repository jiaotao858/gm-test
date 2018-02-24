# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import LoginPage


class BaiduSearch(unittest.TestCase):

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)


    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.quit()


    def test_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        loginPage = LoginPage(self.driver)

        loginPage.login('18640857881','jt123456')
        # try:
        #     assert '首页' in loginPage.get_title()  # 调用页面对象继承基类中的获取页面标题方法
        #     print('Test Pass.')
        # except Exception as e:
        #     print('Test Fail.', format(e))
        a = loginPage.get_title()
        self.assertEqual("首页11", a)

    def test_search2(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        loginPage = LoginPage(self.driver)

        loginPage.login('18640857881','jt123456')
        # try:
        #     assert '首页' in loginPage.get_title()  # 调用页面对象继承基类中的获取页面标题方法
        #     print('Test Pass.')
        # except Exception as e:
        #     print('Test Fail.', format(e))
        # assert '首页' in loginPage.get_title()
        a = loginPage.get_title()
        self.assertEqual("首页", a)

if __name__ == '__main__':
    unittest.main()



