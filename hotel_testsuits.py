# coding=utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.gm_hotel.hotel_login import LoginPage
from pageobjects.gm_hotel.hotel_index import IndexPage
from pageobjects.gm_hotel.hotel_hotellist import HotelListPage
from pageobjects.gm_hotel.hotel_order import FillOrderPage,OnlinePay,GoToAdmin

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
    def test_search1(self):
        """验证酒店查询是否正确"""
        indexpage = IndexPage(self.driver)
        indexpage.goto_hotellist()       # 跳转至酒店列表页
        hotellist = HotelListPage(self.driver)
        hotellist.search_hotel()
        self.assertEqual(hotellist.search_suss(), "唐山迪士尼")
        hotellist.book_room()
        # fillorder = FillOrderPage(self.driver)
        # fillorder.fill_order()
        # fillorder.pay_style(1)
        # fillorder.submit_order()
        # onlinepage = OnlinePay(self.driver)
        # onlinepage.get_billno()
        # gotoadmin = GoToAdmin(self.driver)
        # gotoadmin.goto_admin()

    # 查询酒店
    def test_search2(self):
        """测试数据2"""
        indexpage = IndexPage(self.driver)
        indexpage.goto_hotellist()  # 跳转至酒店列表页

if __name__ == '__main__':
    unittest.main()



