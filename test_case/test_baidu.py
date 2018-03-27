from selenium import webdriver
import HTMLTestRunner
import unittest
import time

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = 'http://www.baidu.com'

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('unittest')
        driver.find_element_by_id('su').click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title,'unittest_百度搜索')

    def tearDown(self):
        self.driver.quit()

if '__name__' == '__main__':
    # unittest.main()
    testunit = unittest.TestSuite()
    testunit.addTest(MyTest('test_baidu'))
    filename = 'D:\\result.html'
    with open(filename,'wb') as fp:
    #定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title='百度搜索测试报告',
                                               description='用例执行情况'
        )
        runner.run(testunit)

        








