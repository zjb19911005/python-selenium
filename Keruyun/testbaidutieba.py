#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
browser=webdriver.Firefox()
browser.get("http://tieba.baidu.com/")
browser.maximize_window()
print '开始操作登陆贴吧了'
browser.find_element_by_xpath("//li[@class='u_login']").click()
browser.implicitly_wait(3)

browser.find_element_by_xpath("//input[@id='TANGRAM__PSP_8__userName']").send_keys('123456')
#username=browser.find_element_by_id('passport-login-pop').find_element_by_id('TANGRAM__PSP_8__userName')
#browser.execute_script('$("TANGRAM__PSP_8__submit").click();')







'''browser.implicitly_wait(3)
browser.find_element_by_xpath("//input[@id='TANGRAM__PSP_8__userName']").send_keys(Keys.TAB)
browser.find_element_by_xpath("//input[@id='TANGRAM__PSP_8__password']").send_keys('zhu2311829')
browser.implicitly_wait(3)
browser.find_element_by_xpath("//input[@id='TANGRAM__PSP_8__memberPass']").click()
browser.implicitly_wait(2)
browser.find_element_by_xpath("//input[@id='TANGRAM__PSP_8__submit']").submit()
browser.implicitly_wait(2)'''

#browser.quit()
#browser.close()