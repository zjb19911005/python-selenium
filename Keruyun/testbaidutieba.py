#coding=utf-8
from selenium import webdriver

browser=webdriver.Firefox()
browser.get("http://tieba.baidu.com/")
try:
    browser.maximize_windows()
except:
    print 'Can not max'
browser.implicitly_wait(3)
browser.find_element_by_class_name('u_login').click()
#browser.find_elements_by_link_text("登录").click()
browser.implicitly_wait(3)
browser.find_element_by_xpath("//div[@id='TANGRAM__PSP_8__userName']").clear()
browser.find_element_by_xpath("//div[@id='TANGRAM__PSP_8__userName']").send_keys('zjb19911005')
browser.close()