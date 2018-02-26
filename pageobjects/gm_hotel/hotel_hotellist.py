# coding=utf-8
from framework.base_page import BasePage


class HotelListPage(BasePage):
    """
    hotel 酒店列表页
    """
    destination = "xpath=/html/body/div[3]/div/div/form/div/div[1]/div[1]/input"  # 目的地
    checkinTime = "xpath=//*[@id='checkinDate']"    # 入住时间
    checkoutTime = "xpath=//*[@id='checkoutDate']"    # 离店时间
    hotelName = "xpath=/html/body/div[3]/div/div/form/div/div[1]/input" # 酒店名称
    searchButton = "xpath=/html/body/div[3]/div/div/form/div/div[1]/button" # 搜索按钮

    # 验证登录是否成功
    def search_hotel(self):
        self.send_keys(self.destination,"唐山")
        js = "document.getElementById('checkinDate').removeAttribute('readonly')"
        self.driver.js(js)
        self.send_keys(self.checkinTime, "2018-02-02")
        self.sleep(5)





