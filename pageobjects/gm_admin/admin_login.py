# coding=utf-8
from framework.base_page import BasePage


class LoginPage(BasePage):
    """
    admin 登录页面相关元素
    """
    admin_url = "http://testadmin.hblckj.cn"
    acc_box = "id=loginId"    # 用户名输入框
    pwd_box = "id=password"    # 密码输入框
    entry_btn = "id=loginBtn"  # 登录按钮

    # 测试登录用户名和密码正确性时使用
    def login(self, acc, pwd):
        self.get(self.admin_url)
        self.send_keys(self.acc_box, acc)
        self.send_keys(self.pwd_box, pwd)
        self.click(self.entry_btn)

    # 封装在setup中使用
    def common_login(self, acc, pwd):
        self.get(self.admin_url)
        self.send_keys(self.acc_box, 'guo')
        self.send_keys(self.pwd_box, 'ts123456')
        self.click(self.entry_btn)



