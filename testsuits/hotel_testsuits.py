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

    @unittest.skip("专门测试登录时使用")
    def test_checkLogin(self):
        loginpage = LoginPage(self.driver)
        loginpage.login('18640857881', 'jt123456')
        indexpage = IndexPage(self.driver)
        self.assertEqual(indexpage.login_suss(), "欢迎您！")
        indexpage.goto_hotellist()

    # 查询酒店
    def test_searchHotel(self):

        # loginpage = LoginPage(self.driver)
        # loginpage.common_login()
        indexpage = IndexPage(self)
        indexpage.goto_hotellist()
        # self.driver.find_element_by_xpath("/html/body/div[2]/div/ul/li[3]/a").click()       # 跳转至酒店页
        searchhotel = HotelListPage(self.driver)
        searchhotel.search_hotel()
        self.assertEqual(searchhotel.search_suss(), "唐山迪士尼")


if __name__ == '__main__':
    unittest.main()



