# coding=utf-8
from framework.base_page import BasePage


class LoginPage(BasePage):
    """
    ebooking 登录页面相关元素
    """
    ebooking_url = "http://testebooking.hblckj.cn"
    acc_box = "id=loginId"    # 用户名输入框
    pwd_box = "id=password"    # 密码输入框
    entry_btn = "xpath=/html/body/div[1]/div[2]/div/div/div[1]/button"  # 登录按钮

    def login(self, acc, pwd):
        self.get(self.ebooking_url)
        self.send_keys(self.acc_box, acc)
        self.send_keys(self.pwd_box, pwd)
        self.click(self.entry_btn)



