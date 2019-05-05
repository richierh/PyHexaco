#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.0 on Thu Mar 21 19:53:17 2019
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!



import wx

from coreapps.views.hexacofile import Hexacofile

class MyApp(wx.App):

    def OnInit(self):
        self.frame = Hexacofile(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp


if __name__ == "__main__":

    import gettext
    import os
    import pathlib

    pathwd = pathlib.Path.cwd() / ".."
    os.chdir(pathwd)  
    gettext.install("app")  # replace with the appropriate catalog name
    app = MyApp(0)
    app.MainLoop()
