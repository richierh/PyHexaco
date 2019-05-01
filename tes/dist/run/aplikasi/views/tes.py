'''
Created on Mar 21, 2019

@author: cireng
'''
import wx 


class Frame(wx.Frame):
    
    def __init__(self, parent):
        super(Frame, self).__init__(parent)
        Title = "Judul buat tes"
        self.SetTitle(Title)
        
        sizer1 = wx.BoxSizer(wx.VERTICAL)
        self.panel = wx.Panel(self)
        sizer1.Add(self.panel, 1, wx.ALL | wx.EXPAND)
         
        sizer2 = wx.BoxSizer(wx.HORIZONTAL)
     
        sizerflex1 = wx.FlexGridSizer(1, 0, 0, 0)
        sizerflex1.AddGrowableCol(0, proportion=1)
        sizerflex1.AddGrowableCol(1, proportion=3)
 
        sizerflex1.AddGrowableRow(0, proportion=1)
 
        self.button = wx.Button(self.panel, label="tes")
        sizerflex1.Add(self.button, 1, wx.EXPAND)
        self.button2 = wx.Button(self.panel, label="tes")
        sizerflex1.Add(self.button2, 1, wx.EXPAND)
        
        self.panel.SetSizer(sizerflex1, deleteOld=True)
        self.SetSizer(sizer1, deleteOld=True)
        
        self.Refresh()
        self.Layout()

        
if __name__ == "__main__":
    root = wx.App()
    openwindow = Frame(None)
    openwindow.Show()
    root.MainLoop()
