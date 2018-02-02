from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# driver.find_element_by_id('kw').send_keys("sewww")
# print(driver.find_element_by_id('kw').text)
time.sleep(2)
# driver.find_element_by_id('su').click()
s = driver.find_element_by_xpath('//*[@id="u1"]/a[1]').text
print(s)
time.sleep(3)
driver.quit()