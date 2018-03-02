# coding=utf-8
from framework.base_page import BasePage
from pageobjects.gm_hotel.hotel_order import OnlinePay


class IndexPage(BasePage):
    """
    hotel 主页相关元素
    """
    wel_ass = "xpath=/html/body/aside/section/div[1]/div/div/a[2]"  # 登录成功断言
    login_acc = "xpath=/html/body/aside/section/div[1]/div/div/a[1]"    # 当前登录用户
    bill = 'xpath=/html/body/div[1]/div[2]/div/div/div[2]/div[1]/input'  # 订单编号输入框
    search_button = '/html/body/div[1]/div[2]/div/div/div[2]/div[3]/input'

    # 验证登录是否成功
    def login_suss(self):
        return self.get_text(self.wel_ass)

    # 订单查询
    def search_bill(self):
        self.find_element('link_text=订单查询')
        self.send_keys(self.bill, OnlinePay.get_billno)
        self.click(self.search_button)





