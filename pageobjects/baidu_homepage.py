# coding=utf-8
from framework.base_page import BasePage


class LoginPage(BasePage):

    # input_box = "id=kw"
    # # search_submit_btn = "xpath=//*[@id='su']"
    # search_submit_btn = "xpath=//*[@id='u1']/a[1]"
    # us = "id=loginId"
    # ps = "id=passwordsss"
    # lg = "id=loginBtn"

    account = "xpath=/html/body/div[2]/div[2]/form/div[1]/input"
    pwd = "xpath=/html/body/div[2]/div[2]/form/div[2]/input"
    entry = "xpath=/html/body/div[2]/div[2]/form/div[4]/div/a"


    def login(self,acc,pw):
        self.send_keys(self.account,acc)
        self.send_keys(self.pwd,pw)
        self.click(self.entry)
        self.sleep(5)

