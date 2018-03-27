from selenium import webdriver


driver = webdriver.Firefox()
driver.get('http://www.youdao.com')
#获取cookie
# cookie = driver.get_cookies()
driver.add_cookie({'name':'keyaaaaa','value':'valueaaa'})
for cookie in driver.get_cookies():
    print(cookie)
driver.quit()