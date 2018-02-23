# coding=utf-8
from framework.base_page import BasePage


class HomePage(BasePage):

    input_box = "id=kw"
    # search_submit_btn = "xpath=//*[@id='su']"
    search_submit_btn = "xpath=//*[@id='u1']/a[1]"
    us = "id=loginId"
    ps = "id=passwordsss"
    lg = "id=loginBtn"

    def login(self):
<<<<<<< HEAD
        self.type(self.us, 'guo')
        self.type(self.ps, 'ts123456')
=======
        self.send_keys(self.us,'guo')
        self.send_keys(self.ps,'ts123456')
>>>>>>> 4b5552dfeffb694370abfbeb9e3cea9f870c6bd4
        self.click(self.lg)
