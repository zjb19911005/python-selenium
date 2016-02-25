#coding=utf-8
__author__ = 'Junior'
import unittest

from selenium import webdriver


class secondpagetestcase(unittest.TestCase):
    def setUp(self):
        print "开始 登陆主界面的测试 ..........Start .................."
        self.browser=webdriver.Firefox()
        self.url='http://www.baidu.com'
        print '现在将浏览器最大化'
        self.browser.maximize_window()#浏览器最大化用例
    def test001forsearch(self):
        self.browser.get(self.url+'/')
        try:
            self.browser.find_element_by_xpath("//input[@id='kddd']").send_keys('u逗比')
        except:
            self.browser.get_screenshot_as_file('D:\selenium\keruyun\错误图片\baidusearch.png')


    def tearDown(self):
        print '第二界面 测试完成............END.........................'
        self.browser.close()
if __name__=='__main__':
    unittest.main()