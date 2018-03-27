from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
#获取当前页面的句柄
search_windows = driver.current_window_handle

driver.find_element_by_name('tj_trmap').click()


driver.find_element_by_name('tj_trnews').click()
#获取所有打开窗口的句柄
all_handles = driver.window_handles

for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
        print('now map window')
        driver.find_element_by_class_name('searchbox-content-common').send_keys('上海市')
        driver.find_element_by_id('search-button').click()
        time.sleep(2)
for handle in all_handles:
    if handle == search_windows:
        driver.switch_to.window(handle)
        print('now search window')
        # driver.find_element_by_id('TANGRAM__PSP_2__closeBtn').click()
        driver.find_element_by_id('kw').send_keys('selenium')
        driver.find_element_by_id('su').click()
        time.sleep(2)

driver.quit()