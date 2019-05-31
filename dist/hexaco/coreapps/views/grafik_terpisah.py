#! usr/bin/env pyt((hon
'''
Created on May 18, 2019

@author: cireng
'''
import wx
from coreapps.views.maingui import FrameGrafikTerpisah

class GrafikFrame(FrameGrafikTerpisah):
    
    
    def __init__(self,parent):
        super(GrafikFrame,self).__init__(parent)
        self.parent = parent
        
        


if __name__== "__main__":
    root = wx.App()
    run = GrafikFrame(None).Show()
    root.MainLoop()