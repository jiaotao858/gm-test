# coding=utf-8
from framework.base_page import BasePage


class LoginPage(BasePage):
    """
    hotel 登录页面相关元素
    """
    hotel_url = "http://testhotel.hblckj.cn"
    acc_box = "xpath=/html/body/div[2]/div[2]/form/div[1]/input"    # 用户名输入框
    pwd_box = "xpath=/html/body/div[2]/div[2]/form/div[2]/input"    # 密码输入框
    entry_btn = "xpath=/html/body/div[2]/div[2]/form/div[4]/div/a"  # 登录按钮

    # 测试登录用户名和密码正确性时使用
    def login(self, acc, pwd):
        self.get(self.hotel_url)
        self.send_keys(self.acc_box, acc)
        self.send_keys(self.pwd_box, pwd)
        self.click(self.entry_btn)

    # 封装在setup中使用
    def common_login(self):
        self.get(self.hotel_url)
        self.send_keys(self.acc_box, "18640857881")
        self.send_keys(self.pwd_box, "jt123456")
        self.click(self.entry_btn)



