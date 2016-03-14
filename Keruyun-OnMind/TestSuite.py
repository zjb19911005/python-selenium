# coding=utf-8
__author__ = 'Junior'
import unittest
import os

# from caselists.loginandlogout import Logandlogout
# from caselists.setcancelreason import test
#
#
# def suite():
#     return unittest.makeSuite(Logandlogout, 'test')
#
#
# def suite2():
#     return unittest.makeSuite(test, 'test')
#
#
# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite())
#     runner.run(suite2())

import os

caselist = os.listdir('/Users/Junior.Zhu/PycharmProjects/python-selenium/Keruyun-OnMind/caselists')
for case in caselist:
    s = case.split('.')[1:][0]  # 选取后缀为py的文件,从.后面开始切片
    if s == 'py':
        # 此处执行dos命令并将结果保存到log.txt
        os.system('/Users/Junior.Zhu/PycharmProjects/python-selenium/Keruyun-OnMind/%s 1>>log.txt 2>&1' % case)
