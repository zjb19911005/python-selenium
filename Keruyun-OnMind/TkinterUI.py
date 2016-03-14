#coding=utf-8
import Tkinter as tk
import sys
import os

import  urllib


root =tk.Tk()
# bm= tk.BitmapImage(file='D:\self.bmp')
root.wm_title('WEB自动化测试工具')

lable1= tk.Label(root,fg = 'red',bg = 'blue',text = 'Hello I am Tkinter',width=30,height=20)
lable1.pack()
tk.Label(root,fg = 'red',bg = '#FF00FF',text = 'Hello I am Tkinter').pack()
def helloButton():
    print 'Hello world'

tk.Button(root,text='Hello button',command=helloButton).pack()


#进入消息循环
root.mainloop()