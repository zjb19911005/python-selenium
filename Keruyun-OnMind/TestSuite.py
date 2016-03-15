# coding=utf-8
__author__ = 'Junior'
import unittest

# from caselists import *
#
# def suite():
#     return unittest.makeSuite(caselist, 'test')
#
#
# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite())

import os

caselist = os.listdir('/Users/Junior.Zhu/PycharmProjects/python-selenium/Keruyun-OnMind/caselists')

for a in caselist:
    s = a.split('.')[1:][0]  # 选取后缀为py的文件,从.后面开始切片
    if s == 'py':
        os.popen('python /Users/Junior.Zhu/PycharmProjects/python-selenium/Keruyun-OnMind/caselists%s1 >>/Users/Junior.Zhu/PycharmProjectslog.txt 2>&1' %a)

