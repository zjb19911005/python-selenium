#coding=utf-8
import Tkinter as tk
import sys
import os

import  urllib
from TestSuite import suite
from loginandlogout import Logandlogout
root =tk.Tk()
# bm= tk.BitmapImage(file='D:\self.bmp')
tk.Label(root,fg = 'red',bg = 'blue',text = 'Hello I am Tkinter',width=10,height=10).pack()
tk.Label(root,fg = 'red',bg = '#FF00FF',text = 'Hello I am Tkinter').pack()
def helloButton():
    print 'Hello world'

tk.Button(root,text='Hello button',command=helloButton).pack()
tk.Button(root,text='第一条自动化测试-登录与登出',command=Logandlogout).pack()

#进入消息循环
root.mainloop()