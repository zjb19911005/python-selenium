# coding=utf-8
__author__ = 'Junior'
import unittest
import HTMLTestRunner
from caselists.changepassword import changepassword
import time


if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(changepassword('test_'))
    times = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

filename ='D:\\result'+times+'.html'
fp=file(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(
stream=fp,
title=u'自动化测试报告',
description=u'自动化测试结果'
)
runner.run(testunit)




# import os
# import HTMLTestRunner
# # caselist = os.listdir('/Users/Junior.Zhu/PycharmProjects/python-selenium/Keruyun-OnMind/caselists')#MAC下的文件路劲
# caselist=os.system('C:\Users\Administrator\PycharmProjects\python-selenium\Keruyun-OnMind\caselists')#WINDOS路径
# for a in caselist:
#     s = a.split('.')[1:][0]  # 选取后缀为py的文件,从.后面开始切片
#     if s == 'py':
#         #WIN路径
#         os.popen('python C:\Users\Administrator\PycharmProjects\python-selenium\Keruyun-OnMind\caselists%s1 >>/Users/Junior.Zhu/PycharmProjectslog.txt 2>&1' %a)

