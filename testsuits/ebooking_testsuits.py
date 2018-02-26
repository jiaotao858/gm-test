# coding=utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.gm_ebooking.ebooking_index import IndexPage
from pageobjects.gm_ebooking.ebooking_login import LoginPage


class AdminLogin(unittest.TestCase):

    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_checkLogin(self):
        loginpage = LoginPage(self.driver)
        loginpage.login('18640857881', 'jt123456')
        indexpage = IndexPage(self.driver)
        self.assertEqual(indexpage.login_suss(), "帮助中心")

if __name__ == '__main__':
    unittest.main()



