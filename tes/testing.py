'''
Created on Mar 21, 2019

@author: cireng
'''
import wx
import wx.lib.inspection
import wx.lib.mixins.inspection


class MyFrame(wx.Frame):
    pass

 
class MyApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):

    def OnInit(self):
        self.Init()  # initialize the inspection tool
        frame = MyFrame(None, title="This is a test")
        frame.Show()
        self.SetTopWindow(frame)
        return True


app = MyApp()
app.MainLoop()
wx.lib.inspection.InspectionTool().Show()
