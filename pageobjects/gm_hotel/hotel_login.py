# coding=utf-8
from framework.base_page import BasePage


class LoginPage(BasePage):
    """
    hotel 登录页面相关元素
    """
    acc_box = "xpath=/html/body/div[2]/div[2]/form/div[1]/input"
    pwd_box = "xpath=/html/body/div[2]/div[2]/form/div[2]/input"
    entry_btn = "xpath=/html/body/div[2]/div[2]/form/div[4]/div/a"
    login_acc = "xpath=/html/body/div[2]/div/div/span[2]"

    def login(self, acc, pwd):
        self.send_keys(self.acc_box, acc)
        self.send_keys(self.pwd_box, pwd)
        self.click(self.entry_btn)



