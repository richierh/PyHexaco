#! usr/bin/env python

import wx
from coreapps.views.maingui import TentangAplikasi
import pathlib

class TentangAplikasi ( TentangAplikasi ):

    def __init__( self, parent ):
        super().__init__(parent)
        pathimage = pathlib.Path.cwd() / "resources/images/binakarir.png"
        print (pathimage)
        self.image1 = wx.Image(str(pathimage))
#         self.re_image1 = self.image1.Rescale(450,300)
        self.m_bitmap2.SetBitmap(wx.Bitmap(self.image1))

