#! usr/bin/env python


import wx
from coreapps.controllers.hitung_data import HitungData, HitungDataDatabase
from coreapps.models.query import query_kamus

'''
Created on May 12, 2019

@author: cireng
'''

class HalamanEventControl():
    
    def __init__(self,parent):
        self.parent = parent
        self.parent.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
        self.parent.m_button2.Bind( wx.EVT_BUTTON, self.m_button2OnButtonClick )
        self.parent.m_button3.Bind( wx.EVT_BUTTON, self.m_button3OnButtonClick )

    def m_button1OnButtonClick(self,event):
        print ("click here 'ke awal'")
        self.parent.m_simplebook1.SetSelection(0)
        self.parent.m_button2.Disable()        
        self.parent.m_button3.Enable()
        self.parent.m_button1.Disable()
        
    def m_button2OnButtonClick(self,event):
        self.getSel = self.parent.m_simplebook1.GetSelection()
        print (self.getSel)
        
        self.parent.m_simplebook1.SetSelection(self.getSel - 1)
        self.getSel = self.parent.m_simplebook1.GetSelection()
        print (self.getSel)
        
        if self.getSel == 1:
            self.parent.m_button3.Disable()
            
        elif self.getSel == 0:
            self.parent.m_button1.Disable()
            self.parent.m_button2.Disable()        
            self.parent.m_button3.Enable()    
            
        else :
            self.parent.m_button3.Enable()
            pass
        print ("click here 'Sebelumnya'")


    def m_button3OnButtonClick(self, event):

#         try:
            self.getSel = self.parent.m_simplebook1.GetSelection()
#             print (self.getSel)
            self.parent.m_simplebook1.SetSelection(self.getSel + 1)
            self.getSel = self.parent.m_simplebook1.GetSelection()
#             print (self.getSel)
            self.parent.m_button1.Enable()
            if self.getSel == 1:
                self.parent.m_button2.Enable()        
                self.parent.m_button3.Disable()
            elif self.getSel == 3 :
                self.parent.no_database = 0
                self.data_induk = AmbilData(self.parent)
                self.data_induk.save()
#                 self.data_induk.data_induk()
                print ("masuk ke halaman {}".format(self.getSel))
                'Proses hitung dimulai ketika halaman 3 , atau pada saat penyajian grafik'
            elif self.getSel == 4 :
                self.parent.m_button3.Disable()  #         print(self.text_entry.get_input_versi24())
            else :
                self.parent.m_button3.Enable()
            self.parent.m_notebook2.SetSelection(1)                                                                      

#         except :
#             self.parent.m_button3.Disable()  #         print(self.text_entry.get_input_versi24())
#         print(self.text_entry.get_input_versi60())
#         print(self.text_entry.get_input_versi100())
    

class AmbilData():
    
    
    def __init__(self,parent):
        self.parent = parent
#         from coreapps.views.grafikmatplotlib import GrafikDimensi
        from coreapps.controllers.grafik_matplotlib import GrafikDimensi
        
        
        if self.parent.no_database == 1 :
            print ("lewasjjjss")
            self.hasil_subdimensi = self.parent.x
            self.hasil_dimensi = self.parent.y
            pass
        
        else :
            self.hasil_subdimensi,self.hasil_dimensi = self.data_induk()
#         print ("cek")
#         print (self.hasil_dimensi)
#         print (self.hasil_dimensi["Honesty & Humility"])
#         print (self.hasil_subdimensi["Honesty & Humility"])
        self.parent.grafik_matplotlib=GrafikDimensi(self.parent)
        self.parent.grafik_matplotlib.draw(self.hasil_dimensi,self.hasil_subdimensi,self.parent.versi_soal)
        self.parent.GrafikMatplotlib.SetSizer(self.parent.grafik_matplotlib.sizer90)
        self.parent.GrafikMatplotlib.Update()
        self.parent.GrafikMatplotlib.Refresh()
        self.parent.GrafikMatplotlib.Layout()
    
    def save(self):
        return self.parent.grafik_matplotlib.save_figure()
    
    def data_induk(self):
        self.a = HitungData(self.parent)
        hasil_dimensi,hasil_subdimensi = self.a.hitung()
        return hasil_dimensi,hasil_subdimensi
        
    
    def data_database(self):
        self.a = HitungData(self.parent)
        hasil_dimensi,hasil_subdimensi = self.a.hitung()
        return hasil_dimensi,hasil_subdimensi
        
    
    def get_data_from_input(self):
        return self.data_induk()

# class DataTarik():
#     
#     
#     def __init__(self,parent):
#         self.parent = parent
# #         from coreapps.views.grafikmatplotlib import GrafikDimensi
#         from coreapps.controllers.grafik_matplotlib import GrafikDimensi
#         
#         self.hasil_subdimensi,self.hasil_dimensi = self.data_induk()
# #         print ("cek")
# #         print (self.hasil_dimensi)
# #         print (self.hasil_dimensi["Honesty & Humility"])
# #         print (self.hasil_subdimensi["Honesty & Humility"])
#         self.parent.grafik_matplotlib=GrafikDimensi(self.parent)
#         self.parent.grafik_matplotlib.draw(self.hasil_dimensi,self.hasil_subdimensi,self.parent.versi_soal)
#         self.parent.GrafikMatplotlib.SetSizer(self.parent.grafik_matplotlib.sizer90)
#         self.parent.GrafikMatplotlib.Update()
#         self.parent.GrafikMatplotlib.Refresh()
#         self.parent.GrafikMatplotlib.Layout()
#     
#     def data_induk(self):
#         self.a = HitungDataDatabase(self.parent)
#         hasil_dimensi,hasil_subdimensi = self.a.hitung()
#         return hasil_dimensi,hasil_subdimensi
#         pass
#     
#     def get_data_from_input(self):
#         return self.data_induk()


class KamusControl():
    
    
    def __init__(self,parent):
        self.parent = parent
        self.parent.m_listbox_kamus_hexaco.Bind( wx.EVT_LISTBOX, self.m_listbox_kamus_hexacoOnListBox )
        
    def m_listbox_kamus_hexacoOnListBox(self,event):
        print ("hello")
        print (event.GetString())
        string_value= self.__definision(event.GetString())
        self.parent.m_textCtrl_kamus_hexaco.SetValue("")
        self.parent.m_textCtrl_kamus_hexaco.write(string_value)
        pass
    
    def __definision(self,stringtxtctrl):
        
        self.query = query_kamus(stringtxtctrl)
        return self.query[2]


        
    
    
    
    