# coding=utf-8
from framework.base_page import BasePage


class IndexPage(BasePage):
    """
    hotel 主页相关元素
    """
    wel_ass = "xpath=/html/body/div[2]/div/div/span[1]"  # 登录成功断言
    login_acc = "xpath=/html/body/div[2]/div/div/span[2]"    # 当前登录用户
    jd = "xpath=/html/body/div[2]/div/ul/li[3]/a"

    # 验证登录是否成功
    def login_suss(self):
        return self.get_text(self.wel_ass)

    # 跳转至酒店列表页
    def goto_hotellist(self):
        self.wait(10)
        # self.find_element("xpath=/html/body/div[2]/div/ul/li[3]/a")
        # self.click("link_text=旅游线路")
        # self.f5()
        # self.sleep(10)





