from coreapps.views import maingui
import wx
import wx.lib.mixins.listctrl  as  listmix


class EditableListCtrl(wx.ListCtrl, listmix.TextEditMixin):
    ''' TextEditMixin allows any column to be edited. '''
 
    #----------------------------------------------------------------------
    def __init__(self, parent, ID=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        """Constructor"""
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.TextEditMixin.__init__(self)
 


class TurunanLihatData(maingui.LihatNilaiPeserta,listmix.TextEditMixin):
    
    def __init__(self,parent,*args):
        super(TurunanLihatData,self).__init__(parent,*args)
        self.parent = parent
        self.parent2 = args
        print (self.parent)

        sizer44 = wx.BoxSizer(wx.VERTICAL)
        self.m_listCtrl2 = EditableListCtrl(self.m_panel23, style=wx.LC_REPORT)
#         self.m_listCtrl2=wx.ListCtrl( self.m_scrolledWindow6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,wx.LC_EDIT_LABELS| wx.LC_REPORT )
        sizer44.Add(self.m_listCtrl2,1,wx.EXPAND|wx.ALL,5)
        
        self.SetTitle("Lihat Nilai Peserta")
        self.m_listCtrl2.InsertColumn(0,"No",width=50,format = wx.LIST_FORMAT_CENTER)
        self.m_listCtrl2.InsertColumn(1,"Jawaban Peserta",width=105,format = wx.LIST_FORMAT_CENTER)

        print ("hello , {} ".format(self.parent.rincian_input_data_peserta))
        
        
        
        rows=[]
        for data in self.parent.rincian_input_data_peserta:
            print (data)
            rows.append((data[3],data[4]))
        
        
        
        
        
#         rows =[(1,4),
#                (2,1)
#             ]
        index = 0
        for row in rows :
            self.m_listCtrl2.InsertItem(index,str(row[0]))
            self.m_listCtrl2.SetItem(index,1,str(row[1]))
            index+=1
       

        
        
        
        self.m_scrolledWindow6.SetSizer(sizer44)
        print("hei")
        
        
        
#         Event Handler
        self.m_button19.Bind( wx.EVT_BUTTON, self.m_button_tutup_lihat_data )
        self.m_button18.Bind( wx.EVT_BUTTON, self.m_button_update_lihat_data )
        pass
        
    def m_button_tutup_lihat_data(self, event):
        print ("tutup aplikasi lihat data")
        self.Close()
        pass
    
    def m_button_update_lihat_data(self, event):
        from coreapps.models.query import update_jawaban
        print (self.m_listCtrl2.GetItemText(0, col=1))
        self.id_peserta = self.parent.get_item_id_name.upper()
        data_update = []
        for data in range(self.m_listCtrl2.GetItemCount()):
            print (data)
            self.no = self.m_listCtrl2.GetItemText(data, col=0)
            self.jawaban = self.m_listCtrl2.GetItemText(data, col=1)
            data_update.append(("",self.no,self.jawaban))

        
        for i in data_update:
            
            print (i)
            self.update_database= update_jawaban(i,self.id_peserta)
        
        for index in range(0,2):
            self.get_item = self.m_listCtrl2.GetItemText(index,col=1)
            print (self.get_item)
        print (self.parent.get_item_id_name.upper())

        pass

if __name__=="__main__":
    root =wx.App()
    runapp = TurunanLihatData(None)
    runapp.Show()
    root.MainLoop()