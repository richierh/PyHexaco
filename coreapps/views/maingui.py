# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Jan 12 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
from wx.lib.agw import ultimatelistctrl as ULC

###########################################################################
## Class FrameDepan
###########################################################################

class FrameDepan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 950,900 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel12.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer141 = wx.BoxSizer( wx.VERTICAL )

		self.m_simplebook1 = wx.Simplebook( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )
		self.m_panel1.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )


		bSizer5.Add( ( 0, 50), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText212 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"HEXACO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )

		self.m_staticText212.SetFont( wx.Font( 48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_staticText212.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer5.Add( self.m_staticText212, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer5.Add( ( 0, 50), 0, 0, 5 )

		self.m_panel121 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel121.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_panel121.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer191 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1071 = wx.StaticText( self.m_panel121, wx.ID_ANY, u"HEXACO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1071.Wrap( -1 )

		self.m_staticText1071.Hide()

		bSizer191.Add( self.m_staticText1071, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer15 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer15.AddGrowableCol( 0 )
		fgSizer15.AddGrowableCol( 1 )
		fgSizer15.AddGrowableRow( 0 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer11 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self.m_panel121, wx.ID_ANY, u"No Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.m_panel121, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer11.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel121, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_datePicker1 = wx.adv.DatePickerCtrl( self.m_panel121, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( -1,-1 ), wx.adv.DP_DEFAULT )
		self.m_datePicker1.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_datePicker1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer11.Add( self.m_datePicker1, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self.m_panel121, wx.ID_ANY, u"Nama Kandidat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self.m_panel121, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer11.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self.m_panel121, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText4.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice1Choices = [ u"Laki - Laki", u"Perempuan" ]
		self.m_choice1 = wx.Choice( self.m_panel121, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		self.m_choice1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer11.Add( self.m_choice1, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self.m_panel121, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText5.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_datePicker2 = wx.adv.DatePickerCtrl( self.m_panel121, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		self.m_datePicker2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer11.Add( self.m_datePicker2, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self.m_panel121, wx.ID_ANY, u"Pendidikan Terakhir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText6.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice2Choices = [ u"SD", u"SMP", u"SMA", u"Diploma", u"S1", u"S2", u"S3" ]
		self.m_choice2 = wx.Choice( self.m_panel121, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 4 )
		self.m_choice2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer11.Add( self.m_choice2, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self.m_panel121, wx.ID_ANY, u"Jurusan Pendidikan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText7.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self.m_panel121, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer11.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self.m_panel121, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText8.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self.m_panel121, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer11.Add( self.m_textCtrl8, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel121, wx.ID_ANY, u"Perusahaan/Instansi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText9.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self.m_panel121, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		fgSizer11.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self.m_panel121, wx.ID_ANY, u"Posisi / Jabatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self.m_panel121, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		fgSizer11.Add( self.m_textCtrl10, 0, wx.ALL, 5 )


		fgSizer15.Add( fgSizer11, 1, wx.EXPAND, 5 )


		fgSizer15.Add( ( 60, 0), 0, wx.RIGHT, 5 )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self.m_panel121, wx.ID_ANY, u"HEXACO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_staticText11.Hide()

		bSizer19.Add( self.m_staticText11, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bitmap1 = wx.StaticBitmap( self.m_panel121, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_bitmap1, 5, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer15.Add( bSizer19, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer191.Add( fgSizer15, 1, wx.EXPAND, 5 )


		self.m_panel121.SetSizer( bSizer191 )
		self.m_panel121.Layout()
		bSizer191.Fit( self.m_panel121 )
		bSizer5.Add( self.m_panel121, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer5 )
		self.m_panel1.Layout()
		bSizer5.Fit( self.m_panel1 )
		self.m_simplebook1.AddPage( self.m_panel1, u"a page", True )
		self.m_panel2 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel6 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer142 = wx.BoxSizer( wx.VERTICAL )


		bSizer142.Add( ( 0, 50), 0, 0, 5 )

		self.m_staticText13 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"VERSI HEXACO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_staticText13.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_staticText13.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer142.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer142.Add( ( 0, 0), 0, 0, 5 )

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

		self.m_button4 = wx.Button( self.m_panel6, wx.ID_ANY, u"24 Soal", wx.DefaultPosition, wx.Size( 300,100 ), 0 )
		self.m_button4.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_button4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer1.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.m_button5 = wx.Button( self.m_panel6, wx.ID_ANY, u"60 Soal", wx.DefaultPosition, wx.Size( 300,100 ), 0 )
		self.m_button5.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_button5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer1.Add( self.m_button5, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button6 = wx.Button( self.m_panel6, wx.ID_ANY, u"100 Soal", wx.DefaultPosition, wx.Size( 300,100 ), 0 )
		self.m_button6.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_button6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

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
		self.m_panel3 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel7.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )
		self.m_panel7.Hide()

		bSizer172 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow2 = wx.ScrolledWindow( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		self.m_scrolledWindow2.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )


		bSizer10.Add( ( 0, 50), 1, 0, 5 )

		self.m_staticText47 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"VERSI 24", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		self.m_staticText47.SetFont( wx.Font( 48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_staticText47.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer10.Add( self.m_staticText47, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer10.Add( ( 0, 50), 1, 0, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText15 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		fgSizer9.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		fgSizer9.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		fgSizer9.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl13, 0, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		fgSizer9.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl14, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		fgSizer9.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl15, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		fgSizer9.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl16 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_textCtrl16, 0, wx.ALL, 5 )


		bSizer11.Add( fgSizer9, 0, wx.EXPAND, 5 )


		bSizer11.Add( ( 50, 0), 0, 0, 5 )

		fgSizer13 = wx.FlexGridSizer( 6, 2, 0, 0 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText21 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		fgSizer13.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl17 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.m_textCtrl17, 0, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		fgSizer13.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.m_textCtrl18, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		fgSizer13.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.m_textCtrl19, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		fgSizer13.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.m_textCtrl20, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		fgSizer13.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.m_textCtrl21, 0, wx.ALL, 5 )

		self.m_staticText38 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		fgSizer13.Add( self.m_staticText38, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.m_textCtrl22, 0, wx.ALL, 5 )


		bSizer11.Add( fgSizer13, 0, wx.EXPAND, 5 )


		bSizer11.Add( ( 50, 0), 0, 0, 5 )

		fgSizer10 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText26 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		fgSizer10.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl23 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl23, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText27 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		fgSizer10.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl24, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText28 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		fgSizer10.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl25 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl25, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText29 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		fgSizer10.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl26 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText30 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		fgSizer10.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl27 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl27, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText31 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		fgSizer10.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl28 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_textCtrl28, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer11.Add( fgSizer10, 0, wx.EXPAND, 5 )


		bSizer11.Add( ( 50, 0), 0, 0, 5 )

		fgSizer14 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText32 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"19", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		fgSizer14.Add( self.m_staticText32, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl29 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_textCtrl29, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText33 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		fgSizer14.Add( self.m_staticText33, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl30 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_textCtrl30, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText34 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"21", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		fgSizer14.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl31 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_textCtrl31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText35 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"22", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		fgSizer14.Add( self.m_staticText35, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl32 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_textCtrl32, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText36 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"23", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		fgSizer14.Add( self.m_staticText36, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl33 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_textCtrl33, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText37 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"24", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		fgSizer14.Add( self.m_staticText37, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl34 = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_textCtrl34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer11.Add( fgSizer14, 1, wx.EXPAND, 5 )


		bSizer10.Add( bSizer11, 5, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_scrolledWindow2.SetSizer( bSizer10 )
		self.m_scrolledWindow2.Layout()
		bSizer10.Fit( self.m_scrolledWindow2 )
		bSizer172.Add( self.m_scrolledWindow2, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel7.SetSizer( bSizer172 )
		self.m_panel7.Layout()
		bSizer172.Fit( self.m_panel7 )
		bSizer6.Add( self.m_panel7, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_panel8 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel8.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow31 = wx.ScrolledWindow( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow31.SetScrollRate( 5, 5 )
		self.m_scrolledWindow31.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )


		bSizer16.Add( ( 0, 0), 1, 0, 5 )

		self.m_staticText48 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"VERSI 60", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		self.m_staticText48.SetFont( wx.Font( 48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_staticText48.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer16.Add( self.m_staticText48, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer16.Add( ( 0, 0), 1, 0, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer51 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer51.SetFlexibleDirection( wx.BOTH )
		fgSizer51.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText49 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		fgSizer51.Add( self.m_staticText49, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl42 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl42, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText50 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		fgSizer51.Add( self.m_staticText50, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl43 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl43, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText51 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		fgSizer51.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl44 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl44, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText52 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		fgSizer51.Add( self.m_staticText52, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl45 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl45, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText53 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		fgSizer51.Add( self.m_staticText53, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl46 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl46, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText54 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )

		fgSizer51.Add( self.m_staticText54, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl47 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl47, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText55 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		fgSizer51.Add( self.m_staticText55, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl48 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl48, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText56 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )

		fgSizer51.Add( self.m_staticText56, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl49 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl49, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText57 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )

		fgSizer51.Add( self.m_staticText57, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl50 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl50, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText58 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )

		fgSizer51.Add( self.m_staticText58, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl51 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer51.Add( self.m_textCtrl51, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer14.Add( fgSizer51, 0, 0, 5 )


		bSizer14.Add( ( 50, 0), 0, 0, 5 )

		fgSizer6 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText59 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )

		fgSizer6.Add( self.m_staticText59, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl52 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl52, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText60 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )

		fgSizer6.Add( self.m_staticText60, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl53 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl53, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText61 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		fgSizer6.Add( self.m_staticText61, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl54 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl54, 0, wx.ALL, 5 )

		self.m_staticText62 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )

		fgSizer6.Add( self.m_staticText62, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl55 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl55, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText63 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )

		fgSizer6.Add( self.m_staticText63, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl56 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl56, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText64 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )

		fgSizer6.Add( self.m_staticText64, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl57 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl57, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText65 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )

		fgSizer6.Add( self.m_staticText65, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl58 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl58, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText66 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66.Wrap( -1 )

		fgSizer6.Add( self.m_staticText66, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl59 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl59, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText67 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"19", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText67.Wrap( -1 )

		fgSizer6.Add( self.m_staticText67, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl60 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl60, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText68 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )

		fgSizer6.Add( self.m_staticText68, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl61 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_textCtrl61, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer14.Add( fgSizer6, 0, 0, 5 )


		bSizer14.Add( ( 50, 0), 0, 0, 5 )

		fgSizer7 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText69 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"21", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )

		fgSizer7.Add( self.m_staticText69, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl62 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl62, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText70 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"22", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText70.Wrap( -1 )

		fgSizer7.Add( self.m_staticText70, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl63 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl63, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText71 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"23", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		fgSizer7.Add( self.m_staticText71, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl64 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl64, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText72 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"24", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText72.Wrap( -1 )

		fgSizer7.Add( self.m_staticText72, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl65 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl65, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText73 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"25", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText73.Wrap( -1 )

		fgSizer7.Add( self.m_staticText73, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl66 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl66, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText74 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"26", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText74.Wrap( -1 )

		fgSizer7.Add( self.m_staticText74, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl67 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl67, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText75 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"27", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText75.Wrap( -1 )

		fgSizer7.Add( self.m_staticText75, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl68 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl68, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText76 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"28", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText76.Wrap( -1 )

		fgSizer7.Add( self.m_staticText76, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl69 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl69, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText77 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"29", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )

		fgSizer7.Add( self.m_staticText77, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl70 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl70, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText78 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"30", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( -1 )

		fgSizer7.Add( self.m_staticText78, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl71 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl71, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer14.Add( fgSizer7, 0, 0, 5 )


		bSizer14.Add( ( 50, 0), 0, 0, 5 )

		fgSizer8 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText79 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"31", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )

		fgSizer8.Add( self.m_staticText79, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl72 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl72, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText80 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"32", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )

		fgSizer8.Add( self.m_staticText80, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl73 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl73, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText81 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"33", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		fgSizer8.Add( self.m_staticText81, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl74 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl74, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText82 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"34", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )

		fgSizer8.Add( self.m_staticText82, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl75 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl75, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText83 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"35", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )

		fgSizer8.Add( self.m_staticText83, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl76 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl76, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText84 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"36", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )

		fgSizer8.Add( self.m_staticText84, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl77 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl77, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText85 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"37", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )

		fgSizer8.Add( self.m_staticText85, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl78 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl78, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText86 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"38", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )

		fgSizer8.Add( self.m_staticText86, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl79 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl79, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText87 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"39", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText87.Wrap( -1 )

		fgSizer8.Add( self.m_staticText87, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl80 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl80, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText88 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"40", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )

		fgSizer8.Add( self.m_staticText88, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl81 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_textCtrl81, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer14.Add( fgSizer8, 0, 0, 5 )


		bSizer14.Add( ( 50, 0), 0, 0, 5 )

		fgSizer91 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer91.SetFlexibleDirection( wx.BOTH )
		fgSizer91.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText89 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"41", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText89.Wrap( -1 )

		fgSizer91.Add( self.m_staticText89, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl82 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl82, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText90 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"42", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText90.Wrap( -1 )

		fgSizer91.Add( self.m_staticText90, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl83 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl83, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText91 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"43", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		fgSizer91.Add( self.m_staticText91, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl84 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl84, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText92 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"44", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText92.Wrap( -1 )

		fgSizer91.Add( self.m_staticText92, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl85 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl85, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText93 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"45", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText93.Wrap( -1 )

		fgSizer91.Add( self.m_staticText93, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl86 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl86, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText94 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"46", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText94.Wrap( -1 )

		fgSizer91.Add( self.m_staticText94, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl87 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl87, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText95 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"47", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText95.Wrap( -1 )

		fgSizer91.Add( self.m_staticText95, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl88 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl88, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText96 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"48", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText96.Wrap( -1 )

		fgSizer91.Add( self.m_staticText96, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl89 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl89, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText97 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"49", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText97.Wrap( -1 )

		fgSizer91.Add( self.m_staticText97, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl90 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl90, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText98 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"50", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText98.Wrap( -1 )

		fgSizer91.Add( self.m_staticText98, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl91 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_textCtrl91, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer14.Add( fgSizer91, 0, 0, 5 )


		bSizer14.Add( ( 50, 0), 0, 0, 5 )

		fgSizer101 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer101.SetFlexibleDirection( wx.BOTH )
		fgSizer101.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText99 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"51", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText99.Wrap( -1 )

		fgSizer101.Add( self.m_staticText99, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl92 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl92, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText100 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"52", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText100.Wrap( -1 )

		fgSizer101.Add( self.m_staticText100, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl93 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl93, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText101 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"53", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		fgSizer101.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl94 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl94, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText102 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"54", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText102.Wrap( -1 )

		fgSizer101.Add( self.m_staticText102, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl95 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl95, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText103 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"55", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText103.Wrap( -1 )

		fgSizer101.Add( self.m_staticText103, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl96 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl96, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText104 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"56", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText104.Wrap( -1 )

		fgSizer101.Add( self.m_staticText104, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl97 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl97, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText105 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"57", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText105.Wrap( -1 )

		fgSizer101.Add( self.m_staticText105, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl98 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl98, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText106 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"58", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText106.Wrap( -1 )

		fgSizer101.Add( self.m_staticText106, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl99 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl99, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText107 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"59", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText107.Wrap( -1 )

		fgSizer101.Add( self.m_staticText107, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl100 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl100, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText108 = wx.StaticText( self.m_scrolledWindow31, wx.ID_ANY, u"60", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText108.Wrap( -1 )

		fgSizer101.Add( self.m_staticText108, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl101 = wx.TextCtrl( self.m_scrolledWindow31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer101.Add( self.m_textCtrl101, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer14.Add( fgSizer101, 0, 0, 5 )


		bSizer16.Add( bSizer14, 5, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_scrolledWindow31.SetSizer( bSizer16 )
		self.m_scrolledWindow31.Layout()
		bSizer16.Fit( self.m_scrolledWindow31 )
		bSizer21.Add( self.m_scrolledWindow31, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel8.SetSizer( bSizer21 )
		self.m_panel8.Layout()
		bSizer21.Fit( self.m_panel8 )
		bSizer6.Add( self.m_panel8, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_panel9 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel9.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )
		self.m_panel9.Hide()

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow4 = wx.ScrolledWindow( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow4.SetScrollRate( 5, 5 )
		self.m_scrolledWindow4.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )


		bSizer17.Add( ( 0, 50), 1, 0, 5 )

		self.m_staticText1081 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"VERSI 100", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1081.Wrap( -1 )

		self.m_staticText1081.SetFont( wx.Font( 48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_staticText1081.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer17.Add( self.m_staticText1081, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer17.Add( ( 0, 50), 1, 0, 5 )

		bSizer171 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer151 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer151.SetFlexibleDirection( wx.BOTH )
		fgSizer151.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText109 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText109.Wrap( -1 )

		fgSizer151.Add( self.m_staticText109, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl981 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer151.Add( self.m_textCtrl981, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText110 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText110.Wrap( -1 )

		fgSizer151.Add( self.m_staticText110, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl991 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer151.Add( self.m_textCtrl991, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText111 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		fgSizer151.Add( self.m_staticText111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl1001 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer151.Add( self.m_textCtrl1001, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText112 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText112.Wrap( -1 )

		fgSizer151.Add( self.m_staticText112, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl1011 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer151.Add( self.m_textCtrl1011, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText113 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText113.Wrap( -1 )

		fgSizer151.Add( self.m_staticText113, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl102 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer151.Add( self.m_textCtrl102, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText114 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText114.Wrap( -1 )

		fgSizer151.Add( self.m_staticText114, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl103 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer151.Add( self.m_textCtrl103, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText115 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText115.Wrap( -1 )

		fgSizer151.Add( self.m_staticText115, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl104 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer151.Add( self.m_textCtrl104, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText116 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText116.Wrap( -1 )

		fgSizer151.Add( self.m_staticText116, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl105 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer151.Add( self.m_textCtrl105, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText117 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText117.Wrap( -1 )

		fgSizer151.Add( self.m_staticText117, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl106 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer151.Add( self.m_textCtrl106, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText118 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText118.Wrap( -1 )

		fgSizer151.Add( self.m_staticText118, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl107 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer151.Add( self.m_textCtrl107, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer171.Add( fgSizer151, 0, 0, 5 )


		bSizer171.Add( ( 35, 0), 0, 0, 5 )

		fgSizer16 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText119 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText119.Wrap( -1 )

		fgSizer16.Add( self.m_staticText119, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl108 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer16.Add( self.m_textCtrl108, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText120 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText120.Wrap( -1 )

		fgSizer16.Add( self.m_staticText120, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl109 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer16.Add( self.m_textCtrl109, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText121 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		fgSizer16.Add( self.m_staticText121, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl110 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer16.Add( self.m_textCtrl110, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText122 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText122.Wrap( -1 )

		fgSizer16.Add( self.m_staticText122, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl111 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer16.Add( self.m_textCtrl111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText123 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText123.Wrap( -1 )

		fgSizer16.Add( self.m_staticText123, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl112 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer16.Add( self.m_textCtrl112, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText124 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText124.Wrap( -1 )

		fgSizer16.Add( self.m_staticText124, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl113 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer16.Add( self.m_textCtrl113, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText125 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText125.Wrap( -1 )

		fgSizer16.Add( self.m_staticText125, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl114 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer16.Add( self.m_textCtrl114, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText126 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText126.Wrap( -1 )

		fgSizer16.Add( self.m_staticText126, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl115 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer16.Add( self.m_textCtrl115, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText127 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"19", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText127.Wrap( -1 )

		fgSizer16.Add( self.m_staticText127, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl116 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer16.Add( self.m_textCtrl116, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText128 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText128.Wrap( -1 )

		fgSizer16.Add( self.m_staticText128, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl117 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer16.Add( self.m_textCtrl117, 0, wx.ALL, 5 )


		bSizer171.Add( fgSizer16, 0, 0, 5 )


		bSizer171.Add( ( 35, 0), 0, 0, 5 )

		fgSizer17 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText129 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"21", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText129.Wrap( -1 )

		fgSizer17.Add( self.m_staticText129, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl118 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer17.Add( self.m_textCtrl118, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText130 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"22", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText130.Wrap( -1 )

		fgSizer17.Add( self.m_staticText130, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl119 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer17.Add( self.m_textCtrl119, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText131 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"23", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )

		fgSizer17.Add( self.m_staticText131, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl120 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer17.Add( self.m_textCtrl120, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText132 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"24", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText132.Wrap( -1 )

		fgSizer17.Add( self.m_staticText132, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl121 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer17.Add( self.m_textCtrl121, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText133 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"25", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText133.Wrap( -1 )

		fgSizer17.Add( self.m_staticText133, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl122 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer17.Add( self.m_textCtrl122, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText134 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"26", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText134.Wrap( -1 )

		fgSizer17.Add( self.m_staticText134, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl123 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer17.Add( self.m_textCtrl123, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText135 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"27", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText135.Wrap( -1 )

		fgSizer17.Add( self.m_staticText135, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl124 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer17.Add( self.m_textCtrl124, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText136 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"28", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText136.Wrap( -1 )

		fgSizer17.Add( self.m_staticText136, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl125 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer17.Add( self.m_textCtrl125, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText137 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"29", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText137.Wrap( -1 )

		fgSizer17.Add( self.m_staticText137, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl126 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer17.Add( self.m_textCtrl126, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText138 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"30", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText138.Wrap( -1 )

		fgSizer17.Add( self.m_staticText138, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl127 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer17.Add( self.m_textCtrl127, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer171.Add( fgSizer17, 0, 0, 5 )


		bSizer171.Add( ( 35, 0), 0, 0, 5 )

		fgSizer18 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText139 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"31", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText139.Wrap( -1 )

		fgSizer18.Add( self.m_staticText139, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl128 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer18.Add( self.m_textCtrl128, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText140 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"32", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText140.Wrap( -1 )

		fgSizer18.Add( self.m_staticText140, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl129 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer18.Add( self.m_textCtrl129, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText141 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"33", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )

		fgSizer18.Add( self.m_staticText141, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl130 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer18.Add( self.m_textCtrl130, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText142 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"34", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText142.Wrap( -1 )

		fgSizer18.Add( self.m_staticText142, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl131 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer18.Add( self.m_textCtrl131, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText143 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"35", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText143.Wrap( -1 )

		fgSizer18.Add( self.m_staticText143, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl132 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer18.Add( self.m_textCtrl132, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText144 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"36", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText144.Wrap( -1 )

		fgSizer18.Add( self.m_staticText144, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl133 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer18.Add( self.m_textCtrl133, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText145 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"37", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText145.Wrap( -1 )

		fgSizer18.Add( self.m_staticText145, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl134 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer18.Add( self.m_textCtrl134, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText146 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"38", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText146.Wrap( -1 )

		fgSizer18.Add( self.m_staticText146, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl135 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer18.Add( self.m_textCtrl135, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText147 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"39", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText147.Wrap( -1 )

		fgSizer18.Add( self.m_staticText147, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl136 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer18.Add( self.m_textCtrl136, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText148 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"40", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText148.Wrap( -1 )

		fgSizer18.Add( self.m_staticText148, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl137 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer18.Add( self.m_textCtrl137, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer171.Add( fgSizer18, 0, 0, 5 )


		bSizer171.Add( ( 35, 0), 0, 0, 5 )

		fgSizer19 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer19.SetFlexibleDirection( wx.BOTH )
		fgSizer19.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText150 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"41", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText150.Wrap( -1 )

		fgSizer19.Add( self.m_staticText150, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl139 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer19.Add( self.m_textCtrl139, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText151 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"42", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )

		fgSizer19.Add( self.m_staticText151, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl140 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer19.Add( self.m_textCtrl140, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText152 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"43", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText152.Wrap( -1 )

		fgSizer19.Add( self.m_staticText152, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl141 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer19.Add( self.m_textCtrl141, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText153 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"44", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText153.Wrap( -1 )

		fgSizer19.Add( self.m_staticText153, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl142 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer19.Add( self.m_textCtrl142, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText154 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"45", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText154.Wrap( -1 )

		fgSizer19.Add( self.m_staticText154, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl143 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer19.Add( self.m_textCtrl143, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText155 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"46", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText155.Wrap( -1 )

		fgSizer19.Add( self.m_staticText155, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl144 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer19.Add( self.m_textCtrl144, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText156 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"47", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText156.Wrap( -1 )

		fgSizer19.Add( self.m_staticText156, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl145 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer19.Add( self.m_textCtrl145, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText157 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"48", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText157.Wrap( -1 )

		fgSizer19.Add( self.m_staticText157, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl146 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer19.Add( self.m_textCtrl146, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText158 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"49", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText158.Wrap( -1 )

		fgSizer19.Add( self.m_staticText158, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl147 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer19.Add( self.m_textCtrl147, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText159 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"50", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText159.Wrap( -1 )

		fgSizer19.Add( self.m_staticText159, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl148 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer19.Add( self.m_textCtrl148, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer171.Add( fgSizer19, 0, 0, 5 )


		bSizer171.Add( ( 35, 0), 0, 0, 5 )

		fgSizer20 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText160 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"51", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText160.Wrap( -1 )

		fgSizer20.Add( self.m_staticText160, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl149 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer20.Add( self.m_textCtrl149, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText161 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"52", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )

		fgSizer20.Add( self.m_staticText161, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl150 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer20.Add( self.m_textCtrl150, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText162 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"53", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText162.Wrap( -1 )

		fgSizer20.Add( self.m_staticText162, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl151 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer20.Add( self.m_textCtrl151, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText163 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"54", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText163.Wrap( -1 )

		fgSizer20.Add( self.m_staticText163, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl152 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer20.Add( self.m_textCtrl152, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText164 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"55", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText164.Wrap( -1 )

		fgSizer20.Add( self.m_staticText164, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl153 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer20.Add( self.m_textCtrl153, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText165 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"56", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText165.Wrap( -1 )

		fgSizer20.Add( self.m_staticText165, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl154 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer20.Add( self.m_textCtrl154, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText166 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"57", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText166.Wrap( -1 )

		fgSizer20.Add( self.m_staticText166, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl155 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer20.Add( self.m_textCtrl155, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText167 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"58", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText167.Wrap( -1 )

		fgSizer20.Add( self.m_staticText167, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl156 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer20.Add( self.m_textCtrl156, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText168 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"59", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText168.Wrap( -1 )

		fgSizer20.Add( self.m_staticText168, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl157 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer20.Add( self.m_textCtrl157, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText169 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"60", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText169.Wrap( -1 )

		fgSizer20.Add( self.m_staticText169, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl158 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer20.Add( self.m_textCtrl158, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer171.Add( fgSizer20, 0, 0, 5 )


		bSizer171.Add( ( 35, 0), 0, 0, 5 )

		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText180 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"61", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText180.Wrap( -1 )

		fgSizer21.Add( self.m_staticText180, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl159 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl159, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText170 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"62", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText170.Wrap( -1 )

		fgSizer21.Add( self.m_staticText170, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl160 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl160, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText171 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"63", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )

		fgSizer21.Add( self.m_staticText171, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl161 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl161, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText172 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"64", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText172.Wrap( -1 )

		fgSizer21.Add( self.m_staticText172, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl162 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl162, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText173 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"65", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText173.Wrap( -1 )

		fgSizer21.Add( self.m_staticText173, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl163 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl163, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText174 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"66", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText174.Wrap( -1 )

		fgSizer21.Add( self.m_staticText174, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl164 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl164, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText175 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"67", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText175.Wrap( -1 )

		fgSizer21.Add( self.m_staticText175, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl165 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl165, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText176 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"68", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText176.Wrap( -1 )

		fgSizer21.Add( self.m_staticText176, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl166 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl166, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText177 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"69", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText177.Wrap( -1 )

		fgSizer21.Add( self.m_staticText177, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl167 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl167, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText178 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"70", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText178.Wrap( -1 )

		fgSizer21.Add( self.m_staticText178, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl168 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer21.Add( self.m_textCtrl168, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer171.Add( fgSizer21, 0, 0, 5 )


		bSizer171.Add( ( 35, 0), 0, 0, 5 )

		fgSizer22 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText181 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"71", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )

		fgSizer22.Add( self.m_staticText181, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl170 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer22.Add( self.m_textCtrl170, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText182 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"72", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText182.Wrap( -1 )

		fgSizer22.Add( self.m_staticText182, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl171 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer22.Add( self.m_textCtrl171, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText183 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"73", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText183.Wrap( -1 )

		fgSizer22.Add( self.m_staticText183, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl172 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer22.Add( self.m_textCtrl172, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText184 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"74", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText184.Wrap( -1 )

		fgSizer22.Add( self.m_staticText184, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl173 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer22.Add( self.m_textCtrl173, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText185 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"75", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText185.Wrap( -1 )

		fgSizer22.Add( self.m_staticText185, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl174 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer22.Add( self.m_textCtrl174, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText186 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"76", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText186.Wrap( -1 )

		fgSizer22.Add( self.m_staticText186, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl175 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer22.Add( self.m_textCtrl175, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText187 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"77", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText187.Wrap( -1 )

		fgSizer22.Add( self.m_staticText187, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl176 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer22.Add( self.m_textCtrl176, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText188 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"78", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText188.Wrap( -1 )

		fgSizer22.Add( self.m_staticText188, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl177 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer22.Add( self.m_textCtrl177, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText189 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"79", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText189.Wrap( -1 )

		fgSizer22.Add( self.m_staticText189, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl178 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer22.Add( self.m_textCtrl178, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText190 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"80", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText190.Wrap( -1 )

		fgSizer22.Add( self.m_staticText190, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl179 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer22.Add( self.m_textCtrl179, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer171.Add( fgSizer22, 0, 0, 5 )


		bSizer171.Add( ( 35, 0), 0, 0, 5 )

		fgSizer23 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer23.SetFlexibleDirection( wx.BOTH )
		fgSizer23.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText192 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"81", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText192.Wrap( -1 )

		fgSizer23.Add( self.m_staticText192, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl181 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer23.Add( self.m_textCtrl181, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText193 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"82", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText193.Wrap( -1 )

		fgSizer23.Add( self.m_staticText193, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl182 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer23.Add( self.m_textCtrl182, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText194 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"83", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText194.Wrap( -1 )

		fgSizer23.Add( self.m_staticText194, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl183 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer23.Add( self.m_textCtrl183, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText195 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"84", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText195.Wrap( -1 )

		fgSizer23.Add( self.m_staticText195, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl184 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer23.Add( self.m_textCtrl184, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText196 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"85", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText196.Wrap( -1 )

		fgSizer23.Add( self.m_staticText196, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl185 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer23.Add( self.m_textCtrl185, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText197 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"86", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText197.Wrap( -1 )

		fgSizer23.Add( self.m_staticText197, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl186 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer23.Add( self.m_textCtrl186, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText198 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"87", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText198.Wrap( -1 )

		fgSizer23.Add( self.m_staticText198, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl187 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer23.Add( self.m_textCtrl187, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText199 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"88", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText199.Wrap( -1 )

		fgSizer23.Add( self.m_staticText199, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl188 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer23.Add( self.m_textCtrl188, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText200 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"89", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText200.Wrap( -1 )

		fgSizer23.Add( self.m_staticText200, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl189 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer23.Add( self.m_textCtrl189, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText201 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"90", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText201.Wrap( -1 )

		fgSizer23.Add( self.m_staticText201, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl190 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer23.Add( self.m_textCtrl190, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer171.Add( fgSizer23, 0, 0, 5 )


		bSizer171.Add( ( 35, 0), 0, 0, 5 )

		fgSizer24 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText202 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"91", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText202.Wrap( -1 )

		fgSizer24.Add( self.m_staticText202, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl191 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer24.Add( self.m_textCtrl191, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText203 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"92", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText203.Wrap( -1 )

		fgSizer24.Add( self.m_staticText203, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl192 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer24.Add( self.m_textCtrl192, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText204 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"93", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText204.Wrap( -1 )

		fgSizer24.Add( self.m_staticText204, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl193 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer24.Add( self.m_textCtrl193, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText205 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"94", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText205.Wrap( -1 )

		fgSizer24.Add( self.m_staticText205, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl194 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer24.Add( self.m_textCtrl194, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText206 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"95", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText206.Wrap( -1 )

		fgSizer24.Add( self.m_staticText206, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl195 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer24.Add( self.m_textCtrl195, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText207 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"96", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText207.Wrap( -1 )

		fgSizer24.Add( self.m_staticText207, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl196 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer24.Add( self.m_textCtrl196, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText208 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"97", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText208.Wrap( -1 )

		fgSizer24.Add( self.m_staticText208, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl197 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer24.Add( self.m_textCtrl197, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText209 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"98", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText209.Wrap( -1 )

		fgSizer24.Add( self.m_staticText209, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl198 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer24.Add( self.m_textCtrl198, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText210 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"99", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText210.Wrap( -1 )

		fgSizer24.Add( self.m_staticText210, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl199 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer24.Add( self.m_textCtrl199, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText211 = wx.StaticText( self.m_scrolledWindow4, wx.ID_ANY, u"100", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )

		fgSizer24.Add( self.m_staticText211, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl200 = wx.TextCtrl( self.m_scrolledWindow4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		fgSizer24.Add( self.m_textCtrl200, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer171.Add( fgSizer24, 0, 0, 5 )


		bSizer17.Add( bSizer171, 5, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_scrolledWindow4.SetSizer( bSizer17 )
		self.m_scrolledWindow4.Layout()
		bSizer17.Fit( self.m_scrolledWindow4 )
		bSizer24.Add( self.m_scrolledWindow4, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel9.SetSizer( bSizer24 )
		self.m_panel9.Layout()
		bSizer24.Fit( self.m_panel9 )
		bSizer6.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel3.SetSizer( bSizer6 )
		self.m_panel3.Layout()
		bSizer6.Fit( self.m_panel3 )
		self.m_simplebook1.AddPage( self.m_panel3, u"a page", False )
		self.m_panel4 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel10.Hide()

		bSizer8.Add( self.m_panel10, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_scrolledWindow3 = wx.ScrolledWindow( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow3.SetScrollRate( 5, 5 )
		self.m_scrolledWindow3.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel15 = wx.Panel( self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel15.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer91 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText213 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"GRAFIK HEXACO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText213.Wrap( -1 )

		self.m_staticText213.SetFont( wx.Font( 48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_staticText213.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer91.Add( self.m_staticText213, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.GrafikMatplotlib = wx.Panel( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,200 ), wx.TAB_TRAVERSAL )
		bSizer20.Add( self.GrafikMatplotlib, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.ALIGN_BOTTOM, 5 )


		bSizer91.Add( bSizer20, 3, wx.EXPAND, 5 )

		fgSizer26 = wx.FlexGridSizer( 2, 8, 0, 0 )
		fgSizer26.AddGrowableCol( 7 )
		fgSizer26.AddGrowableRow( 0 )
		fgSizer26.AddGrowableRow( 1 )
		fgSizer26.SetFlexibleDirection( wx.BOTH )
		fgSizer26.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText41 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Openess To Experience", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		self.m_staticText41.Hide()

		fgSizer26.Add( self.m_staticText41, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText42 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Conscientiouseness", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		self.m_staticText42.Hide()

		fgSizer26.Add( self.m_staticText42, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText43 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Agreeableness", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		self.m_staticText43.Hide()

		fgSizer26.Add( self.m_staticText43, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText44 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Extraversion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		self.m_staticText44.Hide()

		fgSizer26.Add( self.m_staticText44, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText45 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Emotionality", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		self.m_staticText45.Hide()

		fgSizer26.Add( self.m_staticText45, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText46 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Honesty – Humility", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		self.m_staticText46.Hide()

		fgSizer26.Add( self.m_staticText46, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText40 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"(Interstitial Facet Scale) Interstitial", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		self.m_staticText40.Hide()

		fgSizer26.Add( self.m_staticText40, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText214 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText214.Wrap( -1 )

		self.m_staticText214.Hide()

		fgSizer26.Add( self.m_staticText214, 0, wx.ALL, 5 )

		self.m_button_o = wx.Button( self.m_panel15, wx.ID_ANY, u"Openess To\nExperience", wx.DefaultPosition, wx.Size( 150,80 ), wx.BU_EXACTFIT )
		self.m_button_o.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer26.Add( self.m_button_o, 0, wx.ALL, 5 )

		self.m_button_c = wx.Button( self.m_panel15, wx.ID_ANY, u"Conscientiouseness", wx.DefaultPosition, wx.Size( 150,80 ), 0 )
		self.m_button_c.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer26.Add( self.m_button_c, 0, wx.ALL, 5 )

		self.m_button_a = wx.Button( self.m_panel15, wx.ID_ANY, u"Agreeableness", wx.DefaultPosition, wx.Size( 150,80 ), 0 )
		self.m_button_a.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer26.Add( self.m_button_a, 0, wx.ALL, 5 )

		self.m_button_ex = wx.Button( self.m_panel15, wx.ID_ANY, u"Extraversion", wx.DefaultPosition, wx.Size( 150,80 ), 0 )
		self.m_button_ex.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer26.Add( self.m_button_ex, 0, wx.ALL, 5 )

		self.m_button_em = wx.Button( self.m_panel15, wx.ID_ANY, u"Emotionality", wx.DefaultPosition, wx.Size( 150,80 ), 0 )
		self.m_button_em.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer26.Add( self.m_button_em, 0, wx.ALL, 5 )

		self.m_button_h = wx.Button( self.m_panel15, wx.ID_ANY, u"Honesty\nHumility", wx.DefaultPosition, wx.Size( 150,80 ), 0 )
		self.m_button_h.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer26.Add( self.m_button_h, 0, wx.ALL, 5 )

		self.m_button141 = wx.Button( self.m_panel15, wx.ID_ANY, u"Interstitial Facet", wx.DefaultPosition, wx.Size( 150,80 ), 0 )
		self.m_button141.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer26.Add( self.m_button141, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer40 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button22 = wx.Button( self.m_panel15, wx.ID_ANY, u"Lihat Biodata", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button22.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer40.Add( self.m_button22, 1, wx.ALL|wx.EXPAND, 5 )

		fgSizer29 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer29.AddGrowableCol( 0 )
		fgSizer29.SetFlexibleDirection( wx.BOTH )
		fgSizer29.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button_simpan_data = wx.Button( self.m_panel15, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_simpan_data.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer29.Add( self.m_button_simpan_data, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button_save_as_pdf = wx.Button( self.m_panel15, wx.ID_ANY, u"Save as PDF", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer29.Add( self.m_button_save_as_pdf, 0, wx.ALL, 5 )

		self.m_button_print = wx.Button( self.m_panel15, wx.ID_ANY, u"Print", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer29.Add( self.m_button_print, 0, wx.ALL, 5 )

		self.m_button21 = wx.Button( self.m_panel15, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button21.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer29.Add( self.m_button21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer40.Add( fgSizer29, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		fgSizer26.Add( bSizer40, 1, wx.EXPAND, 5 )


		bSizer91.Add( fgSizer26, 0, wx.EXPAND, 5 )


		self.m_panel15.SetSizer( bSizer91 )
		self.m_panel15.Layout()
		bSizer91.Fit( self.m_panel15 )
		bSizer29.Add( self.m_panel15, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_scrolledWindow3.SetSizer( bSizer29 )
		self.m_scrolledWindow3.Layout()
		bSizer29.Fit( self.m_scrolledWindow3 )
		bSizer8.Add( self.m_scrolledWindow3, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer8 )
		self.m_panel4.Layout()
		bSizer8.Fit( self.m_panel4 )
		self.m_simplebook1.AddPage( self.m_panel4, u"a page", True )
		self.m_panel18 = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel18.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook2 = wx.Notebook( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_notebook2.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		self.m_panel19 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel19.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText215 = wx.StaticText( self.m_panel19, wx.ID_ANY, u"KAMUS HEXACO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText215.Wrap( -1 )

		self.m_staticText215.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer26.Add( self.m_staticText215, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_listbox_kamus_hexacoChoices = [ u"Aesthetic Appreciation", u"Agreeableness", u"Anxiety", u"Conscientiousness", u"Creativity", u"Dependence", u"Diligence", u"Emotionality", u"Extraversion", u"Fairness", u"Fearfullness", u"Flexibility", u"Forgiveness", u"Gentleness", u"Greed Avoidance", u"Honesty & Humility", u"Inquisitiveness", u"Interstitial", u"Liveliness", u"Modesty", u"Openness to Experience", u"Organization", u"Patience", u"Perfectionism", u"Prudence", u"Sentimentality", u"Sincerity", u"Sociability", u"Social Boldness", u"Social Self Esteem", u"Unconventionality" ]
		self.m_listbox_kamus_hexaco = wx.ListBox( self.m_panel19, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listbox_kamus_hexacoChoices, wx.LB_ALWAYS_SB|wx.LB_SORT )
		self.m_listbox_kamus_hexaco.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer26.Add( self.m_listbox_kamus_hexaco, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl_kamus_hexaco = wx.TextCtrl( self.m_panel19, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer26.Add( self.m_textCtrl_kamus_hexaco, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel19.SetSizer( bSizer26 )
		self.m_panel19.Layout()
		bSizer26.Fit( self.m_panel19 )
		self.m_notebook2.AddPage( self.m_panel19, u"Kamus Hexaco", False )
		self.m_panel20 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel20.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_panel20.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel21 = wx.Panel( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel21.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		fgSizer271 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer271.AddGrowableCol( 0 )
		fgSizer271.SetFlexibleDirection( wx.BOTH )
		fgSizer271.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button_hapus_data_listctrl = wx.Button( self.m_panel21, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer271.Add( self.m_button_hapus_data_listctrl, 0, wx.ALL, 5 )

		self.m_button_buka_windows_filter = wx.Button( self.m_panel21, wx.ID_ANY, u"Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer271.Add( self.m_button_buka_windows_filter, 0, wx.ALL, 5 )

		self.m_button_lihat = wx.Button( self.m_panel21, wx.ID_ANY, u"Lihat", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer271.Add( self.m_button_lihat, 0, wx.ALL, 5 )


		self.m_panel21.SetSizer( fgSizer271 )
		self.m_panel21.Layout()
		fgSizer271.Fit( self.m_panel21 )
		bSizer27.Add( self.m_panel21, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_panel_tabel_database = wx.ScrolledWindow( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_panel_tabel_database.SetScrollRate( 5, 5 )
		self.m_panel_tabel_database.Hide()

		bSizer27.Add( self.m_panel_tabel_database, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel29 = wx.Panel( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer261 = wx.BoxSizer( wx.VERTICAL )

		self.m_listCtrl_tabel_database = wx.ListCtrl( self.m_panel29, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		self.m_listCtrl_tabel_database.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl_tabel_database.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer261.Add( self.m_listCtrl_tabel_database, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel29.SetSizer( bSizer261 )
		self.m_panel29.Layout()
		bSizer261.Fit( self.m_panel29 )
		bSizer27.Add( self.m_panel29, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel20.SetSizer( bSizer27 )
		self.m_panel20.Layout()
		bSizer27.Fit( self.m_panel20 )
		self.m_notebook2.AddPage( self.m_panel20, u"Database", True )

		bSizer25.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel18.SetSizer( bSizer25 )
		self.m_panel18.Layout()
		bSizer25.Fit( self.m_panel18 )
		self.m_simplebook1.AddPage( self.m_panel18, u"a page", False )

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
		self.m_button1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer5.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self.m_panel5, wx.ID_ANY, u"Sebelumnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_button2.Enable( False )

		fgSizer5.Add( self.m_button2, 0, wx.ALIGN_BOTTOM|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_RIGHT, 5 )

		self.m_button3 = wx.Button( self.m_panel5, wx.ID_ANY, u"Selanjutnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer5.Add( self.m_button3, 1, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		self.m_panel5.SetSizer( fgSizer5 )
		self.m_panel5.Layout()
		fgSizer5.Fit( self.m_panel5 )
		bSizer1.Add( self.m_panel5, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menubar1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Keluar", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menubar1.Append( self.m_menu1, u"File" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Kontak", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem2 )

		self.m_menubar1.Append( self.m_menu2, u"Tentang" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_radioBtn1.Bind( wx.EVT_RADIOBUTTON, self.m_radioBtn1OnRadioButtonSoal24 )
		self.m_radioBtn2.Bind( wx.EVT_RADIOBUTTON, self.m_radioBtn2OnRadioButtonSoal60 )
		self.m_radioBtn3.Bind( wx.EVT_RADIOBUTTON, self.m_radioBtn3OnRadioButtonSoal100 )
		self.m_button4.Bind( wx.EVT_BUTTON, self.m_button4OnButtonClick24 )
		self.m_button5.Bind( wx.EVT_BUTTON, self.m_button5OnButtonClick60 )
		self.m_button6.Bind( wx.EVT_BUTTON, self.m_button6OnButtonClick100 )
		self.m_button_o.Bind( wx.EVT_BUTTON, self.m_button_oOnButtonClick )
		self.m_button_c.Bind( wx.EVT_BUTTON, self.m_button_cOnButtonClick )
		self.m_button_a.Bind( wx.EVT_BUTTON, self.m_button_aOnButtonClick )
		self.m_button_ex.Bind( wx.EVT_BUTTON, self.m_button_exOnButtonClick )
		self.m_button_em.Bind( wx.EVT_BUTTON, self.m_button_emOnButtonClick )
		self.m_button_h.Bind( wx.EVT_BUTTON, self.m_button_hOnButtonClick )
		self.m_button141.Bind( wx.EVT_BUTTON, self.m_button_iaOnButtonClick )
		self.m_button22.Bind( wx.EVT_BUTTON, self.m_button_lihat_biodata )
		self.m_button_simpan_data.Bind( wx.EVT_BUTTON, self.m_button_simpan_dataOnButtonClick )
		self.m_button_save_as_pdf.Bind( wx.EVT_BUTTON, self.m_button_save_as_pdfOnButtonClick )
		self.m_button_print.Bind( wx.EVT_BUTTON, self.m_button_printOnButtonClick )
		self.m_button21.Bind( wx.EVT_BUTTON, self.m_button21_bersihkan )
		self.m_listbox_kamus_hexaco.Bind( wx.EVT_LISTBOX, self.m_listbox_kamus_hexacoOnListBox )
		self.m_button_hapus_data_listctrl.Bind( wx.EVT_BUTTON, self.m_button_hapus_data_listctrlOnButtonClick )
		self.m_button_buka_windows_filter.Bind( wx.EVT_BUTTON, self.m_button_buka_windows_filterOnButtonClick )
		self.m_button_lihat.Bind( wx.EVT_BUTTON, self.m_button_lihatOnButtonClick )
		self.m_listCtrl_tabel_database.Bind( wx.EVT_LEFT_DCLICK, self.m_listCtrl_tabel_databaseOnLeftDClick )
		self.m_listCtrl_tabel_database.Bind( wx.EVT_LIST_COL_BEGIN_DRAG, self.m_listCtrl_tabel_databaseOnListColBeginDrag )
		self.m_listCtrl_tabel_database.Bind( wx.EVT_LIST_ITEM_RIGHT_CLICK, self.m_listCtrl_tabel_databaseOnListItemRightClick )
		self.m_listCtrl_tabel_database.Bind( wx.EVT_LIST_ITEM_SELECTED, self.m_listCtrl_tabel_databaseOnListItemSelected )
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
		self.m_button2.Bind( wx.EVT_BUTTON, self.m_button2OnButtonClick )
		self.m_button3.Bind( wx.EVT_BUTTON, self.m_button3OnButtonClick )
		self.Bind( wx.EVT_MENU, self.m_menuItem1OnMenuSelection, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem2OnMenuSelection, id = self.m_menuItem2.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
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

	def m_button_oOnButtonClick( self, event ):
		event.Skip()

	def m_button_cOnButtonClick( self, event ):
		event.Skip()

	def m_button_aOnButtonClick( self, event ):
		event.Skip()

	def m_button_exOnButtonClick( self, event ):
		event.Skip()

	def m_button_emOnButtonClick( self, event ):
		event.Skip()

	def m_button_hOnButtonClick( self, event ):
		event.Skip()

	def m_button_iaOnButtonClick( self, event ):
		event.Skip()

	def m_button_lihat_biodata( self, event ):
		event.Skip()

	def m_button_simpan_dataOnButtonClick( self, event ):
		event.Skip()

	def m_button_save_as_pdfOnButtonClick( self, event ):
		event.Skip()

	def m_button_printOnButtonClick( self, event ):
		event.Skip()

	def m_button21_bersihkan( self, event ):
		event.Skip()

	def m_listbox_kamus_hexacoOnListBox( self, event ):
		event.Skip()

	def m_button_hapus_data_listctrlOnButtonClick( self, event ):
		event.Skip()

	def m_button_buka_windows_filterOnButtonClick( self, event ):
		event.Skip()

	def m_button_lihatOnButtonClick( self, event ):
		event.Skip()

	def m_listCtrl_tabel_databaseOnLeftDClick( self, event ):
		event.Skip()

	def m_listCtrl_tabel_databaseOnListColBeginDrag( self, event ):
		event.Skip()

	def m_listCtrl_tabel_databaseOnListItemRightClick( self, event ):
		event.Skip()

	def m_listCtrl_tabel_databaseOnListItemSelected( self, event ):
		event.Skip()

	def m_button1OnButtonClick( self, event ):
		event.Skip()

	def m_button2OnButtonClick( self, event ):
		event.Skip()

	def m_button3OnButtonClick( self, event ):
		event.Skip()

	def m_menuItem1OnMenuSelection( self, event ):
		event.Skip()

	def m_menuItem2OnMenuSelection( self, event ):
		event.Skip()


###########################################################################
## Class TentangAplikasi
###########################################################################

class TentangAplikasi ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Binakarir", pos = wx.DefaultPosition, size = wx.Size( 600,350 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel26 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel26.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel24 = wx.Panel( self.m_panel26, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap2 = wx.StaticBitmap( self.m_panel24, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap2.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer33.Add( self.m_bitmap2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.m_panel24.SetSizer( bSizer33 )
		self.m_panel24.Layout()
		bSizer33.Fit( self.m_panel24 )
		bSizer34.Add( self.m_panel24, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_panel25 = wx.Panel( self.m_panel26, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel25.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )


		bSizer32.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText208 = wx.StaticText( self.m_panel25, wx.ID_ANY, u"Bandung - Indonesia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText208.Wrap( -1 )

		self.m_staticText208.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_staticText208.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_staticText208.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer32.Add( self.m_staticText208, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText209 = wx.StaticText( self.m_panel25, wx.ID_ANY, u"Email : careindonesiasolusi@gmail.com", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText209.Wrap( -1 )

		self.m_staticText209.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_staticText209.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer32.Add( self.m_staticText209, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText210 = wx.StaticText( self.m_panel25, wx.ID_ANY, u"Telp. 022 87241354", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText210.Wrap( -1 )

		self.m_staticText210.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_staticText210.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer32.Add( self.m_staticText210, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer32.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel25.SetSizer( bSizer32 )
		self.m_panel25.Layout()
		bSizer32.Fit( self.m_panel25 )
		bSizer34.Add( self.m_panel25, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText238 = wx.StaticText( self.m_panel26, wx.ID_ANY, u"versi : 23/01/2020", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText238.Wrap( -1 )

		bSizer34.Add( self.m_staticText238, 0, wx.ALL, 5 )


		self.m_panel26.SetSizer( bSizer34 )
		self.m_panel26.Layout()
		bSizer34.Fit( self.m_panel26 )
		bSizer31.Add( self.m_panel26, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer31 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class DatabasePeserta
###########################################################################

class DatabasePeserta ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		self.SetSizer( bSizer27 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class FrameGrafikTerpisah
###########################################################################

class FrameGrafikTerpisah ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Binakarir - Grafik", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel15.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.m_Grafik_Terpisah = wx.Panel( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_Grafik_Terpisah.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_Grafik_Terpisah.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer22.Add( self.m_Grafik_Terpisah, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_text_definisi = wx.TextCtrl( self.m_panel15, wx.ID_ANY, u"asdfasdf", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_text_definisi.Enable( False )
		self.m_text_definisi.Hide()
		self.m_text_definisi.SetMinSize( wx.Size( 200,200 ) )

		bSizer22.Add( self.m_text_definisi, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.ultimateList = ULC.UltimateListCtrl(self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,agwStyle = wx.LC_REPORT|ULC.ULC_HAS_VARIABLE_ROW_HEIGHT )
		self.ultimateList.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.ultimateList.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer22.Add( self.ultimateList, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel15.SetSizer( bSizer22 )
		self.m_panel15.Layout()
		bSizer22.Fit( self.m_panel15 )
		bSizer23.Add( self.m_panel15, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer23 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class LihatNilaiPeserta
###########################################################################

class LihatNilaiPeserta ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 494,499 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel25 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel25.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		fgSizer27 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer27.SetFlexibleDirection( wx.BOTH )
		fgSizer27.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button19 = wx.Button( self.m_panel25, wx.ID_ANY, u"Tutup", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer27.Add( self.m_button19, 0, wx.ALL, 5 )

		self.m_button18 = wx.Button( self.m_panel25, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer27.Add( self.m_button18, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel25.SetSizer( fgSizer27 )
		self.m_panel25.Layout()
		fgSizer27.Fit( self.m_panel25 )
		bSizer29.Add( self.m_panel25, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel21 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel30 = wx.Panel( self.m_panel21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel30.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		fgSizer28 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer28.SetFlexibleDirection( wx.BOTH )
		fgSizer28.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText218 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"No Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText218.Wrap( -1 )

		self.m_staticText218.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_staticText218.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer28.Add( self.m_staticText218, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_text_edit_no_tes = wx.TextCtrl( self.m_panel30, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer28.Add( self.m_text_edit_no_tes, 0, wx.ALL, 5 )

		self.m_staticText221 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )

		fgSizer28.Add( self.m_staticText221, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_datePicker_edit_tanggal_tes = wx.adv.DatePickerCtrl( self.m_panel30, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		fgSizer28.Add( self.m_datePicker_edit_tanggal_tes, 0, wx.ALL, 5 )

		self.m_staticText219 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Nama Kandidat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText219.Wrap( -1 )

		fgSizer28.Add( self.m_staticText219, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_text_edit_nama_kandidat = wx.TextCtrl( self.m_panel30, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer28.Add( self.m_text_edit_nama_kandidat, 0, wx.ALL, 5 )

		self.m_staticText224 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText224.Wrap( -1 )

		fgSizer28.Add( self.m_staticText224, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice_edit_jenis_kelaminChoices = [ u"Laki - Laki", u"Perempuan" ]
		self.m_choice_edit_jenis_kelamin = wx.Choice( self.m_panel30, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_edit_jenis_kelaminChoices, 0 )
		self.m_choice_edit_jenis_kelamin.SetSelection( 0 )
		fgSizer28.Add( self.m_choice_edit_jenis_kelamin, 0, wx.ALL, 5 )

		self.m_staticText222 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText222.Wrap( -1 )

		fgSizer28.Add( self.m_staticText222, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_datePicker_edit_tanggal_lahir = wx.adv.DatePickerCtrl( self.m_panel30, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		fgSizer28.Add( self.m_datePicker_edit_tanggal_lahir, 0, wx.ALL, 5 )

		self.m_staticText225 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Pendidikan Terakhir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText225.Wrap( -1 )

		fgSizer28.Add( self.m_staticText225, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice_edit_pendidikan_terakhirChoices = [ u"SD", u"SMP", u"SMA", u"D3", u"S1", u"S2", u"S3" ]
		self.m_choice_edit_pendidikan_terakhir = wx.Choice( self.m_panel30, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_edit_pendidikan_terakhirChoices, 0 )
		self.m_choice_edit_pendidikan_terakhir.SetSelection( 4 )
		fgSizer28.Add( self.m_choice_edit_pendidikan_terakhir, 0, wx.ALL, 5 )

		self.m_staticText220 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Jurusan Pendidikan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText220.Wrap( -1 )

		fgSizer28.Add( self.m_staticText220, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_text_edit_jurusan_pendidikan = wx.TextCtrl( self.m_panel30, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		fgSizer28.Add( self.m_text_edit_jurusan_pendidikan, 0, wx.ALL, 5 )

		self.m_staticText223 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText223.Wrap( -1 )

		fgSizer28.Add( self.m_staticText223, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_text_edit_kota = wx.TextCtrl( self.m_panel30, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer28.Add( self.m_text_edit_kota, 0, wx.ALL, 5 )

		self.m_staticText226 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Perusahaan / Instansi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText226.Wrap( -1 )

		fgSizer28.Add( self.m_staticText226, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_text_edit_perusahaan_instansi = wx.TextCtrl( self.m_panel30, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		fgSizer28.Add( self.m_text_edit_perusahaan_instansi, 0, wx.ALL, 5 )

		self.m_staticText227 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Posisi / Jabatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText227.Wrap( -1 )

		fgSizer28.Add( self.m_staticText227, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_text_edit_posisi_jabatan = wx.TextCtrl( self.m_panel30, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		fgSizer28.Add( self.m_text_edit_posisi_jabatan, 0, wx.ALL, 5 )


		self.m_panel30.SetSizer( fgSizer28 )
		self.m_panel30.Layout()
		fgSizer28.Fit( self.m_panel30 )
		bSizer30.Add( self.m_panel30, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel23 = wx.Panel( self.m_panel21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel23.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		bSizer30.Add( self.m_panel23, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel21.SetSizer( bSizer30 )
		self.m_panel21.Layout()
		bSizer30.Fit( self.m_panel21 )
		bSizer29.Add( self.m_panel21, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer29 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button19.Bind( wx.EVT_BUTTON, self.m_button_tutup_lihat_data )
		self.m_button18.Bind( wx.EVT_BUTTON, self.m_button_update_lihat_data )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button_tutup_lihat_data( self, event ):
		event.Skip()

	def m_button_update_lihat_data( self, event ):
		event.Skip()


###########################################################################
## Class DialogSimpan
###########################################################################

class DialogSimpan ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Binakarir", pos = wx.DefaultPosition, size = wx.Size( 245,137 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel27 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText211 = wx.StaticText( self.m_panel27, wx.ID_ANY, u"Data berhasil disimpan'", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )

		bSizer36.Add( self.m_staticText211, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel27.SetSizer( bSizer36 )
		self.m_panel27.Layout()
		bSizer36.Fit( self.m_panel27 )
		bSizer35.Add( self.m_panel27, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel28 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer37 = wx.BoxSizer( wx.VERTICAL )

		self.m_button20 = wx.Button( self.m_panel28, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.m_button20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel28.SetSizer( bSizer37 )
		self.m_panel28.Layout()
		bSizer37.Fit( self.m_panel28 )
		bSizer35.Add( self.m_panel28, 0, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer35 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button20.Bind( wx.EVT_BUTTON, self.m_button_dialog_simpan_berhasil )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button_dialog_simpan_berhasil( self, event ):
		event.Skip()


###########################################################################
## Class Biodata
###########################################################################

class Biodata ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Biodata", pos = wx.DefaultPosition, size = wx.Size( 494,479 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer39 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel31 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel31.SetBackgroundColour( wx.Colour( 77, 204, 187 ) )

		fgSizer11 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"No Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0|wx.TAB_TRAVERSAL )
		self.m_textCtrl1.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_textCtrl1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer11.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl205 = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer11.Add( self.m_textCtrl205, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Nama Kandidat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0|wx.TAB_TRAVERSAL )
		self.m_textCtrl3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer11.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText4.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl207 = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer11.Add( self.m_textCtrl207, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText5.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl206 = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer11.Add( self.m_textCtrl206, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Pendidikan Terakhir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText6.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl208 = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer11.Add( self.m_textCtrl208, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Jurusan Pendidikan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText7.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0|wx.TAB_TRAVERSAL )
		self.m_textCtrl7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer11.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText8.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0|wx.TAB_TRAVERSAL )
		self.m_textCtrl8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer11.Add( self.m_textCtrl8, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Perusahaan/Instansi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText9.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0|wx.TAB_TRAVERSAL )
		self.m_textCtrl9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer11.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Posisi / Jabatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer11.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0|wx.TAB_TRAVERSAL )
		self.m_textCtrl10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer11.Add( self.m_textCtrl10, 0, wx.ALL, 5 )


		self.m_panel31.SetSizer( fgSizer11 )
		self.m_panel31.Layout()
		fgSizer11.Fit( self.m_panel31 )
		bSizer39.Add( self.m_panel31, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.SetSizer( bSizer39 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl1.Bind( wx.EVT_TEXT, self.m_textCtrl1OnText )
		self.m_textCtrl3.Bind( wx.EVT_TEXT, self.m_textCtrl3OnText )
		self.m_textCtrl7.Bind( wx.EVT_TEXT, self.m_textCtrl7OnText )
		self.m_textCtrl8.Bind( wx.EVT_TEXT, self.m_textCtrl8OnText )
		self.m_textCtrl9.Bind( wx.EVT_TEXT, self.m_textCtrl9OnText )
		self.m_textCtrl10.Bind( wx.EVT_TEXT, self.m_textCtrl10OnText )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_textCtrl1OnText( self, event ):
		event.Skip()

	def m_textCtrl3OnText( self, event ):
		event.Skip()

	def m_textCtrl7OnText( self, event ):
		event.Skip()

	def m_textCtrl8OnText( self, event ):
		event.Skip()

	def m_textCtrl9OnText( self, event ):
		event.Skip()

	def m_textCtrl10OnText( self, event ):
		event.Skip()


###########################################################################
## Class DialogSavePDF
###########################################################################

class DialogSavePDF ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 396,173 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer40 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer31 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer31.SetFlexibleDirection( wx.BOTH )
		fgSizer31.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Direktori", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		fgSizer31.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_direktori_pdf = wx.DirPickerCtrl( self.m_panel1, wx.ID_ANY, u",90,90,-1,70,0", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		fgSizer31.Add( self.m_direktori_pdf, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Nama File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		fgSizer31.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_filepdf = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_filepdf.SetMaxLength( 0 )
		fgSizer31.Add( self.m_filepdf, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( fgSizer31 )
		self.m_panel1.Layout()
		fgSizer31.Fit( self.m_panel1 )
		bSizer40.Add( self.m_panel1, 1, wx.EXPAND|wx.ALL, 5 )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_simpanPDFFile = wx.Button( self.m_panel2, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_button_simpanPDFFile, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button_batal_simpanPDF = wx.Button( self.m_panel2, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_button_batal_simpanPDF, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel2.SetSizer( bSizer41 )
		self.m_panel2.Layout()
		bSizer41.Fit( self.m_panel2 )
		bSizer40.Add( self.m_panel2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer40 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


