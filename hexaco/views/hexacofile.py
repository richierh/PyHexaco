"""Subclass of MyFrame1, which is generated by wxFormBuilder."""

import wx
import views.maingui as maingui
import pathlib

# Implementing MyFrame1
class Hexacofile( maingui.FrameDepan ):
	def __init__( self, parent ):
		super(Hexacofile,self).__init__(parent)
		self.SetTitle("Aplikasi Binakarir - Hexaco")
		pathimage = pathlib.Path.cwd()/"resources/images/binadata.png"
		self.image = wx.Image(str(pathimage))
		self.m_bitmap1.SetBitmap(wx.Bitmap(self.image))
		
		self.Maximize(maximize=True)
		self.m_simplebook1.SetSelection(0)


	def m_button1OnButtonClick(self, event):
		self.m_simplebook1.SetSelection(0)
		
		print ("tes")
		
	def m_button2OnButtonClick(self, event):
		self.getSel = self.m_simplebook1.GetSelection()
		self.m_simplebook1.SetSelection(self.getSel-1)
		print ("tes 2")
		
	def m_button3OnButtonClick(self, event):
		self.getSel = self.m_simplebook1.GetSelection()
		self.m_simplebook1.SetSelection(self.getSel+1)
		print ("tes 3")
		
	def m_textCtrl3OnText(self, event):
		self.nama = self.m_textCtrl3.GetValue()
		self.m_textCtrl3.SetValue(self.nama.upper())
		self.m_textCtrl3.SetInsertionPointEnd()
		
	def m_radioBtn1OnRadioButtonSoal24(self, event):
		print ("radio buttton 24")
		self.m_panel7.Show()
		self.m_panel8.Hide()
		self.m_panel9.Hide()
		self.Update()
		self.Refresh()
		self.Layout()
	
	def m_radioBtn2OnRadioButtonSoal60(self, event):
		print ("radio button 60")
		self.m_panel7.Hide()
		self.m_panel8.Show()
		self.m_panel9.Hide()
		self.Update()
		self.Refresh()
		self.Layout()
	
		
	def m_radioBtn3OnRadioButtonSoal100(self, event):
		print ("radio button 100")
		self.m_panel7.Hide()
		self.m_panel8.Hide()
		self.m_panel9.Show()
		self.Update()
		self.Refresh()
		self.Layout()
	

if __name__=="__main__":
	root = wx.App()
	openwindows = Hexacofile(None)
	openwindows.Show()
	root.MainLoop()