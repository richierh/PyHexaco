"""Subclass of MyFrame1, which is generated by wxFormBuilder."""

import wx
import hexaco.views.maingui as maingui
import pathlib


# Implementing MyFrame1
class Hexacofile(maingui.FrameDepan):

	def __init__(self, parent):
		super(Hexacofile, self).__init__(parent)
		self.SetTitle("Aplikasi Binakarir - Hexaco")
		pathimage = pathlib.Path.cwd() / "resources/images/binadata.png"
		self.image = wx.Image(str(pathimage))
		self.m_bitmap1.SetBitmap(wx.Bitmap(self.image))

		pathimage = pathlib.Path.cwd() / "resources/images/binakarir.png"
		self.image = wx.Image(str(pathimage))
		self.m_bitmap2.SetBitmap(wx.Bitmap(self.image))
		
		self.Maximize(maximize=True)
		self.m_simplebook1.SetSelection(0)

	def m_button1OnButtonClick(self, event):
		self.m_simplebook1.SetSelection(0)
		self.m_button2.Disable()		
		self.m_button3.Enable()
		
		print ("tes")
		
	def m_button2OnButtonClick(self, event):
		self.getSel = self.m_simplebook1.GetSelection()
		print (self.getSel)
		if self.getSel == 3 :
			self.m_simplebook1.SetSelection(1)
			self.m_button3.Disable()
			print ("dari 60")
		
		elif self.getSel == 2 :
			self.m_simplebook1.SetSelection(1)
			self.m_button3.Disable()
			print ("dari 24")
			
		
		else :
			self.m_simplebook1.SetSelection(self.getSel - 1)

			if self.getSel-2 == 2:
				self.m_button3.Disable()
			elif self.getSel-1 == 0:
				self.m_button2.Disable()		
				self.m_button3.Enable()	
			else :
				self.m_button3.Enable()
				pass
			print ("tes 2")
		
	def m_button3OnButtonClick(self, event):
		self.getSel = self.m_simplebook1.GetSelection()
		self.m_simplebook1.SetSelection(self.getSel + 1)
		if self.getSel+2 == 2:
			self.m_button2.Enable()		
			self.m_button3.Disable()
		else :
			self.m_button3.Enable()
		print ("tes 3")
		
	def m_textCtrl3OnText(self, event):
		self.nama = self.m_textCtrl3.GetValue()
		self.m_textCtrl3.SetValue(self.nama.upper())
		self.m_textCtrl3.SetInsertionPointEnd()
		
	def m_radioBtn1OnRadioButtonSoal24(self, event):
		print ("radio buttton 24")
		self.m_simplebook1.SetSelection(2)
		self.m_panel24.Enable()
		self.m_panel60.Disable()
		self.m_button3.Enable()
		#self.m_panel100.Hide()
		self.Update()
		self.Refresh()
		self.Layout()
	
	def m_radioBtn2OnRadioButtonSoal60(self, event):
		print ("radio button 60")
		self.m_simplebook1.SetSelection(3)
		self.m_panel24.Disable()
		self.m_panel60.Enable()
		self.m_button3.Enable()
		#self.m_panel100.Hide()
		self.Update()
		self.Refresh()
		self.Layout()
		
	def m_radioBtn3OnRadioButtonSoal100(self, event):
		print ("radio button 100")
		self.m_panel24.Hide()
		self.m_panel60.Hide()
		self.m_button3.Enable()
		#self.m_panel100.Show()
		self.Update()
		self.Refresh()
		self.Layout()
	
	def m_button4OnButtonClick24(self,event):
		self.m_radioBtn1OnRadioButtonSoal24(self)
		print ("tes soal item 24")
		
	
	def m_button5OnButtonClick60(self,event):
		self.m_radioBtn2OnRadioButtonSoal60(self)
		print ("tes soal item 60")

	
	def m_button6OnButtonClick100(self,event):
		self.m_radioBtn3OnRadioButtonSoal100(self)
		print ("tes soal item 100")
		
	def m_button7OnButtonClick(self,event):
		print ("hhjk")
