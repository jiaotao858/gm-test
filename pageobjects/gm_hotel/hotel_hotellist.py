# coding=utf-8
from framework.base_page import BasePage


class HotelListPage(BasePage):
    """
    hotel 酒店列表页
    """
    destination = "xpath=/html/body/div[3]/div/div/form/div/div[1]/div[1]/input"  # 目的地
    checkinTime = "id=checkinDate"    # 入住时间
    checkoutTime = "id=checkoutDate"    # 离店时间
    hotelName = "xpath=/html/body/div[3]/div/div/form/div/div[1]/input"     # 酒店名称
    searchButton = "xpath=/html/body/div[3]/div/div/form/div/div[1]/button"     # 搜索按钮
    searchResult = "xpath=/html/body/div[3]/div/div/div/div/div[1]/div[2]/h2/a"     # 酒店查询结果

    # 查询酒店
    def search_hotel(self):
        self.send_keys(self.destination, "唐山")
        self.js("document.getElementById('checkinDate').removeAttribute('readonly')")
        self.send_keys(self.checkinTime, "2018-02-01")
        self.js("document.getElementById('checkoutDate').removeAttribute('readonly')")
        self.send_keys(self.checkoutTime, "2018-02-03")
        self.send_keys(self.hotelName, "唐山迪士尼")
        self.click(self.searchButton)
        self.sleep(2)

    # 查询酒店搜索结果
    def search_suss(self):
        return self.get_text(self.searchResult)









