# coding=utf-8
from framework.base_page import BasePage


class IndexPage(BasePage):
    """
    ebooking 主页相关元素
    """
    wel_ass = "xpath=/html/body/div[1]/div[1]/div/ul/li[4]/a"  # 登录成功断言
    login_acc = "xpath=/html/body/div[1]/div[1]/div/ul/li[2]/ul/li/a"    # 当前登录用户

    # 验证登录是否成功
    def login_suss(self):
        return self.get_text(self.wel_ass)




