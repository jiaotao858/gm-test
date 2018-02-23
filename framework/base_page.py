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

    def get(self, url):
        """
        Open url,same as get.

        Usage:
        driver.get("https://www.baidu.com")
        """
        self.driver.get(url)
        logger.info("Open url:%s" % url)

    def max_window(self):
        """
        Set browser window maximized.

        Usage:
        driver.max_window()
        """
        self.driver.maximize_window()
        logger.info("Set browser window maximized.")

    def wait(self, seconds):
        """
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        """
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    def set_window_size(self, wide, high):
        """
        Set browser window wide and high.
        
        Usage:
        driver.set_window_size(100, 250)
        """
        self.driver.set_window_size(wide, high)
        logger.info("Set browser window wind:%d high:%d" %(wide, high))

    def get_windows_img(self):
        """
        Get the current window screenshot.

        Usage:
        driver.get_windows_img()
        """
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
    def find_element(self, element):
        """
           Judge element positioning way, and returns the element.

           Usage:
           driver.find_element("id=kw")
        """
        if '=' not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        by = element.split('=')[0]
        value = element.split('=')[1]

        if by == 'id':
            return self.driver.find_element_by_id(value)
        elif by == 'name':
            return self.driver.find_element(By.NAME, value)
        elif by == 'class_name':
            return self.driver.find_element(By.CLASS_NAME, value)
        elif by == 'link_text':
            return self.driver.find_element(By.LINK_TEXT,value)
        elif by == 'partial_link_text':
            return self.driver.find_element(By.PARTIAL_LINK_TEXT, value)
        elif by == 'tag_name':
            return self.driver.find_element(By.TAG_NAME, value)
        elif by == 'xpath':
            return self.driver.find_element(By.XPATH, value)
        elif by == 'css_selector':
            return self.driver.find_element(By.CSS_SELECTOR, value)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpaht','css'.")

    # 等待元素出现
    def wait_element(self, element, seconds=10):
        """
            Waiting for an element to display.

            Usage:
            driver.wait_element("id=kw",10)
        """
        if '=' not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        by = element.split('=')[0]
        value = element.split('=')[1]

        if by == "id":
            try:
                WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.ID, value)),
                                                           '通过%s 查找属性%s,Dom树中未查找到该元素' % (by, value))
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)
        elif by == "name":
            try:
                WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.NAME, value)),
                                                           '通过%s 查找属性%s,Dom树中未查找到该元素' % (by, value))
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)
        elif by == "class_name":
            try:
                WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((
                    By.CLASS_NAME, value)),'通过%s 查找属性%s,Dom树中未查找到该元素' % (by, value))
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)
        elif by == "link_text":
            try:
                WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((
                    By.LINK_TEXT, value)),'通过%s 查找属性%s,Dom树中未查找到该元素' % (by, value))
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)
        elif by == "partial_link_text":
            try:
                WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((
                    By.PARTIAL_LINK_TEXT, value)),'通过%s 查找属性%s,Dom树中未查找到该元素' % (by, value))
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)
        elif by == "tag_name":
            try:
                WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((
                    By.TAG_NAME, value)),'通过%s 查找属性%s,Dom树中未查找到该元素' % (by, value))
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)
        elif by == "xpath":
            try:
                WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((
                    By.XPATH, value)),'通过%s 查找属性%s,Dom树中未查找到该元素' % (by, value))
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)
        elif by == "css_selector":
            try:
                WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((
                    By.CSS_SELECTOR, value)),'通过%s 查找属性%s,Dom树中未查找到该元素' % (by, value))
            except TimeoutException as e:
                logger.info("TimeoutException: %s" % e)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpaht','css'.")

    def type(self, element, text):
        """
        Clear element and type text.
        
        Usage:
        driver.type("class=right", "Hello World!")
        """
        self.wait_element(element)
        el = self.find_element(element)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \'%s\' inputBox" %text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    def clear(self, element):
        """
         Clear element value.

        Usage:
        driver.clear("class=right")
        """
        self.wait_element(element)
        el = self.find_element(element)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    def click(self,element):
        """
        Click element.

        Usage:
        driver.click("class=right")
        """
        self.wait_element(element)
        el = self.find_element(element)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    def right_click(self, element):
        """
        Right click element.

        Usage:
        driver.right_click("class=right")
        """
        self.wait_element(element)
        ActionChains(self.driver).context_click(self.find_element(element)).perform()
        logger.info("Right click element %s." % element)

    def move_to_element(self, element):
        """
        Mouse over the element.

        Usage:
        driver.move_to_element("css=choose")
        """
        self.wait_element(element)
        ActionChains(self.driver).move_to_element(self.find_element(element)).perform()
        logger.info("Mouse over the element %s." % element)

    def double_click(self, element):
        """
        Double click element.

        Usage:
        driver.double_click("name=baidu")
        """
        self.wait_element(element)
        ActionChains(self.driver).double_click(self.find_element(element)).perform()
        logger.info("Double click element %s." % element)

    def drag_and_drop(self, source_element, target_element):
        """
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("id=s","id=t")
        """
        self.wait_element(source_element)
        self.wait_element(target_element)
        ActionChains(self.driver).drag_and_drop(self.find_element(source_element),
                                                self.find_element(target_element)).perform()
        logger.info("Drags an element from %s to %s." % (source_element, target_element))

    def back(self):
        """
        Back to old window.

        Usage:
        driver.back()
        """
        self.driver.back()
        logger.info("Back to old window.")

    def forward(self):
        """
        Forward to old window.

        Usage:
        driver.forward()
        """
        self.driver.forward()
        logger.info("Forward to old window.")

    def get_attribute(self, element, attribute):
        """
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("id=kw","attribute")
        """
        logger.info("Gets the value of an element:%s attribute." % element)
        self.wait_element(element)
        return self.find_element(element).get_attribute(attribute)

    def get_text(self, element):
        """
        Get element text information.

        Usage:
        driver.get_text("name=johnny")
        """
        logger.info("Get element:%s text information." % element)
        self.wait_element(element)
        return self.find_element(element).text

    def get_display(self, element):
        """
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("id=ppp")
        """
        logger.info("Gets the element:%s to display" % element)
        self.wait_element(element)
        return self.find_element(element).is_displayed()

    def get_title(self):
        """
        Get window title.

        Usage:
        driver.get_title()
        """
        logger.info("Get window title.")
        return self.driver.title

    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        """
        logger.info("Get the URL address of the current page.")
        return self.driver.current_url


    def submit(self, element):
        """
        Submit the specified form.

        Usage:
        driver.submit("id=mainFrame")
        """
        self.wait_element(element)
        self.find_element(element).submit()
        logger.info("Submit the specified form.")

    def switch_to_frame(self, element):
        """
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("id=mainFrame")
        """
        self.wait_element(element)
        self.driver._switch_to_frame(self.find_element(element))
        logger.info("Switch to the specified frame.")

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        """
        self.driver.switch_to.default_content()
        logger.info("Switch to the higher level frame.")

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
        logger.info("Open the new window and switch the handle to the newly opened window.")

    def F5(self):
        '''
        Refresh the current page.

        Usage:
        driver.F5()
        '''
        self.driver.refresh()
        logger.info("Refresh the current page.")

    def js(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)
        logger.info("Execute JavaScript scripts.")

    def accept_alert(self):
        """
        Accept warning box.

        Usage:
        driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()
        logger.info("Accept warning box.")

    def dismiss_alert(self):
        """
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()
        logger.info("Dismisses the alert available.")

    def close(self):
        """
        Close the windows.

        Usage:
        driver.close()
        """
        self.driver.close()
        logger.info("Close the windows.")

    def quit(self):
        """
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        """
        self.driver.quit()
        logger.info(" Quit the driver and close all the windows.")

    # 固定休眠
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)



