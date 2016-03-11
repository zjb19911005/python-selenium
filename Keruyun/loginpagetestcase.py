# coding=utf-8
__author__ = 'Junior'
import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class loginpagetest(unittest.TestCase):
    def setUp(self):
        print "开始 登陆主界面的测试 ..........Start .................."
        self.browser = webdriver.Firefox()
        self.url = 'https://testsso.shishike.com/cas/login?service=http://testb.shishike.com/cas'
        print '现在将浏览器最大化'
        self.browser.set_window_size(800, 800)  # 浏览器最大化用例

    def test001turelogin(self):  # 正确账户登录
        self.browser.get(self.url + '/')
        self.browser.find_element_by_xpath("//input[@id='loginId']").clear()
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_xpath("//input[@id='loginId']").send_keys('4481')
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_xpath("//input[@id='username']").clear()
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_xpath("//input[@id='username']").send_keys('admin')
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_xpath("//input[@id='password']").clear()
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_xpath("//input[@id='password']").send_keys('a123456')
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_xpath("//input[@id='captcha']").send_keys('aa')
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_xpath("//input[@class='btn-1']").submit()

    def tearDown(self):
        print'完成登陆主界面的测试...........END............'
        self.browser.quit()
        self.browser.close()


if __name__ == '__main__':
    unittest.main()
