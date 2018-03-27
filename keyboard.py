from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

#输入框输入内容
driver.find_element_by_id("kw").send_keys('seleniumm')

#删除输入的m
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)

#输入空格键加教程
driver.find_element_by_id('kw').send_keys(Keys.SPACE)
driver.find_element_by_id('kw').send_keys('教程')

#CTRL+A全选输入框的内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')

driver.find_element_by_id('kw').send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()
