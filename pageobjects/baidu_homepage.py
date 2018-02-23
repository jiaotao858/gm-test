# coding=utf-8
from framework.base_page import BasePage


class HomePage(BasePage):

    input_box = "id=kw"
    # search_submit_btn = "xpath=//*[@id='su']"
    search_submit_btn = "xpath=//*[@id='u1']/a[1]"
    us = "id=loginId"
    ps = "id=passwordsss"
    lg = "id=loginBtn"
    #
    # def type_search(self, text):
    #     self.type(self.input_box, text)
    #
    # def send_submit_btn(self):
    #     self.click(self.search_submit_btn)
    #
    # def clear_search(self):
    #     self.clear(self.input_box)

    def login(self):
        self.type(self.us, 'guo')
        self.type(self.ps, 'ts123456')
        self.click(self.lg)
