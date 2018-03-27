from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# time.sleep(1)
# # driver.set_window_size(480,800)
# second_url = 'http://news.baidu.com'
# driver.get(second_url)
# time.sleep(1)
# driver.refresh()
# #返回首页
# driver.back()
# time.sleep(1)
# #前进一页
# driver.forward()
# # driver.find_element_by_xpath("//input[@id='kw']").send_keys('selenium2')
# # driver.find_element_by_id('su').click()
# time.sleep(1)
# driver.quit()
size = driver.find_element_by_id('kw').size
print(size)
text = driver.find_element_by_id('cp').text
print(text)
attribute = driver.find_element_by_id('kw').get_attribute('type')
print(attribute)
driver.quit()