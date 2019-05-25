#! usr/bin/env python

import wx


class TentangAplikasi (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=u"Binakarir", pos=wx.DefaultPosition, size=wx.Size(550, 325), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer41 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel21 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer42 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap2 = wx.StaticBitmap(self.m_panel21, wx.ID_ANY, wx.Bitmap(u"resources/images/binakarir.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer42.Add(self.m_bitmap2, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl45 = wx.TextCtrl(self.m_panel21, wx.ID_ANY, u"\nBandung - INDONESIA.\nEmail: careindonesiasolusi@gmail.com\nTelp. 022 8724 1354", wx.DefaultPosition, wx.Size(500, 200), wx.TE_CENTER | wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_WORDWRAP)
        self.m_textCtrl45.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT"))
        self.m_textCtrl45.Enable(False)

        bSizer42.Add(self.m_textCtrl45, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.m_panel21.SetSizer(bSizer42)
        self.m_panel21.Layout()
        bSizer42.Fit(self.m_panel21)
        bSizer41.Add(self.m_panel21, 1, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer41)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
