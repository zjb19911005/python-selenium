#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
browser=webdriver.Firefox()
browser.get("http://tieba.baidu.com/")
browser.implicitly_wait(4)
print "设置浏览器大小啦"
try:
#    browser.maximize_window()
    browser.set_window_size(800,600)
except:
    print '抱歉,设置失败了'
browser.implicitly_wait(3)
nowhandle=browser.current_window_handle
print '开始操作登陆贴吧了'
browser.find_element_by_xpath("//li[@class='u_login']").click()

allhandles=browser.window_handles
for handle in allhandles:
    if handle!=nowhandle:
        browser.switch_to.window(handle)
        browser.find_element_by_xpath("//input[@id='TANGRAM__PSP_8__userName']").send_keys('123456')
        browser.implicitly_wait(3)
        browser.find_element_by_xpath("//input[@id='TANGRAM__PSP_8__password']").send_keys('zhu2311829')
        browser.implicitly_wait(3)
        browser.find_element_by_xpath("//input[@id='TANGRAM__PSP_8__memberPass']").click()
        browser.implicitly_wait(2)
        browser.find_element_by_xpath("//input[@id='TANGRAM__PSP_8__submit']").submit()
        browser.implicitly_wait(2)

#browser.quit()
#browser.close()