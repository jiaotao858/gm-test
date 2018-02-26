# coding=utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.gm_admin.admin_index import IndexPage
from pageobjects.gm_admin.admin_login import LoginPage


class AdminLogin(unittest.TestCase):

    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_checkLogin(self):
        loginpage = LoginPage(self.driver)
        loginpage.login('guo', 'ts123456')
        indexpage = IndexPage(self.driver)
        self.assertEqual(indexpage.login_suss(), "退出")

if __name__ == '__main__':
    unittest.main()



