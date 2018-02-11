# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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

    # 设置浏览器尺寸
    def set_window_size(self, wide, high):
        self.driver.set_window_size(wide, high)
        logger.info("Set browser window wind:%d high:%d" %(wide, high))

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Close and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s." % e)

    # 保存图片
    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath(".")) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("ad take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    # 定位元素方法
    def find_element(self, selector):
        element = ''
        if '=' not in selector:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        selector_by = selector.split('=')[0]
        selector_value = selector.split('=')[1]

        if selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                print(type(element))
                logger.info("Had find the element \' %s \' successful " 
                            "by: %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.info("NoSuchElementException: %s" %e)
                self.get_windows_img()

        elif selector_by == 'name':
            try:
                element = self.driver.find_element(By.NAME, selector_value)
                logger.info("Had find the element \' %s \' successful " 
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.info("NoSuchElementException: %s" %e)
                self.get_windows_img()

        elif selector_by == 'class_name':
            try:
                element = self.driver.find_element(By.CLASS_NAME, selector_value)
                logger.info("Had find the element \' %s \' successful " 
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.info("NoSuchElementException: %s" %e)
                self.get_windows_img()

        elif selector_by == 'link_text':
            try:
                element = self.driver.find_element(By.LINK_TEXT,selector_value)
                logger.info("Had find the element \' %s \' successful " 
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.info("NoSuchElementException: %s" %e)
                self.get_windows_img()

        elif selector_by == 'partial_link_text':
            try:
                element = self.driver.find_element(By.PARTIAL_LINK_TEXT, selector_value)
                logger.info("Had find the element \' %s \' successful " 
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.info("NoSuchElementException: %s" %e)
                self.get_windows_img()

        elif selector_by == 'tag_name':
            try:
                element = self.driver.find_element(By.TAG_NAME, selector_value)
                logger.info("Had find the element \' %s \' successful " 
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.info("NoSuchElementException: %s" %e)
                self.get_windows_img()

        elif selector_by == 'xpath':
            try:
                element = self.driver.find_element(By.XPATH, selector_value)
                logger.info("Had find the element \' %s \' successful " 
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.info("NoSuchElementException: %s" %e)
                self.get_windows_img()

        elif selector_by == 'css_selector':
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, selector_value)
                logger.info("Had find the element \' %s \' successful " 
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.info("NoSuchElementException: %s" %e)
                self.get_windows_img()

        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpaht','css'.")

        return element

    # 等待元素出现
    def wait_element(self, selector, seconds=10):
        if '=' not in selector:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        selector_by = selector.split('=')[0]
        selector_value = selector.split('=')[1]

        if selector_by == "id":
            try:
                WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.ID, selector_value)),
                                                           '通过%s,Dom树中未查找到该元素' % selector_value)
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)

        elif selector_by == "name":
            try:
                WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.NAME, selector_value)),
                                                           '通过%s,Dom树中未查找到该元素' % selector_value)
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)

        elif selector_by == "class_name":
            try:
                WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((
                    By.CLASS_NAME, selector_value)),'通过%s,Dom树中未查找到该元素' % selector_value)
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)

        elif selector_by == "link_text":
            try:
                WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((
                    By.LINK_TEXT, selector_value)),'通过%s,Dom树中未查找到该元素' % selector_value)
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)

        elif selector_by == "partial_link_text":
            try:
                WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((
                    By.PARTIAL_LINK_TEXT, selector_value)),'通过%s,Dom树中未查找到该元素' % selector_value)
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)

        elif selector_by == "tag_name":
            try:
                WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((
                    By.TAG_NAME, selector_value)),'通过%s,Dom树中未查找到该元素' % selector_value)
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)

        elif selector_by == "xpath":
            try:
                WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((
                    By.XPATH, selector_value)),'通过%s,Dom树中未查找到该元素' % selector_value)
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)

        elif selector_by == "css_selector":
            try:
                WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((
                    By.CSS_SELECTOR, selector_value)),'通过%s,Dom树中未查找到该元素' % selector_value)
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpaht','css'.")

    # 输入
    def type(self, selector, text):

        self.wait_element(selector)
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \'%s\' inputBox" %text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    # 清除文本框
    def clear(self, selector):

        self.wait_element(selector)
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    #点击元素
    def click(self,selector):

        self.wait_element(selector)
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 获取网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    # 固定休眠
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)



