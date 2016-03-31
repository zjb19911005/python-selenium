# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Changecommercial(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://testsso.shishike.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_changecommercial(self):
        driver = self.driver
        driver.get(self.base_url + "/cas/login?service=http://testb.shishike.com/cas")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("a123456")
        driver.find_element_by_id("loginId").clear()
        driver.find_element_by_id("loginId").send_keys("4881")
        driver.find_element_by_id("captcha").clear()
        driver.find_element_by_id("captcha").send_keys("ww")
        driver.find_element_by_name("submit1").click()
        driver.implicitly_wait(30)
        driver.find_element_by_css_selector("div.user-info").click()
        driver.find_element_by_id("changeCommercial").click()
        driver.find_element_by_link_text(u"切换").click()
        driver.find_element_by_css_selector("div.user-info").click()
        driver.find_element_by_id("changeCommercial").click()
        driver.find_element_by_link_text(u"切换").click()
        driver.find_element_by_css_selector("div.user-info").click()
        driver.find_element_by_id("changeCommercial").click()
        driver.find_element_by_link_text(u"切换").click()
        driver.find_element_by_css_selector("div.user-info").click()
        driver.find_element_by_id("logout").click()
        driver.find_element_by_link_text(u"确定").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("a123456")
    
    # def is_element_present(self, how, what):
    #     try: self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e: return False
    #     return True
    
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