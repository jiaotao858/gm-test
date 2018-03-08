from selenium import webdriver

driver = webdriver.Chrome()  # 打开chrome，如果没有安装chrome,换成webdriver.Firefox()
driver.maximize_window()  # 最大化浏览器窗口
driver.implicitly_wait(8)  # 设置隐式时间等待

driver.get("https://www.baidu.com")  # 地址栏输入百度地址
driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")  # 搜索输入框输入Selenium
driver.find_element_by_xpath("//*[@id='su']").click()  # 点击百度一下按钮
