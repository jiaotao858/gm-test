# coding=utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.gm_hotel.hotel_login import LoginPage


class HotelLogin(unittest.TestCase):

    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        loginpage = LoginPage(self.driver)
        loginpage.login('18640857881', 'jt123456')
        a = self.driver.find_element("xpath=/html/body/div[2]/div/div/span[2]").text
        self.assertEqual(a, "11111", "登录失败")

if __name__ == '__main__':
    unittest.main()



