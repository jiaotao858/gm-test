# coding=utf-8
from framework.base_page import BasePage


class FillOrderPage(BasePage):
    """
    hotel 酒店预订页
    """
    addroom = "partial_link_text=+"  # 增加房间
    reduceroom = "partial_link_text=-"  # 减少房间
    linkname = "xpath=/html/body/div[3]/div/form/div[2]/ul/li[1]/div/input"  # 联系人
    linkphone = 'xpath=/html/body/div[3]/div/form/div[2]/ul/li[2]/div/input'  # 联系人手机号
    checkinname = 'xpath=/html/body/div[3]/div/form/div[3]/ul/li[1]/div/input'    # 入住人
    checkinphone = 'xpath=/html/body/div[3]/div/form/div[3]/ul/li[2]/div/input'   # 入住人手机号
    note = 'xpath=/html/body/div[3]/div/form/div[4]/ul/li/div/textarea'   # 订单备注
    account_pay = 'xpath=/html/body/div[3]/div/form/div[6]/div[2]/label[1]'
    zhifubao_pay = 'xpath=/html/body/div[3]/div/form/div[6]/div[2]/label[2]'
    weinxin_pay = 'xpath=/html/body/div[3]/div/form/div[6]/div[2]/label[3]'
    submit_button = 'xpath=/html/body/div[3]/div/form/div[6]/div[3]/button'    # 提交订单按钮

    # 查询酒店
    def fill_order(self):
        # self.send_keys(self.linkname, "正常流程测试")
        # self.send_keys(self.linkphone, "18640857881")
        self.send_keys(self.checkinname, "正常流程测试")
        self.send_keys(self.checkinphone, "18640857881")
        self.send_keys(self.note, "此处为订单备注")

    # 选择支付方式
    def pay_style(self,No): # （0.账户支付 1.支付宝 2.微信）
        if No == 0:
            self.click(self.account_pay)
        elif No == 1:
            self.click(self.zhifubao_pay)
        else:
            self.click(self.weinxin_pay)

    # 提交订单按钮
    def submit_order(self):
        self.click(self.submit_button)
        self.sleep(2)

class OnlinePay(BasePage):
    order_success = ''
    bill = 'xpath=/html/body/div[3]/div/form/div/div[2]/div/div[1]/div[2]'

    def get_billno(self):
        msg = self.get_text(self.bill)
        billno = msg.split('：')[1]
        print(billno)
        return billno

class PaySuccess(BasePage):
    pass


class GoToAdmin(BasePage):

    # @staticmethod
    def goto_admin(self):
        self.open_new_tag('http://testadmin.hblckj.cn')










