# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os.path
from framework.logger import Logger

# create a logger instance
logger = Logger(logger="BasePage").getlog()

class BasePage(object):
    """
    页面基本类
    """

    def __init__(self, driver):
        self.driver = driver

    # 退出浏览器并结束用例
    def quit_browser(self):
        self.driver.quit()
        logger.info("Quit browser and end testing.")

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forword on current page.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Close and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s." % e)

    # 保存图片
    def get_windows_img(self):
        file_path = os.path.dirname(os.path(".")) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M'),time.localtime(time.time())
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("ad take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()


    # 定位元素方法
    def find_element(self, selector):
        pass

    # 输入
    def type(self, selector, text):
        pass

    # 清除文本框
    def clear(self, selector):
        pass

    #点击元素
    def click(self,selector):
        pass

    # 获取网页标题
    def get_page_title(self):
        pass

    # 固定休眠
    @staticmethod
    def sleep(seconds):
        pass



