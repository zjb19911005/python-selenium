#coding=utf-8
#Author Junior.zhu
from Tkinter import *
import sys
import os
from tkMessageBox import showinfo
import TestSuite
import  urllib


tool = Tk()

tool.wm_title('WEB自动化测试工具')
tool.resizable(False,False)



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

menubar.add_cascade(label='文件',menu=fmenu)
menubar.add_cascade(label='编辑',menu=emenu)
menubar.add_cascade(label='视图',menu=vmenu)
menubar.add_cascade(label='关于',menu=amenu)

tool['menu']=menubar




# def helloButton(event):
#     global tool
Label(tool,text='***********Python万岁**************').grid(row=0,sticky=W)
t=Label(tool,fg = 'black',bg='yellow',text = '这是一个用来做WEB自动化测试的工具')
# t.bind('<Button-2>',helloButton)#Button-2模拟鼠标右键事件
t.grid(row=1,sticky=W)

Label(tool,fg='white',bg='blue',text="Python大法好,脚本语言牛逼哄哄的").grid(row=2,sticky=W)

# Button(tool,text='Hello button',command=helloButton,background='yellow').grid(row=3,sticky=W)


Label(tool,text='账号:').grid(row=4,sticky=W)
account=Entry(tool).grid(row=4,column=1,sticky=E)

Label(tool,text='密码:').grid(row=5,sticky=W)
password=Entry(tool,show='*').grid(row=5,column=1,sticky=E)
def verify():
    s1=account.get()
    s2=password.get()
    t1=len(s1)
    t2=len(s2)
    if s1=='zhujb' and s2=='123456':
        showinfo(title='WEB自动化账号验证窗口',message='账号验证成功')
        Label(tool,text='验证成功').grid(row=6,column=0,sticky=W)
    else:
        Label(tool,text='用户名或者密码错误').grid(row=6,column=0,sticky=W)

        account.delete(0,t1)
        password.delete(0,t2)







Button(tool,text='权限验证',command=verify).grid(row=6,column=1,sticky=E)

Button(tool,text='开始自动化测试',command=TestSuite).grid(row=7,column=0,sticky=E)




def secondwindows():
    tool.wm_withdraw()
    popup=Toplevel()
    Label(popup,text='测试弹窗').pack()
    Button(popup,text='退回到上个窗口',command=firstwindows).pack()

def firstwindows():
    tool.wm_withdraw()
Button(tool,text='测试弹窗',command=secondwindows).grid(row=7,column=1,sticky=E)



#进入消息循环
tool.mainloop()




