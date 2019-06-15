'''
Created on May 12, 2019

@author: cireng
'''
import  wx
from coreapps.views.buka_filter_db import FrameFilterDatabase
from coreapps.models.query import query_tabel_data_peserta
from coreapps.controllers.ev_database import DataListCtrl

class BukaFilter(FrameFilterDatabase):
    
    def __init__(self,parent):
        super(BukaFilter,self).__init__(parent)
        self.parent = parent
        self.SetSize((450,550))
        self.m_panel20.SetBackgroundColour(wx.Colour(77, 204, 187))
        self.m_staticText206.SetForegroundColour(wx.Colour(255, 255, 255))
        self.m_staticText207.SetForegroundColour(wx.Colour(255, 255, 255))
        self.m_staticText208.SetForegroundColour(wx.Colour(255, 255, 255))
        self.m_staticText209.SetForegroundColour(wx.Colour(255, 255, 255))
        self.m_staticText210.SetForegroundColour(wx.Colour(255, 255, 255))
        self.m_staticText211.SetForegroundColour(wx.Colour(255, 255, 255))

        
        print ("lewat sini nggak")
        
    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def m_buttonKlikFilterTanggalOnButtonClick( self, event ):
        print ("bekerja")
        self.datedari = self.m_datePickerdaritgl.GetValue().Format("%Y/%m/%d")
        self.datesampai = self.m_datePickersampaitgl.GetValue().Format("%Y/%m/%d")
        print (self.datedari)
        print (self.datesampai) 
        
        self.values =[None,None,self.datedari,self.datesampai,"tanggal"]
        self.query_tabel = query_tabel_data_peserta(self.values)
        print (self.query_tabel)
        self.tampilkan = DataListCtrl(self)
        self.tampilkan.tampil_kelistctrl()
        
        event.Skip()

    def m_buttonKlikFilterOrangOnButtonClick( self, event ):
        print ("Bekerja")
        self.nama_orang = self.m_textCtrlnamaorang.GetValue()
        print (self.nama_orang)
        self.values =[self.nama_orang.upper(),"","","","nama orang"]
        self.query_tabel = query_tabel_data_peserta(self.values)
        print (self.query_tabel)
        self.tampilkan = DataListCtrl(self)
        self.tampilkan.tampil_kelistctrl()

        event.Skip()

    def m_buttonKlikFilterNoTesOnButtonClick( self, event ):
        print ("Bekerja")
        self.nomor_tes = self.m_textCtrlnomortes.GetValue()
        print (self.nomor_tes)

        self.values =[None,self.nomor_tes.upper(),"","","no tes"]
        self.query_tabel = query_tabel_data_peserta(self.values)
        print (self.query_tabel)
        self.tampilkan = DataListCtrl(self)
        self.tampilkan.tampil_kelistctrl()
        
        
        event.Skip()

    def m_buttonFilterBatalOnButtonClick( self, event ):
        print ("Bekerja")
        self.Close(force=False)
        event.Skip()
        
if __name__=="__main__":
    root = wx.App()
    run  = BukaFilter(None)
    run.Show()
    root.MainLoop()        
        
        
        
        
        