from selenium import webdriver
from framework.base_page import BasePage
import time


driver = BasePage("driver")
driver.wait(10)
driver.get("http://testhotel.hblckj.cn/login.html")
driver.send_keys("xpath=/html/body/div[2]/div[2]/form/div[1]/input","18640857881")
driver.send_keys("xpath=/html/body/div[2]/div[2]/form/div[2]/input","jt123456")
driver.click("xpath=/html/body/div[2]/div[2]/form/div[4]/div/a")
driver.wait(5)

driver.set_window_size(600,600)
# driver.sleep(3)
driver.max_window()
driver.get_window_img()
driver.clear("xpath=/html/body/div[3]/div/div[1]/div[2]/form/div[1]/input")

driver.right_click("xpath=/html/body/div[3]/div/div[1]/div[2]/form/div[1]/input")

driver.move_to_element("xpath=/html/body/div[1]/div/ul/li[1]/a")

driver.back()

driver.forward()

driver.get_attribute("xpath=/html/body/div[3]/div/div[1]/div[2]/form/div[5]/button","type")

driver.get_text("xpath=/html/body/div[3]/div/div[1]/div[2]/form/div[5]/button")

driver.get_display("xpath=/html/body/div[3]/div/div[1]/div[2]/form/div[5]/button")
driver.sleep(2)
driver.get_title()
driver.sleep(2)
driver.get_url()
driver.sleep(2)
driver.open_new_tag("http://www.baidu.com")
driver.send_keys("id=kw","hhhh")
driver.sleep(2)
driver.F5()
driver.sleep(2)
driver.js("window.open('http://www.163.com')")
driver.sleep(2)
# driver.open_new_window("xpath=/html/body/div[2]/div/ul/li[2]/a")
driver.switch_tag(0)
driver.sleep(2)
driver.switch_tag(1)
driver.sleep(2)
driver.switch_tag(2)
driver.sleep(3)
driver.switch_tag(1)
driver.sleep(2)
driver.send_keys("id=kw","hhhh")
# driver.quit()