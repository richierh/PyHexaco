# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Apr 14 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class FrameDepan
###########################################################################

class FrameDepan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 804,900 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )


		bSizer1.Add( bSizer9, 1, wx.EXPAND, 5 )

		self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer141 = wx.BoxSizer( wx.VERTICAL )

		self.m_simplebook1 = wx.Simplebook( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TAB_TRAVERSAL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		self.m_scrolledWindow1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"HEXACO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer2.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bitmap1 = wx.StaticBitmap( self.m_scrolledWindow1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_bitmap1, 1, wx.ALL|wx.EXPAND, 5 )

		fgSizer11 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"No Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		fgSizer11.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0|wx.TAB_TRAVERSAL )
		fgSizer11.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( fgSizer11, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer12 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		fgSizer12.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_datePicker1 = wx.adv.DatePickerCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( -1,-1 ), wx.adv.DP_DEFAULT )
		fgSizer12.Add( self.m_datePicker1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		self.m_textCtrl2.Hide()

		fgSizer12.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( fgSizer12, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer13 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Nama Kandidat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer13.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0|wx.TAB_TRAVERSAL )
		fgSizer13.Add( self.m_textCtrl3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( fgSizer13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer14 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText4 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		fgSizer14.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		self.m_textCtrl4.Hide()

		fgSizer14.Add( self.m_textCtrl4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_choice1Choices = [ u"Laki - Laki", u"Perempuan" ]
		self.m_choice1 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		fgSizer14.Add( self.m_choice1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( fgSizer14, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText5 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer2.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_datePicker2 = wx.adv.DatePickerCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		bSizer2.Add( self.m_datePicker2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		self.m_textCtrl5.Hide()

		bSizer2.Add( self.m_textCtrl5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText6 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Pendidikan Terakhir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer2.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_choice2Choices = [ u"SD", u"SMP", u"SMA", u"Diploma", u"S1", u"S2", u"S3" ]
		self.m_choice2 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		bSizer2.Add( self.m_choice2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText7 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Jurusan Pendidikan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer2.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0|wx.TAB_TRAVERSAL )
		bSizer2.Add( self.m_textCtrl7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText8 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer2.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0|wx.TAB_TRAVERSAL )
		bSizer2.Add( self.m_textCtrl8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl6.Hide()

		bSizer2.Add( self.m_textCtrl6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Perusahaan/Instansi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer2.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0|wx.TAB_TRAVERSAL )
		bSizer2.Add( self.m_textCtrl9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText10 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Posisi / Jabatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer2.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0|wx.TAB_TRAVERSAL )
		bSizer2.Add( self.m_textCtrl10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer2 )
		self.m_scrolledWindow1.Layout()
		bSizer2.Fit( self.m_scrolledWindow1 )
		bSizer5.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer5 )
		self.m_panel1.Layout()
		bSizer5.Fit( self.m_panel1 )
		self.m_simplebook1.AddPage( self.m_panel1, u"a page", True )
		self.m_panel2 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel6 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer142 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText13 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Tipe Soal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 26, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer142.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer142.Add( ( 0, 50), 0, 0, 5 )

		fgSizer1 = wx.FlexGridSizer( 6, 0, 0, 0 )
		fgSizer1.AddGrowableCol( 0 )
		fgSizer1.AddGrowableRow( 3 )
		fgSizer1.AddGrowableRow( 4 )
		fgSizer1.AddGrowableRow( 5 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_radioBtn1 = wx.RadioButton( self.m_panel6, wx.ID_ANY, u"Soal 24", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn1.Hide()

		fgSizer1.Add( self.m_radioBtn1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_radioBtn2 = wx.RadioButton( self.m_panel6, wx.ID_ANY, u"Soal 60", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn2.Hide()

		fgSizer1.Add( self.m_radioBtn2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_radioBtn3 = wx.RadioButton( self.m_panel6, wx.ID_ANY, u"Soal 100", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn3.Hide()

		fgSizer1.Add( self.m_radioBtn3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button4 = wx.Button( self.m_panel6, wx.ID_ANY, u"24 Item", wx.DefaultPosition, wx.Size( 300,100 ), 0 )
		self.m_button4.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer1.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.m_button5 = wx.Button( self.m_panel6, wx.ID_ANY, u"60 Item", wx.DefaultPosition, wx.Size( 300,100 ), 0 )
		self.m_button5.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer1.Add( self.m_button5, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button6 = wx.Button( self.m_panel6, wx.ID_ANY, u"100 Item", wx.DefaultPosition, wx.Size( 300,100 ), 0 )
		self.m_button6.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer1.Add( self.m_button6, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer142.Add( fgSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel6.SetSizer( bSizer142 )
		self.m_panel6.Layout()
		bSizer142.Fit( self.m_panel6 )
		bSizer7.Add( self.m_panel6, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel2.SetSizer( bSizer7 )
		self.m_panel2.Layout()
		bSizer7.Fit( self.m_panel2 )
		self.m_simplebook1.AddPage( self.m_panel2, u"a page", False )
		self.m_panel24 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel24.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText47 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Tipe Soal 24", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		bSizer10.Add( self.m_staticText47, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText15 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		fgSizer9.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		fgSizer9.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		fgSizer9.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl13, 0, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		fgSizer9.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl14, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		fgSizer9.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl15, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		fgSizer9.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.m_textCtrl16 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl16, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		fgSizer9.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.m_textCtrl17 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl17, 0, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		fgSizer9.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl18, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		fgSizer9.Add( self.m_staticText23, 0, wx.ALL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl20, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		fgSizer9.Add( self.m_staticText24, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl21, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		fgSizer9.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl22, 0, wx.ALL, 5 )

		self.m_staticText38 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		fgSizer9.Add( self.m_staticText38, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl19, 0, wx.ALL, 5 )


		bSizer11.Add( fgSizer9, 0, wx.EXPAND, 5 )

		fgSizer10 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText26 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		fgSizer10.Add( self.m_staticText26, 0, wx.ALL, 5 )

		self.m_textCtrl23 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl23, 0, wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		fgSizer10.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl24, 0, wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		fgSizer10.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_textCtrl25 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl25, 0, wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		fgSizer10.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_textCtrl26 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl26, 0, wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		fgSizer10.Add( self.m_staticText30, 0, wx.ALL, 5 )

		self.m_textCtrl27 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl27, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		fgSizer10.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_textCtrl28 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl28, 0, wx.ALL, 5 )

		self.m_staticText32 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"19", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		fgSizer10.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.m_textCtrl29 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl29, 0, wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		fgSizer10.Add( self.m_staticText33, 0, wx.ALL, 5 )

		self.m_textCtrl30 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl30, 0, wx.ALL, 5 )

		self.m_staticText34 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"21", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		fgSizer10.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.m_textCtrl31 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl31, 0, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"22", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		fgSizer10.Add( self.m_staticText35, 0, wx.ALL, 5 )

		self.m_textCtrl32 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl32, 0, wx.ALL, 5 )

		self.m_staticText36 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"23", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		fgSizer10.Add( self.m_staticText36, 0, wx.ALL, 5 )

		self.m_textCtrl33 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl33, 0, wx.ALL, 5 )

		self.m_staticText37 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"24", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		fgSizer10.Add( self.m_staticText37, 0, wx.ALL, 5 )

		self.m_textCtrl34 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl34, 0, wx.ALL, 5 )


		bSizer11.Add( fgSizer10, 0, wx.EXPAND, 5 )


		bSizer10.Add( bSizer11, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel7.SetSizer( bSizer10 )
		self.m_panel7.Layout()
		bSizer10.Fit( self.m_panel7 )
		bSizer6.Add( self.m_panel7, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel8 = wx.Panel( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel8.Hide()

		bSizer6.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel9 = wx.Panel( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel9.Hide()

		bSizer6.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel24.SetSizer( bSizer6 )
		self.m_panel24.Layout()
		bSizer6.Fit( self.m_panel24 )
		self.m_simplebook1.AddPage( self.m_panel24, u"a page", False )
		self.m_panel60 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText48 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"Tipe 60", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		self.m_staticText48.SetFont( wx.Font( 48, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer13.Add( self.m_staticText48, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer51 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer51.SetFlexibleDirection( wx.BOTH )
		fgSizer51.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText49 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		fgSizer51.Add( self.m_staticText49, 0, wx.ALL, 5 )

		self.m_textCtrl42 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl42, 0, wx.ALL, 5 )

		self.m_staticText50 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		fgSizer51.Add( self.m_staticText50, 0, wx.ALL, 5 )

		self.m_textCtrl43 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl43, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		fgSizer51.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.m_textCtrl44 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl44, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		fgSizer51.Add( self.m_staticText52, 0, wx.ALL, 5 )

		self.m_textCtrl45 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl45, 0, wx.ALL, 5 )

		self.m_staticText53 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		fgSizer51.Add( self.m_staticText53, 0, wx.ALL, 5 )

		self.m_textCtrl46 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl46, 0, wx.ALL, 5 )

		self.m_staticText54 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )

		fgSizer51.Add( self.m_staticText54, 0, wx.ALL, 5 )

		self.m_textCtrl47 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl47, 0, wx.ALL, 5 )

		self.m_staticText55 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		fgSizer51.Add( self.m_staticText55, 0, wx.ALL, 5 )

		self.m_textCtrl48 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl48, 0, wx.ALL, 5 )

		self.m_staticText56 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )

		fgSizer51.Add( self.m_staticText56, 0, wx.ALL, 5 )

		self.m_textCtrl49 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl49, 0, wx.ALL, 5 )

		self.m_staticText57 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )

		fgSizer51.Add( self.m_staticText57, 0, wx.ALL, 5 )

		self.m_textCtrl50 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl50, 0, wx.ALL, 5 )

		self.m_staticText58 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )

		fgSizer51.Add( self.m_staticText58, 0, wx.ALL, 5 )

		self.m_textCtrl51 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl51, 0, wx.ALL, 5 )


		bSizer14.Add( fgSizer51, 0, 0, 5 )

		fgSizer6 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText59 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )

		fgSizer6.Add( self.m_staticText59, 0, wx.ALL, 5 )

		self.m_textCtrl52 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl52, 0, wx.ALL, 5 )

		self.m_staticText60 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )

		fgSizer6.Add( self.m_staticText60, 0, wx.ALL, 5 )

		self.m_textCtrl53 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl53, 0, wx.ALL, 5 )

		self.m_staticText61 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		fgSizer6.Add( self.m_staticText61, 0, wx.ALL, 5 )

		self.m_textCtrl54 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl54, 0, wx.ALL, 5 )

		self.m_staticText62 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )

		fgSizer6.Add( self.m_staticText62, 0, wx.ALL, 5 )

		self.m_textCtrl55 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl55, 0, wx.ALL, 5 )

		self.m_staticText63 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )

		fgSizer6.Add( self.m_staticText63, 0, wx.ALL, 5 )

		self.m_textCtrl56 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl56, 0, wx.ALL, 5 )

		self.m_staticText64 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )

		fgSizer6.Add( self.m_staticText64, 0, wx.ALL, 5 )

		self.m_textCtrl57 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl57, 0, wx.ALL, 5 )

		self.m_staticText65 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )

		fgSizer6.Add( self.m_staticText65, 0, wx.ALL, 5 )

		self.m_textCtrl58 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl58, 0, wx.ALL, 5 )

		self.m_staticText66 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66.Wrap( -1 )

		fgSizer6.Add( self.m_staticText66, 0, wx.ALL, 5 )

		self.m_textCtrl59 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl59, 0, wx.ALL, 5 )

		self.m_staticText67 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"19", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText67.Wrap( -1 )

		fgSizer6.Add( self.m_staticText67, 0, wx.ALL, 5 )

		self.m_textCtrl60 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl60, 0, wx.ALL, 5 )

		self.m_staticText68 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )

		fgSizer6.Add( self.m_staticText68, 0, wx.ALL, 5 )

		self.m_textCtrl61 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl61, 0, wx.ALL, 5 )


		bSizer14.Add( fgSizer6, 0, 0, 5 )

		fgSizer7 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText69 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"21", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )

		fgSizer7.Add( self.m_staticText69, 0, wx.ALL, 5 )

		self.m_textCtrl62 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl62, 0, wx.ALL, 5 )

		self.m_staticText70 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"22", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText70.Wrap( -1 )

		fgSizer7.Add( self.m_staticText70, 0, wx.ALL, 5 )

		self.m_textCtrl63 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl63, 0, wx.ALL, 5 )

		self.m_staticText71 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"23", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		fgSizer7.Add( self.m_staticText71, 0, wx.ALL, 5 )

		self.m_textCtrl64 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl64, 0, wx.ALL, 5 )

		self.m_staticText72 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"24", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText72.Wrap( -1 )

		fgSizer7.Add( self.m_staticText72, 0, wx.ALL, 5 )

		self.m_textCtrl65 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl65, 0, wx.ALL, 5 )

		self.m_staticText73 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"25", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText73.Wrap( -1 )

		fgSizer7.Add( self.m_staticText73, 0, wx.ALL, 5 )

		self.m_textCtrl66 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl66, 0, wx.ALL, 5 )

		self.m_staticText74 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"26", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText74.Wrap( -1 )

		fgSizer7.Add( self.m_staticText74, 0, wx.ALL, 5 )

		self.m_textCtrl67 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl67, 0, wx.ALL, 5 )

		self.m_staticText75 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"27", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText75.Wrap( -1 )

		fgSizer7.Add( self.m_staticText75, 0, wx.ALL, 5 )

		self.m_textCtrl68 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl68, 0, wx.ALL, 5 )

		self.m_staticText76 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"28", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText76.Wrap( -1 )

		fgSizer7.Add( self.m_staticText76, 0, wx.ALL, 5 )

		self.m_textCtrl69 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl69, 0, wx.ALL, 5 )

		self.m_staticText77 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"29", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )

		fgSizer7.Add( self.m_staticText77, 0, wx.ALL, 5 )

		self.m_textCtrl70 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl70, 0, wx.ALL, 5 )

		self.m_staticText78 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"30", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( -1 )

		fgSizer7.Add( self.m_staticText78, 0, wx.ALL, 5 )

		self.m_textCtrl71 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl71, 0, wx.ALL, 5 )


		bSizer14.Add( fgSizer7, 0, 0, 5 )

		fgSizer8 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText79 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"31", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )

		fgSizer8.Add( self.m_staticText79, 0, wx.ALL, 5 )

		self.m_textCtrl72 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl72, 0, wx.ALL, 5 )

		self.m_staticText80 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"32", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )

		fgSizer8.Add( self.m_staticText80, 0, wx.ALL, 5 )

		self.m_textCtrl73 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl73, 0, wx.ALL, 5 )

		self.m_staticText81 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"33", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		fgSizer8.Add( self.m_staticText81, 0, wx.ALL, 5 )

		self.m_textCtrl74 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl74, 0, wx.ALL, 5 )

		self.m_staticText82 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"34", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )

		fgSizer8.Add( self.m_staticText82, 0, wx.ALL, 5 )

		self.m_textCtrl75 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl75, 0, wx.ALL, 5 )

		self.m_staticText83 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"35", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )

		fgSizer8.Add( self.m_staticText83, 0, wx.ALL, 5 )

		self.m_textCtrl76 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl76, 0, wx.ALL, 5 )

		self.m_staticText84 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"36", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )

		fgSizer8.Add( self.m_staticText84, 0, wx.ALL, 5 )

		self.m_textCtrl77 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl77, 0, wx.ALL, 5 )

		self.m_staticText85 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"37", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )

		fgSizer8.Add( self.m_staticText85, 0, wx.ALL, 5 )

		self.m_textCtrl78 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl78, 0, wx.ALL, 5 )

		self.m_staticText86 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"38", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )

		fgSizer8.Add( self.m_staticText86, 0, wx.ALL, 5 )

		self.m_textCtrl79 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl79, 0, wx.ALL, 5 )

		self.m_staticText87 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"39", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText87.Wrap( -1 )

		fgSizer8.Add( self.m_staticText87, 0, wx.ALL, 5 )

		self.m_textCtrl80 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl80, 0, wx.ALL, 5 )

		self.m_staticText88 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"40", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )

		fgSizer8.Add( self.m_staticText88, 0, wx.ALL, 5 )

		self.m_textCtrl81 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl81, 0, wx.ALL, 5 )


		bSizer14.Add( fgSizer8, 0, 0, 5 )

		fgSizer91 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer91.SetFlexibleDirection( wx.BOTH )
		fgSizer91.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText89 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"41", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText89.Wrap( -1 )

		fgSizer91.Add( self.m_staticText89, 0, wx.ALL, 5 )

		self.m_textCtrl82 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl82, 0, wx.ALL, 5 )

		self.m_staticText90 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"42", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText90.Wrap( -1 )

		fgSizer91.Add( self.m_staticText90, 0, wx.ALL, 5 )

		self.m_textCtrl83 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl83, 0, wx.ALL, 5 )

		self.m_staticText91 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"43", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		fgSizer91.Add( self.m_staticText91, 0, wx.ALL, 5 )

		self.m_textCtrl84 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl84, 0, wx.ALL, 5 )

		self.m_staticText92 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"44", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText92.Wrap( -1 )

		fgSizer91.Add( self.m_staticText92, 0, wx.ALL, 5 )

		self.m_textCtrl85 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl85, 0, wx.ALL, 5 )

		self.m_staticText93 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"45", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText93.Wrap( -1 )

		fgSizer91.Add( self.m_staticText93, 0, wx.ALL, 5 )

		self.m_textCtrl86 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl86, 0, wx.ALL, 5 )

		self.m_staticText94 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"46", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText94.Wrap( -1 )

		fgSizer91.Add( self.m_staticText94, 0, wx.ALL, 5 )

		self.m_textCtrl87 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl87, 0, wx.ALL, 5 )

		self.m_staticText95 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"47", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText95.Wrap( -1 )

		fgSizer91.Add( self.m_staticText95, 0, wx.ALL, 5 )

		self.m_textCtrl88 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl88, 0, wx.ALL, 5 )

		self.m_staticText96 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"48", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText96.Wrap( -1 )

		fgSizer91.Add( self.m_staticText96, 0, wx.ALL, 5 )

		self.m_textCtrl89 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl89, 0, wx.ALL, 5 )

		self.m_staticText97 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"49", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText97.Wrap( -1 )

		fgSizer91.Add( self.m_staticText97, 0, wx.ALL, 5 )

		self.m_textCtrl90 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl90, 0, wx.ALL, 5 )

		self.m_staticText98 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"50", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText98.Wrap( -1 )

		fgSizer91.Add( self.m_staticText98, 0, wx.ALL, 5 )

		self.m_textCtrl91 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl91, 0, wx.ALL, 5 )


		bSizer14.Add( fgSizer91, 0, 0, 5 )

		fgSizer101 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer101.SetFlexibleDirection( wx.BOTH )
		fgSizer101.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText99 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"51", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText99.Wrap( -1 )

		fgSizer101.Add( self.m_staticText99, 0, wx.ALL, 5 )

		self.m_textCtrl92 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl92, 0, wx.ALL, 5 )

		self.m_staticText100 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"52", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText100.Wrap( -1 )

		fgSizer101.Add( self.m_staticText100, 0, wx.ALL, 5 )

		self.m_textCtrl93 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl93, 0, wx.ALL, 5 )

		self.m_staticText101 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"53", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		fgSizer101.Add( self.m_staticText101, 0, wx.ALL, 5 )

		self.m_textCtrl94 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl94, 0, wx.ALL, 5 )

		self.m_staticText102 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"54", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText102.Wrap( -1 )

		fgSizer101.Add( self.m_staticText102, 0, wx.ALL, 5 )

		self.m_textCtrl95 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl95, 0, wx.ALL, 5 )

		self.m_staticText103 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"55", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText103.Wrap( -1 )

		fgSizer101.Add( self.m_staticText103, 0, wx.ALL, 5 )

		self.m_textCtrl96 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl96, 0, wx.ALL, 5 )

		self.m_staticText104 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"56", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText104.Wrap( -1 )

		fgSizer101.Add( self.m_staticText104, 0, wx.ALL, 5 )

		self.m_textCtrl97 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl97, 0, wx.ALL, 5 )

		self.m_staticText105 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"57", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText105.Wrap( -1 )

		fgSizer101.Add( self.m_staticText105, 0, wx.ALL, 5 )

		self.m_textCtrl98 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl98, 0, wx.ALL, 5 )

		self.m_staticText106 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"58", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText106.Wrap( -1 )

		fgSizer101.Add( self.m_staticText106, 0, wx.ALL, 5 )

		self.m_textCtrl99 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl99, 0, wx.ALL, 5 )

		self.m_staticText107 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"59", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText107.Wrap( -1 )

		fgSizer101.Add( self.m_staticText107, 0, wx.ALL, 5 )

		self.m_textCtrl100 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl100, 0, wx.ALL, 5 )

		self.m_staticText108 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"60", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText108.Wrap( -1 )

		fgSizer101.Add( self.m_staticText108, 0, wx.ALL, 5 )

		self.m_textCtrl101 = wx.TextCtrl( self.m_panel60, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl101, 0, wx.ALL, 5 )


		bSizer14.Add( fgSizer101, 0, 0, 5 )


		bSizer13.Add( bSizer14, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel60.SetSizer( bSizer13 )
		self.m_panel60.Layout()
		bSizer13.Fit( self.m_panel60 )
		self.m_simplebook1.AddPage( self.m_panel60, u"a page", False )
		self.m_panel4 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer91 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap2 = wx.StaticBitmap( self.m_panel10, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer91.Add( self.m_bitmap2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText39 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Letak Grafik di tulisan Binakarir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		bSizer91.Add( self.m_staticText39, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel10.SetSizer( bSizer91 )
		self.m_panel10.Layout()
		bSizer91.Fit( self.m_panel10 )
		bSizer8.Add( self.m_panel10, 0, wx.EXPAND |wx.ALL, 5 )

		gSizer1 = wx.GridSizer( 2, 0, 0, 0 )

		self.m_staticText40 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Altruism", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		gSizer1.Add( self.m_staticText40, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl35 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl35, 0, wx.ALL, 5 )


		bSizer8.Add( gSizer1, 0, 0, 5 )

		gSizer2 = wx.GridSizer( 3, 6, 0, 0 )

		self.m_staticText41 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"O", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		gSizer2.Add( self.m_staticText41, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText42 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		gSizer2.Add( self.m_staticText42, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText43 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		gSizer2.Add( self.m_staticText43, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText44 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Ex", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		gSizer2.Add( self.m_staticText44, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText45 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Em", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		gSizer2.Add( self.m_staticText45, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText46 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"H", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		gSizer2.Add( self.m_staticText46, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl36 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		gSizer2.Add( self.m_textCtrl36, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_textCtrl37 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		gSizer2.Add( self.m_textCtrl37, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl38 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		gSizer2.Add( self.m_textCtrl38, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl39 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		gSizer2.Add( self.m_textCtrl39, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl40 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		gSizer2.Add( self.m_textCtrl40, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl41 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		gSizer2.Add( self.m_textCtrl41, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button7 = wx.Button( self.m_panel4, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button8 = wx.Button( self.m_panel4, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button8, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self.m_panel4, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_button10 = wx.Button( self.m_panel4, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button10, 0, wx.ALL, 5 )

		self.m_button11 = wx.Button( self.m_panel4, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button11, 0, wx.ALL, 5 )

		self.m_button12 = wx.Button( self.m_panel4, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button12, 0, wx.ALL, 5 )


		bSizer8.Add( gSizer2, 0, 0, 5 )


		self.m_panel4.SetSizer( bSizer8 )
		self.m_panel4.Layout()
		bSizer8.Fit( self.m_panel4 )
		self.m_simplebook1.AddPage( self.m_panel4, u"a page", True )

		bSizer141.Add( self.m_simplebook1, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel12.SetSizer( bSizer141 )
		self.m_panel12.Layout()
		bSizer141.Fit( self.m_panel12 )
		bSizer1.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer5.AddGrowableCol( 1 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button1 = wx.Button( self.m_panel5, wx.ID_ANY, u"Ke Awal", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self.m_panel5, wx.ID_ANY, u"Sebelumnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.Enable( False )

		fgSizer5.Add( self.m_button2, 0, wx.ALIGN_BOTTOM|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_RIGHT, 5 )

		self.m_button3 = wx.Button( self.m_panel5, wx.ID_ANY, u"Selanjutnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button3, 1, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		self.m_panel5.SetSizer( fgSizer5 )
		self.m_panel5.Layout()
		fgSizer5.Fit( self.m_panel5 )
		bSizer1.Add( self.m_panel5, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl3.Bind( wx.EVT_TEXT, self.m_textCtrl3OnText )
		self.m_radioBtn1.Bind( wx.EVT_RADIOBUTTON, self.m_radioBtn1OnRadioButtonSoal24 )
		self.m_radioBtn2.Bind( wx.EVT_RADIOBUTTON, self.m_radioBtn2OnRadioButtonSoal60 )
		self.m_radioBtn3.Bind( wx.EVT_RADIOBUTTON, self.m_radioBtn3OnRadioButtonSoal100 )
		self.m_button4.Bind( wx.EVT_BUTTON, self.m_button4OnButtonClick24 )
		self.m_button5.Bind( wx.EVT_BUTTON, self.m_button5OnButtonClick60 )
		self.m_button6.Bind( wx.EVT_BUTTON, self.m_button6OnButtonClick100 )
		self.m_button7.Bind( wx.EVT_BUTTON, self.m_button7OnButtonClick )
		self.m_button8.Bind( wx.EVT_BUTTON, self.m_button8OnButtonClick )
		self.m_button9.Bind( wx.EVT_BUTTON, self.m_button9OnButtonClick )
		self.m_button10.Bind( wx.EVT_BUTTON, self.m_button10OnButtonClick )
		self.m_button11.Bind( wx.EVT_BUTTON, self.m_button11OnButtonClick )
		self.m_button12.Bind( wx.EVT_BUTTON, self.m_button12OnButtonClick )
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
		self.m_button2.Bind( wx.EVT_BUTTON, self.m_button2OnButtonClick )
		self.m_button3.Bind( wx.EVT_BUTTON, self.m_button3OnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_textCtrl3OnText( self, event ):
		event.Skip()

	def m_radioBtn1OnRadioButtonSoal24( self, event ):
		event.Skip()

	def m_radioBtn2OnRadioButtonSoal60( self, event ):
		event.Skip()

	def m_radioBtn3OnRadioButtonSoal100( self, event ):
		event.Skip()

	def m_button4OnButtonClick24( self, event ):
		event.Skip()

	def m_button5OnButtonClick60( self, event ):
		event.Skip()

	def m_button6OnButtonClick100( self, event ):
		event.Skip()

	def m_button7OnButtonClick( self, event ):
		event.Skip()

	def m_button8OnButtonClick( self, event ):
		event.Skip()

	def m_button9OnButtonClick( self, event ):
		event.Skip()

	def m_button10OnButtonClick( self, event ):
		event.Skip()

	def m_button11OnButtonClick( self, event ):
		event.Skip()

	def m_button12OnButtonClick( self, event ):
		event.Skip()

	def m_button1OnButtonClick( self, event ):
		event.Skip()

	def m_button2OnButtonClick( self, event ):
		event.Skip()

	def m_button3OnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass


###########################################################################
## Class FrameGrafik
###########################################################################

class FrameGrafik ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


