#coding=utf-8
#Author Junior.zhu
from Tkinter import *
import sys
import os
from tkFileDialog import askopenfilename
from tkMessageBox import showinfo
from _tkinter import *
# import TestSuite
import  urllib
import datetime
import time
import  urllib2
from selenium import webdriver
from SimpleDialog import *
from tkMessageBox import *


tool = Tk()
tool.wm_title('测试自动化小工具集合')
tool.resizable(width=False,height=False)
tool.iconbitmap('Clouds.ico')
tool.wm_attributes('-topmost',1)
#开始配置窗口
menubar=Menu(tool)
fmenu=Menu(menubar)
for item in ['新建','打开','保存','另存为','退出']:
     fmenu.add_command(label=item)
fmenu.add_separator()

emenu=Menu(menubar)
for item in ['复制','粘贴','剪切','查找并替换']:
    emenu.add_command(label=item)
emenu.add_separator()

vmenu=Menu(menubar)
for item in ['默认视图','Mac视图']:
    vmenu.add_command(label=item)
vmenu.add_separator()

amenu=Menu(menubar)
for item in ['其他说明']:
  amenu.add_command(label=item)
  amenu.add_separator()
def version():
    showinfo(title='版权信息',message='客如云测试部')
amenu.add_command(label='版权信息',command=version)

menubar.add_cascade(label='文件',menu=fmenu)
menubar.add_cascade(label='编辑',menu=emenu)
menubar.add_cascade(label='视图',menu=vmenu)
menubar.add_cascade(label='关于',menu=amenu)

tool['menu']=menubar

t=Label(tool,text='*******Python万岁,Python大法好*******',bg='yellow',fg='blue').grid(row=0,sticky=E)
time=time.strftime("%Y-%m-%d %H:%M:%S")

Label(tool,fg='white',bg='black',text='现在是北京时间:'+ time).grid(row=3,column=0,sticky=W)

Label(tool,text='账号:').grid(row=4,sticky=W)
account=Entry(tool,textvariable='请输入账户')
account.grid(row=4,column=1,sticky=E)

Label(tool,text='密码:').grid(row=5,sticky=W)
password=Entry(tool,show='*')
password.grid(row=5,column=1,sticky=E)
def verify():
     s1=account.get()
     s2=password.get()
     t1=len(s1)
     t2=len(s2)
     if s1=='123' and s2=='456':
         Label(tool,text='验证成功').grid(row=3,column=1,sticky=W)

     else:
         Label(tool,text='抱歉,用户名或者密码错误').grid(row=3,column=1,sticky=W)
         account.delete(0,t1)
         password.delete(0,t2)




def openfile(message=None):
     openfilename= askopenfilename(filetypes=[('apk','*.apk')])
     try:

         os.system('adb install -r'+path+openfilename)
     except:
         print('Could not open File:%s'%openfilename)

Button(tool,text='权限验证',command=verify).grid(row=6,column=1,sticky=E)
Button(tool,text='弹窗',command=openfile).grid(row=6,column=0,sticky=W)

def adbdevices():
    text=os.system('adb devices')
    showinfo(title='设备列表',message=text)

Button(tool,text='调试设备',command=adbdevices).grid(row=7,column=0,sticky=E)


Button(tool,text='退出程序',command=tool.quit).grid(row=8,column=0,sticky=E)


#进入消息循环
tool.mainloop()
