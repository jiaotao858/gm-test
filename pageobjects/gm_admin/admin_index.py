# coding=utf-8
from framework.base_page import BasePage


class IndexPage(BasePage):
    """
    hotel 主页相关元素
    """
    wel_ass = "xpath=/html/body/aside/section/div[1]/div/div/a[2]"  # 登录成功断言
    login_acc = "xpath=/html/body/aside/section/div[1]/div/div/a[1]"    # 当前登录用户

    # 验证登录是否成功
    def login_suss(self):
        return self.get_text(self.wel_ass)




