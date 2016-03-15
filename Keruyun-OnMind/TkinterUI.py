#coding=utf-8
#Author Junior.zhu
from Tkinter import *
import sys
import os
from tkMessageBox import showinfo
from _tkinter import *
import TestSuite
import  urllib
import datetime
import time
import  urllib2
from selenium import webdriver




tool = Tk()

tool.wm_title('测试自动化小工具集合')
tool.resizable(width=False,height=False)
tool.iconbitmap('Clouds.ico')
tool.wm_attributes('-topmost',1)

# tool.update()#刷新窗口,必须要做的事情
# currentwidth=tool.winfo_reqwidth()#获取当前程序的宽
# currentheight=tool.winfo_reqheight()#获取当前程序的高
# scnWidth,scnHeight=tool.maxsize()#获取屏幕的最大尺寸
# #开始计算位置
# center='%dx%d+%d+%d' %(currentheight,currentwidth,(scnHeight-currentheight)/2,(scnWidth-currentwidth)/2)
# tool.geometry(center)


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
for item in ['版权信息','其他说明']:
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
     if s1=='kry888' and s2=='a123456':
         Label(tool,text='验证成功').grid(row=6,column=0,sticky=W)
         text=os.popen('adb devices')
         # Text(tool,width=50,height=30).pack()
     else:
         Label(tool,text='抱歉,用户名或者密码错误').grid(row=6,column=0,sticky=W)
         account.delete(0,t1)
         password.delete(0,t2)



def TOPlevel():
    secondscreen=Toplevel(tool,title='我是第二窗口',widt=30,height=30).pack()
    Label(secondscreen,text="我是来搞笑的").pack()


Button(tool,text='权限验证',command=verify).grid(row=6,column=1,sticky=E)
Button(tool,text='弹窗',command=Toplevel).grid(row=6,column=0,sticky=W)

Button(tool,text='开始自动化测试',command=TestSuite).grid(row=7,column=0,sticky=E)



Button(tool,text='退出程序',command=tool.quit).grid(row=8,column=0,sticky=E)


#进入消息循环
tool.mainloop()
