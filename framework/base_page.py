# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
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
        if '=' not in selector:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        selector_by = selector.split('=')[0]
        selector_value = selector.split('=')[1]

        if selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
            logger.info("Had find the element successful by: %s via value: %s "
                        % (selector_by, selector_value))

        elif selector_by == 'name':
            element = self.driver.find_element(By.NAME, selector_value)
            logger.info("Had find the element successful by: %s via value: %s "
                        % (selector_by, selector_value))

        elif selector_by == 'class_name':
            element = self.driver.find_element(By.CLASS_NAME, selector_value)
            logger.info("Had find the element successful by: %s via value: %s "
                        % (selector_by, selector_value))

        elif selector_by == 'link_text':
            element = self.driver.find_element(By.LINK_TEXT, selector_value)
            logger.info("Had find the element successful by: %s via value: %s "
                        % (selector_by, selector_value))

        elif selector_by == 'partial_link_text':
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, selector_value)
            logger.info("Had find the element successful by: %s via value: %s "
                        % (selector_by, selector_value))

        elif selector_by == 'tag_name':
            element = self.driver.find_element(By.TAG_NAME, selector_value)
            logger.info("Had find the element successful by: %s via value: %s "
                        % (selector_by, selector_value))

        elif selector_by == 'xpath':
            element = self.driver.find_element(By.XPATH, selector_value)
            logger.info("Had find the element successful by: %s via value: %s "
                        % (selector_by, selector_value))

        elif selector_by == 'css_selector':
            element = self.driver.find_element(By.CSS_SELECTOR, selector_value)
            logger.info("Had find the element successful by: %s via value: %s "
                        % (selector_by, selector_value))

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
                WebDriverWait(self.driver, seconds, 1).until(EC.presence_of_element_located((
                    By.ID, selector_value)), 'by %s，value: %s ,Dom树中未查找到该元素' % (selector_by, selector_value))
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)

        elif selector_by == "name":
            try:
                WebDriverWait(self.driver, seconds, 1).until(EC.presence_of_element_located((
                    By.NAME, selector_value)), '通过%s,Dom树中未查找到该元素' % selector_value)
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)

        elif selector_by == "class_name":
            try:
                WebDriverWait(self.driver, seconds, 1).until(EC.presence_of_element_located((
                    By.CLASS_NAME, selector_value)), '通过%s,Dom树中未查找到该元素' % selector_value)
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)

        elif selector_by == "link_text":
            try:
                WebDriverWait(self.driver, seconds, 1).until(EC.presence_of_element_located((
                    By.LINK_TEXT, selector_value)), '通过%s,Dom树中未查找到该元素' % selector_value)
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)

        elif selector_by == "partial_link_text":
            try:
                WebDriverWait(self.driver, seconds, 1).until(EC.presence_of_element_located((
                    By.PARTIAL_LINK_TEXT, selector_value)), '通过%s,Dom树中未查找到该元素' % selector_value)
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)

        elif selector_by == "tag_name":
            try:
                WebDriverWait(self.driver, seconds, 1).until(EC.presence_of_element_located((
                    By.TAG_NAME, selector_value)), '通过%s,Dom树中未查找到该元素' % selector_value)
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)

        elif selector_by == "xpath":
            try:
                WebDriverWait(self.driver, seconds, 1).until(EC.presence_of_element_located((
                    By.XPATH, selector_value)), '通过%s,Dom树中未查找到该元素' % selector_value)
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)

        elif selector_by == "css_selector":
            try:
                WebDriverWait(self.driver, seconds, 1).until(EC.presence_of_element_located((
                    By.CSS_SELECTOR, selector_value)), '通过%s,Dom树中未查找到该元素' % selector_value)
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
            logger.info("Had type \'%s\' inputBox" % text)
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

    # 点击元素
    def click(self, selector):

        self.wait_element(selector)
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 右击元素
    def right_click(self, selector):
        self.wait_element(selector)
        el = self.find_element(selector)
        try:
            ActionChains(self.driver).context_click(el).perform()
            logger.info("The element was right_click.")
        except NameError as e:
            logger.error("Failed to right_click the element with %s" % e)

    # 移动元素
    def move_to_element(self, selector):
        self.wait_element(selector)
        el = self.find_element(selector)
        try:
            ActionChains(self.driver).move_to_element(el).perform()
            logger.info("The element was move.")
        except NameError as e:
            logger.error("Failed to move_to_element the element with %s" % e)

    def double_click(self, selector):
        """
        Double click element.

        Usage:
        driver.double_click("name=baidu")
        """
        self.wait_element(selector)
        ActionChains(self.driver).double_click(self.find_element(selector)).perform()

    def drag_and_drop(self, source_element, target_element):
        """
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("id=s","id=t")
        """
        self.wait_element(source_element)
        self.wait_element(target_element)
        ActionChains(self.driver).drag_and_drop(self.find_element(source_element), self.find_element(target_element)).perform()
    def back(self):
        """
        Back to old window.

        Usage:
        driver.back()
        """
        self.driver.back()

    def forward(self):
        """
        Forward to old window.

        Usage:
        driver.forward()
        """
        self.driver.forward()

    def get_attribute(self, element, attribute):
        """
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("id=kw","attribute")
        """
        self.wait_element(element)
        return self.find_element(element).get_attribute(attribute)

    def get_text(self, element):
        """
        Get element text information.

        Usage:
        driver.get_text("name=johnny")
        """
        self.wait_element(element)
        return self.find_element(element).text

    def get_display(self, element):
        """
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("id=ppp")
        """
        self.wait_element(element)
        return self.find_element(element).is_displayed()

    def get_title(self):
        """
        Get window title.

        Usage:
        driver.get_title()
        """
        return self.driver.title

    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        """
        return self.driver.current_url

    def get_screenshot(self, file_path):
        """
        Get the current window screenshot.

        Usage:
        driver.get_screenshot("./pic.png")
        """
        self.driver.get_screenshot_as_file(file_path)

    def submit(self, element):
        """
        Submit the specified form.

        Usage:
        driver.submit("id=mainFrame")
        """
        self.wait_element(element)
        self.find_element(element).submit()

    def switch_to_frame(self, element):
        """
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("id=mainFrame")
        """
        self.wait_element(element)
        self.driver._switch_to_frame(self.find_element(element))

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        """
        self.driver.switch_to.default_content()

    def open_new_window(self, element):
        """
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window(id=johnny)
        """
        current_windows = self.driver.current_window_handle
        self.find_element(element).click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_windows:
                self.driver.switch_to.window(handle)

    def F5(self):
        '''
        Refresh the current page.

        Usage:
        driver.F5()
        '''
        self.driver.refresh()

    def js(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def accept_alert(self):
        """
        Accept warning box.

        Usage:
        driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()

    def close(self):
        """
        Close the windows.

        Usage:
        driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        """
        self.driver.quit()
    # 获取网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    # 固定休眠
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)



