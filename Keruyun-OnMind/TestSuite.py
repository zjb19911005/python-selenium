#coding=utf-8
__author__ = 'Junior'
import unittest

from 登录与登出检查 import Logandlogout
from 菜品作废理由设置 import test



def suite():
    return unittest.makeSuite(Logandlogout,'test')
def suite2():
    return unittest.makeSuite(test,'test')
if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(suite())
    # runner.run(suite2())


'''import os
caselist=os.listdir('D')
for a in caselist:
    s=a.split('.')[1:][0]#选取后缀为py的文件,从.后面开始切片
    if s=='py':
        os.system()'''