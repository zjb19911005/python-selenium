#coding=utf-8
__author__ = 'Junior'

#最简单setup打包程序

from distutils.core import setup
import py2exe

#  options = {"py2exe":
#             {   "compressed": 1,
#                 "optimize": 2,
#                 "bundle_files": 1   # <span style="color: rgb(255, 128, 0); line-height: 15px; white-space: pre; background-color: rgb(253, 253, 253); ">所有文件打包成一个exe文件</span>
#             }
#           }
setup(
    version = "0.0.1",
    description = "First Demo",
    name = "测试小工具",
    # options = options,
    zipfile = None, # 不生成zip库文件
    console=['TkinterUI.py']
    # console = [{"script": "Tkinter.py", "icon_resources": [(1, "Hello.ico")] }],
    )