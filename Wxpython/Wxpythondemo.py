#coding=utf-8
__author__ = 'Junior'
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"My Frame Demo",size=(300,300))
        panel =wx.Panel(self,-1)
        panel.Blind(wx.EVT_MOTION,self.OnMove)
        wx.StaticText(panel,-1,'POS:',pos=(10,12))
        self.posCtrl =wx.TexCtlr(panel,-1,'',pos=(40,10))

    def OnMove(self,event):
        pos=event.GetPosition()
        self.posCtrl.setValue("%s,%s" %(pos.x,pos.y))

if __name__=='__main__':
    app = wx.PySimpleApp()
    frame =MyFrame()
    frame.Show(True)
    app.MainLoop()