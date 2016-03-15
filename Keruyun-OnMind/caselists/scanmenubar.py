# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class scanmenubar(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://testsso.shishike.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/cas/login?service=http://testb.shishike.com/cas")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("a123456")
        driver.find_element_by_id("loginId").clear()
        driver.find_element_by_id("loginId").send_keys("4881")
        driver.find_element_by_id("captcha").clear()
        driver.find_element_by_id("captcha").send_keys("w")
        driver.find_element_by_name("submit1").click()
        driver.find_element_by_link_text(u"顾客").click()
        driver.find_element_by_link_text(u"营销方案").click()
        driver.find_element_by_link_text(u"优惠券模板").click()
        driver.find_element_by_link_text(u"预订记录").click()
        driver.find_element_by_link_text(u"订单管理").click()
        driver.find_element_by_link_text(u"外卖订单").click()
        driver.find_element_by_link_text(u"基础管理").click()
        driver.find_element_by_link_text(u"仓库设定").click()
        driver.find_element_by_link_text(u"采购管理").click()
        driver.find_element_by_link_text(u"供应商类别设定").click()
        driver.find_element_by_link_text(u"做法管理").click()
        driver.find_element_by_link_text(u"营业报表").click()
        driver.find_element_by_link_text(u"营业概况").click()
        driver.find_element_by_link_text(u"操作日志").click()
        driver.find_element_by_xpath("//div[@id='nav-fixed']/div/span/div/div/div[2]/ul").click()
        driver.find_element_by_id("logout").click()
        driver.find_element_by_link_text(u"确定").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("a123456")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
