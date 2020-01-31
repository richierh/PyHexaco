#! usr/bin/env/python

import wx
# from coreapps.models.query import query_tabel_data_peserta
from coreapps.models.query import query_input_peserta,query_tabel_data_peserta



class DataListCtrl():
    
    
    def __init__(self,parent):
        self.parent=parent
        self.parent2 = parent.parent
    def tampil_kelistctrl(self):
        line = 1
        self.index =0
        self.parent2.m_listCtrl_tabel_database.DeleteAllItems()
        # print(self.parent.query_tabel)
        self.jml_nomor = len(self.parent.query_tabel)
        for data in self.parent.query_tabel:
            self.parent2.m_listCtrl_tabel_database.InsertItem(self.index,line)
            self.parent2.m_listCtrl_tabel_database.SetItem(self.index,0,str(self.jml_nomor))
            self.parent2.m_listCtrl_tabel_database.SetItem(self.index,1,str(data[0]))
            self.parent2.m_listCtrl_tabel_database.SetItem(self.index,2,str(data[1]))
            self.parent2.m_listCtrl_tabel_database.SetItem(self.index,3,str(data[2]))
            self.parent2.m_listCtrl_tabel_database.SetItem(self.index,4,str(data[3]))
            self.parent2.m_listCtrl_tabel_database.SetItem(self.index,5,str(data[4]))
            self.parent2.m_listCtrl_tabel_database.SetItem(self.index,6,str(data[5]))
            self.parent2.m_listCtrl_tabel_database.SetItem(self.index,7,str(data[6]))           
            self.parent2.m_listCtrl_tabel_database.SetItem(self.index,8,str(data[7]))
            self.parent2.m_listCtrl_tabel_database.SetItem(self.index,9,str(data[8]))
            self.parent2.m_listCtrl_tabel_database.SetItem(self.index,10,str(data[9]))
            self.parent2.m_listCtrl_tabel_database.SetItem(self.index,11,str(data[10]))
            self.parent2.m_listCtrl_tabel_database.SetItem(self.index,12,str(data[11]))
            self.jml_nomor-=1

class DatabaseEventControl():

    
    def __init__(self,parent):
        self.parent = parent
        
        self.parent.m_listCtrl_tabel_database.Bind( wx.EVT_LEFT_DCLICK, self.m_listCtrl_tabel_databaseOnLeftDClick )
        self.parent.m_listCtrl_tabel_database.Bind( wx.EVT_LIST_COL_BEGIN_DRAG, self.m_listCtrl_tabel_databaseOnListColBeginDrag )
        self.parent.m_listCtrl_tabel_database.Bind( wx.EVT_LIST_ITEM_RIGHT_CLICK, self.m_listCtrl_tabel_databaseOnListItemRightClick )
        self.parent.m_listCtrl_tabel_database.Bind( wx.EVT_LIST_ITEM_SELECTED, self.m_listCtrl_tabel_databaseOnListItemSelected )

#         print (self.parent.listcolumn)
        print ("apakah ini")
        pass
    
 
    
    
    def __hitung(self):
        pass
 
    def m_listCtrl_tabel_databaseOnLeftDClick(self, event):
        from coreapps.views.lihat_data_nilai import TurunanLihatData
        self.item = self.parent.m_listCtrl_tabel_database.GetFocusedItem()
        self.parent.get_item_id_name = self.parent.m_listCtrl_tabel_database.GetItemText(self.item,col=1)
        self.parent.get_item_no_tes = self.parent.m_listCtrl_tabel_database.GetItemText(self.item,col=5)
#         print (self.get_item_id_name)
#         print (self.get_item_no_tes)
        
         
#         self.values =[self.get_item_id_name.upper(),"","","","idpeserta"]
#         self.parent.query_tabel = query_tabel_data_peserta(self.values)
#         print (self.parent.query_tabel)
#         for data in self.parent.query_tabel[0]:
#             print (data)
        
        print ("akhi")
#         self.parent.rinc_data = 
        self.rinci_list = ["idpeserta",self.parent.get_item_id_name.upper()]
        self.parent.rincian_input_data_peserta = query_input_peserta(self.rinci_list)
        self.parent.rincian_data_peserta = query_tabel_data_peserta([self.parent.get_item_id_name.upper(),"","","","idpeserta"])
        
        print (self.parent.rincian_input_data_peserta)
        print (self.parent.rincian_data_peserta[0][2])
         
        self.windows_lihat_nilai = TurunanLihatData(self.parent)
        self.windows_lihat_nilai.Maximize()
        self.windows_lihat_nilai.Show()

        pass
    
    def m_listCtrl_tabel_databaseOnListColBeginDrag(self, event):
        print ("list ctrl reaction when col begin drat")
        
        pass
    
    def m_listCtrl_tabel_databaseOnListItemRightClick(self, event):
        print ("list ctrl on list item rightclick")
        pass
    
    
    def m_listCtrl_tabel_databaseOnListItemSelected(self, event):
        print ("list ctrl on list item selected")
        pass
