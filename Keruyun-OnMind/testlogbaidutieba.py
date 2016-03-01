#coding=utf-8
__author__ = 'Junior'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
browser=webdriver.Firefox()
browser.maximize_window()
browser.get("http://tieba.baidu.com/")
browser.implicitly_wait(5)
browser.find_element_by_class_name("u_login").click()
browser.implicitly_wait(5)
allhandles=browser.window_handles
print allhandles
for handle in allhandles:
    if handle!=nowhandle:
        browser.switch_to_window(handle)
        browser.find_element_by_xpath("input[@id='TANGRAM__PSP_8__userName']").send_keys('zjb19911005')
        browser.implicitly_wait(5)
        browser.find_element_by_xpath("input[@id='TANGRAM__PSP_8__password']").send_keys('zhu2311829')
        browser.implicitly_wait(5)
        browser.find_element_by_xpath("input[@id='TANGRAM__PSP_8__submit']").submit()
        browser.implicitly_wait(5)
browser.switch_to_window(nowhandle)
