# coding=utf-8
from framework.base_page import BasePage


class HomePage(BasePage):

    input_box = "id=kw"
    # search_submit_btn = "xpath=//*[@id='su']"
    search_submit_btn = "xpath=//*[@id='u1']/a[1]"
    us = "id=loginId"
    ps = "id=password"
    lg = "id=loginBtn"

    def login(self):
        self.send_keys(self.us,'guo')
        self.send_keys(self.ps,'ts123456')
        self.click(self.lg)
