from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Firefox()

#打开baidu页面
driver.get('http://www.baidu.com')
#-1webdriverwait显示等待

#每0.5秒轮询一次，直到找到ID为kw的元素，超出5s，直接报错
# element = WebDriverWait(driver,5,0.5).until(
#     EC.presence_of_element_located((By.ID,'kw'))
#     )
# element.send_keys('selenium')
# time.sleep(4)
# driver.quit()

#用is_displayed判断
# print(time.ctime())
# for i in range(1,10):
#     try:
#         el = driver.find_element_by_id("kw22")
#         if el.is_displayed():
#             break
#     except:
#         pass
#     time.sleep(1)
# else:
#     print('time out')
# print(time.ctime())
# driver.quit()

#-2隐式等待
driver.implicitly_wait(10)
try:
    print(time.ctime())
    driver.find_element_by_id('kw').send_keys('selenium')
    driver.find_element_by_id('su').click()
    #截取当前窗口并存放到指定位置
    driver.get_screenshot_as_file('D:\\baidu.jpg')
except:
    print()
finally:
    print(time.ctime())
    driver.quit()
