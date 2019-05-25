'''
Created on May 13, 2019

@author: cireng
'''
import wx


class HurufBesar():
    def __init__(self,parent):
        
        self.parent = parent
        self.parent.m_textCtrl1.Bind( wx.EVT_TEXT, self.m_textCtrl1OnText )
        self.parent.m_textCtrl3.Bind( wx.EVT_TEXT, self.m_textCtrl3OnText )
        self.parent.m_textCtrl7.Bind( wx.EVT_TEXT, self.m_textCtrl7OnText )
        self.parent.m_textCtrl8.Bind( wx.EVT_TEXT, self.m_textCtrl8OnText )
        self.parent.m_textCtrl9.Bind( wx.EVT_TEXT, self.m_textCtrl9OnText )
        self.parent.m_textCtrl10.Bind( wx.EVT_TEXT, self.m_textCtrl10OnText )
        
    def m_textCtrl3OnText(self, event):
        self.selection = self.parent.m_textCtrl3.GetSelection()
        self.nama = self.parent.m_textCtrl3.GetValue().upper()
        self.parent.m_textCtrl3.ChangeValue(self.nama)
        self.parent.m_textCtrl3.SetSelection(*self.selection)
#         self.parent.m_textCtrl3.SetInsertionPointEnd()
    
    def m_textCtrl1OnText(self,event):
        self.selection = self.parent.m_textCtrl1.GetSelection()
        self.nomor_tes = self.parent.m_textCtrl1.GetValue().upper()
        self.parent.m_textCtrl1.ChangeValue(self.nomor_tes)
        self.parent.m_textCtrl1.SetSelection(*self.selection)
    
    def m_textCtrl7OnText(self,event):
        self.selection = self.parent.m_textCtrl7.GetSelection()
        self.jurusan_pendidikan = self.parent.m_textCtrl7.GetValue()
        self.parent.m_textCtrl7.ChangeValue(self.jurusan_pendidikan.upper())
        self.parent.m_textCtrl7.SetSelection(*self.selection)
    
    def m_textCtrl8OnText(self, event):
        self.selection = self.parent.m_textCtrl8.GetSelection()
        self.kota = self.parent.m_textCtrl8.GetValue()
        self.parent.m_textCtrl8.ChangeValue(self.kota.upper())
        self.parent.m_textCtrl8.SetSelection(*self.selection)        
        pass
    
    def m_textCtrl9OnText(self, event):
        self.selection = self.parent.m_textCtrl9.GetSelection()
        self.perusahaan_instansi = self.parent.m_textCtrl9.GetValue()
        self.parent.m_textCtrl9.ChangeValue(self.perusahaan_instansi.upper())
        self.parent.m_textCtrl9.SetSelection(*self.selection)
        pass
    
    def m_textCtrl10OnText(self, event):
        self.selection = self.parent.m_textCtrl10.GetSelection()
        self.posisi_jabatan = self.parent.m_textCtrl10.GetValue()
        self.parent.m_textCtrl10.ChangeValue(self.posisi_jabatan.upper())
        self.parent.m_textCtrl10.SetSelection(*self.selection)        
        
        pass