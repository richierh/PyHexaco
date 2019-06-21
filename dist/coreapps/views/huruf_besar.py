'''
Created on May 13, 2019

@author: cireng
'''
import wx
import string

class HurufBesar():
    def __init__(self,parent):
        
        self.parent = parent
        self.parent.m_textCtrl1.Bind( wx.EVT_CHAR, self.m_textCtrl1OnText )
        self.parent.m_textCtrl3.Bind( wx.EVT_CHAR, self.m_textCtrl3OnText )
        self.parent.m_textCtrl7.Bind( wx.EVT_CHAR, self.m_textCtrl7OnText )
        self.parent.m_textCtrl8.Bind( wx.EVT_CHAR, self.m_textCtrl8OnText )
        self.parent.m_textCtrl9.Bind( wx.EVT_CHAR, self.m_textCtrl9OnText )
        self.parent.m_textCtrl10.Bind( wx.EVT_CHAR, self.m_textCtrl10OnText )


    def on_char(self, event):
        key=event.GetKeyCode()
        text_ctrl=event.GetEventObject()
        if chr(key) in string.ascii_lowercase:
            text_ctrl.AppendText(chr(key).upper())
            return
 
        event.Skip()
    
    def m_textCtrl3OnText(self, event):
        key=event.GetKeyCode()
        text_ctrl=event.GetEventObject()
        if chr(key) in string.ascii_lowercase:
            text_ctrl.AppendText(chr(key).upper())
            return
 
        event.Skip()        

    def m_textCtrl1OnText(self, event):

        key = event.GetKeyCode()
        text_ctrl = event.GetEventObject()
        if chr(key) in string.ascii_lowercase:
            text_ctrl.AppendText(chr(key).upper())
            return
 
        event.Skip()


    def m_textCtrl7OnText(self,event):
        key=event.GetKeyCode()
        text_ctrl=event.GetEventObject()
        if chr(key) in string.ascii_lowercase:
            text_ctrl.AppendText(chr(key).upper())
            return

        event.Skip()

    def m_textCtrl8OnText(self, event):
        key=event.GetKeyCode()
        text_ctrl=event.GetEventObject()
        if chr(key) in string.ascii_lowercase:
            text_ctrl.AppendText(chr(key).upper())
            return
        event.Skip()


    def m_textCtrl9OnText(self, event):
        key=event.GetKeyCode()
        text_ctrl=event.GetEventObject()
        if chr(key) in string.ascii_lowercase:
            text_ctrl.AppendText(chr(key).upper())
            return
        event.Skip()
   
    def m_textCtrl10OnText(self, event):
        key=event.GetKeyCode()
        text_ctrl=event.GetEventObject()
        if chr(key) in string.ascii_lowercase:
            text_ctrl.AppendText(chr(key).upper())
            return      
        event.Skip()
   