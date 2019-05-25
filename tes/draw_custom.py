#! usr/bin/env python
'''
Created on May 4, 2019

@author: cireng
'''

import wx


class DrawRadar(wx.Frame):
    
    def __init__(self, parent):
        super(DrawRadar, self).__init__(parent)
        self.parent = parent
        print ("worki") 
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Layout()
        
    def on_paint(self, event):        
        self.paint = wx.PaintDC(self)
        brush = wx.Brush("red")  
        self.paint.SetBackground(wx.Image("python.jpg"))  
        self.paint.Clear() 

        self.pen = wx.Pen(wx.Colour(255, 255, 0))
        self.paint.SetPen(self.pen)
        
        self.paint.DrawLine(200, 50, 350, 50)


if __name__ == "__main__":
    root = wx.App()
    run = DrawRadar(None)
    run.Show()
    root.MainLoop()
