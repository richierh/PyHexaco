# -*- coding: utf-8 -*-

###########################################################################
# # Python code generated with wxFormBuilder (version Mar 22 2019)
# # http://www.wxformbuilder.org/
# #
# # PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
# # Class FrameDepan
###########################################################################


class FrameDepan (wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(500, 900), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		bSizer1 = wx.BoxSizer(wx.VERTICAL)

		self.m_simplebook1 = wx.Simplebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.m_panel1 = wx.Panel(self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.m_panel1.SetBackgroundColour(wx.Colour(196, 61, 50))

		bSizer5 = wx.BoxSizer(wx.VERTICAL)

		self.m_scrolledWindow1 = wx.ScrolledWindow(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL | wx.VSCROLL)
		self.m_scrolledWindow1.SetScrollRate(5, 5)
		self.m_scrolledWindow1.SetBackgroundColour(wx.Colour(219, 77, 77))

		bSizer2 = wx.BoxSizer(wx.VERTICAL)

		self.m_staticText11 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"HEXACO", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText11.Wrap(-1)

		bSizer2.Add(self.m_staticText11, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_bitmap1 = wx.StaticBitmap(self.m_scrolledWindow1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer2.Add(self.m_bitmap1, 1, wx.ALL | wx.EXPAND, 5)

		self.m_staticText1 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"No Tes", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText1.Wrap(-1)

		bSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_textCtrl1 = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, -1), 0 | wx.TAB_TRAVERSAL)
		bSizer2.Add(self.m_textCtrl1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_staticText2 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText2.Wrap(-1)

		bSizer2.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_datePicker1 = wx.adv.DatePickerCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size(-1, -1), wx.adv.DP_DEFAULT)
		bSizer2.Add(self.m_datePicker1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

		self.m_textCtrl2 = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 | wx.TAB_TRAVERSAL)
		self.m_textCtrl2.Hide()

		bSizer2.Add(self.m_textCtrl2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_staticText3 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Nama Kandidat", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText3.Wrap(-1)

		bSizer2.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_textCtrl3 = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1), 0 | wx.TAB_TRAVERSAL)
		bSizer2.Add(self.m_textCtrl3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_staticText4 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText4.Wrap(-1)

		bSizer2.Add(self.m_staticText4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_textCtrl4 = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 | wx.TAB_TRAVERSAL)
		self.m_textCtrl4.Hide()

		bSizer2.Add(self.m_textCtrl4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		m_choice1Choices = [ u"Laki - Laki", u"Perempuan" ]
		self.m_choice1 = wx.Choice(self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
		self.m_choice1.SetSelection(0)
		bSizer2.Add(self.m_choice1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_staticText5 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText5.Wrap(-1)

		bSizer2.Add(self.m_staticText5, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_datePicker2 = wx.adv.DatePickerCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT)
		bSizer2.Add(self.m_datePicker2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_textCtrl5 = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 | wx.TAB_TRAVERSAL)
		self.m_textCtrl5.Hide()

		bSizer2.Add(self.m_textCtrl5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_staticText6 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Pendidikan Terakhir", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText6.Wrap(-1)

		bSizer2.Add(self.m_staticText6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		m_choice2Choices = [ u"SD", u"SMP", u"SMA", u"Diploma", u"S1", u"S2", u"S3" ]
		self.m_choice2 = wx.Choice(self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0)
		self.m_choice2.SetSelection(0)
		bSizer2.Add(self.m_choice2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_staticText7 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Jurusan Pendidikan", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText7.Wrap(-1)

		bSizer2.Add(self.m_staticText7, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_textCtrl7 = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, -1), 0)
		bSizer2.Add(self.m_textCtrl7, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_staticText8 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText8.Wrap(-1)

		bSizer2.Add(self.m_staticText8, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_textCtrl8 = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
		bSizer2.Add(self.m_textCtrl8, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_textCtrl6 = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_textCtrl6.Hide()

		bSizer2.Add(self.m_textCtrl6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_staticText9 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Perusahaan/Instansi", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText9.Wrap(-1)

		bSizer2.Add(self.m_staticText9, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_textCtrl9 = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(250, -1), 0)
		bSizer2.Add(self.m_textCtrl9, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_staticText10 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Posisi / Jabatan", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText10.Wrap(-1)

		bSizer2.Add(self.m_staticText10, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_textCtrl10 = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(250, -1), 0)
		bSizer2.Add(self.m_textCtrl10, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_scrolledWindow1.SetSizer(bSizer2)
		self.m_scrolledWindow1.Layout()
		bSizer2.Fit(self.m_scrolledWindow1)
		bSizer5.Add(self.m_scrolledWindow1, 1, wx.EXPAND | wx.ALL, 5)

		self.m_panel1.SetSizer(bSizer5)
		self.m_panel1.Layout()
		bSizer5.Fit(self.m_panel1)
		self.m_simplebook1.AddPage(self.m_panel1, u"a page", True)
		self.m_panel2 = wx.Panel(self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.m_panel2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

		bSizer7 = wx.BoxSizer(wx.VERTICAL)

		self.m_panel6 = wx.Panel(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		fgSizer1 = wx.FlexGridSizer(3, 3, 0, 0)
		fgSizer1.AddGrowableCol(0)
		fgSizer1.AddGrowableCol(1)
		fgSizer1.AddGrowableCol(2)
		fgSizer1.SetFlexibleDirection(wx.BOTH)
		fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_staticText12 = wx.StaticText(self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText12.Wrap(-1)

		self.m_staticText12.Hide()

		fgSizer1.Add(self.m_staticText12, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_staticText13 = wx.StaticText(self.m_panel6, wx.ID_ANY, u"Tipe Soal", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText13.Wrap(-1)

		fgSizer1.Add(self.m_staticText13, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_staticText14 = wx.StaticText(self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText14.Wrap(-1)

		self.m_staticText14.Hide()

		fgSizer1.Add(self.m_staticText14, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_radioBtn1 = wx.RadioButton(self.m_panel6, wx.ID_ANY, u"Soal 24", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer1.Add(self.m_radioBtn1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_radioBtn2 = wx.RadioButton(self.m_panel6, wx.ID_ANY, u"Soal 60", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer1.Add(self.m_radioBtn2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_radioBtn3 = wx.RadioButton(self.m_panel6, wx.ID_ANY, u"Soal 100", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer1.Add(self.m_radioBtn3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_panel6.SetSizer(fgSizer1)
		self.m_panel6.Layout()
		fgSizer1.Fit(self.m_panel6)
		bSizer7.Add(self.m_panel6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_panel2.SetSizer(bSizer7)
		self.m_panel2.Layout()
		bSizer7.Fit(self.m_panel2)
		self.m_simplebook1.AddPage(self.m_panel2, u"a page", False)
		self.m_panel3 = wx.Panel(self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.m_panel3.SetBackgroundColour(wx.Colour(147, 21, 205))

		bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_panel7 = wx.Panel(self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

		fgSizer9 = wx.FlexGridSizer(0, 2, 0, 0)
		fgSizer9.SetFlexibleDirection(wx.BOTH)
		fgSizer9.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_staticText15 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText15.Wrap(-1)

		fgSizer9.Add(self.m_staticText15, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.m_textCtrl11 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer9.Add(self.m_textCtrl11, 0, wx.ALL, 5)

		self.m_staticText16 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText16.Wrap(-1)

		fgSizer9.Add(self.m_staticText16, 0, wx.ALL, 5)

		self.m_textCtrl12 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer9.Add(self.m_textCtrl12, 0, wx.ALL, 5)

		self.m_staticText17 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText17.Wrap(-1)

		fgSizer9.Add(self.m_staticText17, 0, wx.ALL, 5)

		self.m_textCtrl13 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer9.Add(self.m_textCtrl13, 0, wx.ALL, 5)

		self.m_staticText18 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText18.Wrap(-1)

		fgSizer9.Add(self.m_staticText18, 0, wx.ALL, 5)

		self.m_textCtrl14 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer9.Add(self.m_textCtrl14, 0, wx.ALL, 5)

		self.m_staticText19 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText19.Wrap(-1)

		fgSizer9.Add(self.m_staticText19, 0, wx.ALL, 5)

		self.m_textCtrl15 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer9.Add(self.m_textCtrl15, 0, wx.ALL, 5)

		self.m_staticText20 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText20.Wrap(-1)

		fgSizer9.Add(self.m_staticText20, 0, wx.ALL, 5)

		self.m_textCtrl16 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer9.Add(self.m_textCtrl16, 0, wx.ALL, 5)

		self.m_staticText21 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText21.Wrap(-1)

		fgSizer9.Add(self.m_staticText21, 0, wx.ALL, 5)

		self.m_textCtrl17 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer9.Add(self.m_textCtrl17, 0, wx.ALL, 5)

		self.m_staticText22 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText22.Wrap(-1)

		fgSizer9.Add(self.m_staticText22, 0, wx.ALL, 5)

		self.m_textCtrl18 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer9.Add(self.m_textCtrl18, 0, wx.ALL, 5)

		self.m_staticText23 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText23.Wrap(-1)

		fgSizer9.Add(self.m_staticText23, 0, wx.ALL, 5)

		self.m_textCtrl20 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer9.Add(self.m_textCtrl20, 0, wx.ALL, 5)

		self.m_staticText24 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText24.Wrap(-1)

		fgSizer9.Add(self.m_staticText24, 0, wx.ALL, 5)

		self.m_textCtrl21 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer9.Add(self.m_textCtrl21, 0, wx.ALL, 5)

		self.m_staticText25 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText25.Wrap(-1)

		fgSizer9.Add(self.m_staticText25, 0, wx.ALL, 5)

		self.m_textCtrl22 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer9.Add(self.m_textCtrl22, 0, wx.ALL, 5)

		self.m_staticText38 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText38.Wrap(-1)

		fgSizer9.Add(self.m_staticText38, 0, wx.ALL, 5)

		self.m_textCtrl19 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer9.Add(self.m_textCtrl19, 0, wx.ALL, 5)

		bSizer11.Add(fgSizer9, 1, wx.EXPAND, 5)

		fgSizer10 = wx.FlexGridSizer(0, 2, 0, 0)
		fgSizer10.SetFlexibleDirection(wx.BOTH)
		fgSizer10.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_staticText26 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText26.Wrap(-1)

		fgSizer10.Add(self.m_staticText26, 0, wx.ALL, 5)

		self.m_textCtrl23 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer10.Add(self.m_textCtrl23, 0, wx.ALL, 5)

		self.m_staticText27 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText27.Wrap(-1)

		fgSizer10.Add(self.m_staticText27, 0, wx.ALL, 5)

		self.m_textCtrl24 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer10.Add(self.m_textCtrl24, 0, wx.ALL, 5)

		self.m_staticText28 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText28.Wrap(-1)

		fgSizer10.Add(self.m_staticText28, 0, wx.ALL, 5)

		self.m_textCtrl25 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer10.Add(self.m_textCtrl25, 0, wx.ALL, 5)

		self.m_staticText29 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText29.Wrap(-1)

		fgSizer10.Add(self.m_staticText29, 0, wx.ALL, 5)

		self.m_textCtrl26 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer10.Add(self.m_textCtrl26, 0, wx.ALL, 5)

		self.m_staticText30 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText30.Wrap(-1)

		fgSizer10.Add(self.m_staticText30, 0, wx.ALL, 5)

		self.m_textCtrl27 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer10.Add(self.m_textCtrl27, 0, wx.ALL, 5)

		self.m_staticText31 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText31.Wrap(-1)

		fgSizer10.Add(self.m_staticText31, 0, wx.ALL, 5)

		self.m_textCtrl28 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer10.Add(self.m_textCtrl28, 0, wx.ALL, 5)

		self.m_staticText32 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText32.Wrap(-1)

		fgSizer10.Add(self.m_staticText32, 0, wx.ALL, 5)

		self.m_textCtrl29 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer10.Add(self.m_textCtrl29, 0, wx.ALL, 5)

		self.m_staticText33 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText33.Wrap(-1)

		fgSizer10.Add(self.m_staticText33, 0, wx.ALL, 5)

		self.m_textCtrl30 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer10.Add(self.m_textCtrl30, 0, wx.ALL, 5)

		self.m_staticText34 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText34.Wrap(-1)

		fgSizer10.Add(self.m_staticText34, 0, wx.ALL, 5)

		self.m_textCtrl31 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer10.Add(self.m_textCtrl31, 0, wx.ALL, 5)

		self.m_staticText35 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText35.Wrap(-1)

		fgSizer10.Add(self.m_staticText35, 0, wx.ALL, 5)

		self.m_textCtrl32 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer10.Add(self.m_textCtrl32, 0, wx.ALL, 5)

		self.m_staticText36 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText36.Wrap(-1)

		fgSizer10.Add(self.m_staticText36, 0, wx.ALL, 5)

		self.m_textCtrl33 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer10.Add(self.m_textCtrl33, 0, wx.ALL, 5)

		self.m_staticText37 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText37.Wrap(-1)

		fgSizer10.Add(self.m_staticText37, 0, wx.ALL, 5)

		self.m_textCtrl34 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer10.Add(self.m_textCtrl34, 0, wx.ALL, 5)

		bSizer11.Add(fgSizer10, 1, wx.EXPAND, 5)

		self.m_panel7.SetSizer(bSizer11)
		self.m_panel7.Layout()
		bSizer11.Fit(self.m_panel7)
		bSizer6.Add(self.m_panel7, 1, wx.EXPAND | wx.ALL, 5)

		self.m_panel8 = wx.Panel(self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.m_panel8.Hide()

		bSizer6.Add(self.m_panel8, 1, wx.EXPAND | wx.ALL, 5)

		self.m_panel9 = wx.Panel(self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.m_panel9.Hide()

		bSizer6.Add(self.m_panel9, 1, wx.EXPAND | wx.ALL, 5)

		self.m_panel3.SetSizer(bSizer6)
		self.m_panel3.Layout()
		bSizer6.Fit(self.m_panel3)
		self.m_simplebook1.AddPage(self.m_panel3, u"a page", False)
		self.m_panel4 = wx.Panel(self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.m_panel4.SetBackgroundColour(wx.Colour(116, 198, 160))

		self.m_simplebook1.AddPage(self.m_panel4, u"a page", True)

		bSizer1.Add(self.m_simplebook1, 1, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		bSizer9 = wx.BoxSizer(wx.VERTICAL)

		bSizer1.Add(bSizer9, 1, wx.EXPAND, 5)

		self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		fgSizer5 = wx.FlexGridSizer(0, 3, 0, 0)
		fgSizer5.AddGrowableCol(1)
		fgSizer5.SetFlexibleDirection(wx.BOTH)
		fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_button1 = wx.Button(self.m_panel5, wx.ID_ANY, u"Ke Awal", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer5.Add(self.m_button1, 0, wx.ALL, 5)

		self.m_button2 = wx.Button(self.m_panel5, wx.ID_ANY, u"Sebelumnya", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer5.Add(self.m_button2, 0, wx.ALIGN_BOTTOM | wx.TOP | wx.BOTTOM | wx.RIGHT | wx.ALIGN_RIGHT, 5)

		self.m_button3 = wx.Button(self.m_panel5, wx.ID_ANY, u"Selanjutnyta", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer5.Add(self.m_button3, 1, wx.ALL | wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT, 5)

		self.m_panel5.SetSizer(fgSizer5)
		self.m_panel5.Layout()
		fgSizer5.Fit(self.m_panel5)
		bSizer1.Add(self.m_panel5, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.SetSizer(bSizer1)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.m_textCtrl3.Bind(wx.EVT_TEXT, self.m_textCtrl3OnText)
		self.m_radioBtn1.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn1OnRadioButtonSoal24)
		self.m_radioBtn2.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn2OnRadioButtonSoal60)
		self.m_radioBtn3.Bind(wx.EVT_RADIOBUTTON, self.m_radioBtn3OnRadioButtonSoal100)
		self.m_button1.Bind(wx.EVT_BUTTON, self.m_button1OnButtonClick)
		self.m_button2.Bind(wx.EVT_BUTTON, self.m_button2OnButtonClick)
		self.m_button3.Bind(wx.EVT_BUTTON, self.m_button3OnButtonClick)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def m_textCtrl3OnText(self, event):
		event.Skip()

	def m_radioBtn1OnRadioButtonSoal24(self, event):
		event.Skip()

	def m_radioBtn2OnRadioButtonSoal60(self, event):
		event.Skip()

	def m_radioBtn3OnRadioButtonSoal100(self, event):
		event.Skip()

	def m_button1OnButtonClick(self, event):
		event.Skip()

	def m_button2OnButtonClick(self, event):
		event.Skip()

	def m_button3OnButtonClick(self, event):
		event.Skip()

