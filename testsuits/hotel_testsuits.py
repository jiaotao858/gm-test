# coding=utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.gm_hotel.hotel_login import LoginPage
from pageobjects.gm_hotel.hotel_index import IndexPage
from pageobjects.gm_hotel.hotel_hotellist import HotelListPage


class HotelLogin(unittest.TestCase):

    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        loginpage = LoginPage(self.driver)
        loginpage.common_login()

    def tearDown(self):
        self.driver.quit()

    @unittest.skip
    def test_checkLogin(self):
        loginpage = LoginPage(self.driver)
        loginpage.login('18640857881', 'jt123456')
        indexpage = IndexPage(self.driver)
        self.assertEqual(indexpage.login_suss(), "欢迎您！")

    def test_searchHotel(self):
        loginpage = LoginPage(self.driver)
        loginpage.common_login()
        searchhotel = HotelListPage(self.driver)
        searchhotel.search_hotel()

if __name__ == '__main__':
    unittest.main()



