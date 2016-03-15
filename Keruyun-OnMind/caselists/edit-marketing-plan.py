# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Editmarketingplan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://testsso.shishike.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_editmarketingplan(self):
        driver = self.driver
        driver.get(self.base_url + "/cas/login?service=http://testb.shishike.com/cas")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("a1234567")
        driver.find_element_by_id("loginId").clear()
        driver.find_element_by_id("loginId").send_keys("4881")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("a123456")
        driver.find_element_by_id("captcha").clear()
        driver.find_element_by_id("captcha").send_keys("a")
        driver.find_element_by_name("submit1").click()
        driver.find_element_by_link_text(u"营销方案").click()
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("plan-name").click()
        driver.find_element_by_id("plan-name").clear()
        driver.find_element_by_id("plan-name").send_keys(u"哇卡卡卡耶")
        driver.find_element_by_id("textarea1").clear()
        driver.find_element_by_id("textarea1").send_keys(u"哇哇咔咔")
        driver.find_element_by_xpath("//div[@id='sizcache08288470879480282']/div[3]/table/tbody/tr[3]/td[2]").click()
        driver.find_element_by_xpath("//div[@id='sizcache08288470879480282']/div[3]/table/tbody/tr[5]/td[4]").click()
        driver.find_element_by_css_selector("div.select-control > em").click()
        driver.find_element_by_xpath("//div[@id='accordion']/div/div[2]/div/div/div/div/div/ul/li[2]").click()
        driver.find_element_by_id("cid-1152").click()
        driver.find_element_by_link_text(u"完 成").click()
        driver.find_element_by_id("validate-date").click()
        driver.find_element_by_id("text-validity-dates").clear()
        driver.find_element_by_id("text-validity-dates").send_keys("88")
        driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
        driver.find_element_by_id("voucherNumber").click()
        driver.find_element_by_id("radio-coupons-number-2").click()
        driver.find_element_by_xpath("//div[@id='coupons-set-number']/div[2]/div[2]/label").click()
        driver.find_element_by_id("text-coupons-number").clear()
        driver.find_element_by_id("text-coupons-number").send_keys("888")
        driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
        driver.find_element_by_id("useTimePeriod").click()
        driver.find_element_by_css_selector("div.col-sm-2.w120 > div.select-group > div.select-control > em").click()
        driver.find_element_by_css_selector("div.select-control.select-control-arrowtop > em").click()
        driver.find_element_by_id("saveTime").click()
        driver.find_element_by_xpath("//div[@id='setingTime']/div[2]/form/dl[2]/dd/div/div/div/em").click()
        driver.find_element_by_xpath("//div[@id='setingTime']/div[2]/form/dl[2]/dd/div/div/ul/li[2]").click()
        driver.find_element_by_id("saveTime").click()
        driver.find_element_by_css_selector("div.col-sm-2.w120 > div.select-group > ul > li").click()
        driver.find_element_by_xpath("//div[@id='setingTime']/div[2]/form/dl/dd/div[3]/div/ul/li").click()
        driver.find_element_by_xpath("//div[@id='setingTime']/div[2]/form/dl[2]/dd/div/div/ul/li").click()
        driver.find_element_by_id("eachSendNum").clear()
        driver.find_element_by_id("eachSendNum").send_keys("1")
        driver.find_element_by_id("saveMarketPlan").click()
        driver.find_element_by_id("backToList").click()
        driver.find_element_by_link_text(u"确 定").click()
        driver.find_element_by_xpath("//div[@id='nav-fixed']/div/span/div/div/div[2]/ul").click()
        driver.find_element_by_id("logout").click()
        driver.find_element_by_link_text(u"确 定").click()
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
