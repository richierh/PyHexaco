from coreapps.views import maingui
import wx
import wx.lib.mixins.listctrl  as  listmix
from datetime import datetime

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
        
        print (self.parent.rincian_input_data_peserta)
        
        self.SetTitle("Lihat Nilai Peserta")
        self.m_listCtrl2.InsertColumn(0,"No",width=50,format = wx.LIST_FORMAT_CENTER)
        self.m_listCtrl2.InsertColumn(1,"Jawaban Peserta",width=105,format = wx.LIST_FORMAT_CENTER)

        print ("hello , {} ".format(self.parent.rincian_input_data_peserta))

#         Memasukkan nilai dari list ke edit data
        self.no_tes = str(self.parent.rincian_data_peserta[0][2])
        self.m_text_edit_no_tes.SetValue(self.no_tes.upper())
   
        self.tanggal_tes = datetime.strptime(self.parent.rincian_data_peserta[0][3],"%Y/%m/%d")
        self.m_datePicker_edit_tanggal_tes.SetValue(self.tanggal_tes)
        
        self.nama_kandidat = str(self.parent.rincian_data_peserta[0][4])
        self.m_text_edit_nama_kandidat.SetValue(self.nama_kandidat)
 
        self.jenis_kelamin = str(self.parent.rincian_data_peserta[0][5])
        if self.jenis_kelamin == "Laki - Laki":
            self.jenis_kelamin_item = 0
        elif self.jenis_kelamin == "Perempuan":
            self.jenis_kelamin_item = 1
        self.m_choice_edit_jenis_kelamin.SetSelection(self.jenis_kelamin_item)

        self.tanggal_lahir = datetime.strptime(self.parent.rincian_data_peserta[0][6],"%Y/%m/%d")
        self.m_datePicker_edit_tanggal_lahir.SetValue(self.tanggal_lahir)

        self.pendidikan_terakhir = str(self.parent.rincian_data_peserta[0][7])
        if self.pendidikan_terakhir == "SD":
            self.pendidikan_terakhir_item = 0
        elif self.pendidikan_terakhir == "SMP":
            self.pendidikan_terakhir_item = 1
        elif self.pendidikan_terakhir == "SMA":
            self.pendidikan_terakhir_item = 2
        elif self.pendidikan_terakhir == "D3":
            self.pendidikan_terakhir_item = 3
        elif self.pendidikan_terakhir == "S1":
            self.pendidikan_terakhir_item = 4
        elif self.pendidikan_terakhir == "S2":
            self.pendidikan_terakhir_item = 5
        elif self.pendidikan_terakhir == "S3":
            self.pendidikan_terakhir_item = 6

        self.m_choice_edit_pendidikan_terakhir.SetSelection(self.pendidikan_terakhir_item),

        self.jurusan_pendidikan = str(self.parent.rincian_data_peserta[0][8])
        self.m_text_edit_jurusan_pendidikan.SetValue(self.jurusan_pendidikan.upper())

        self.kota = str(self.parent.rincian_data_peserta[0][9])
        self.m_text_edit_kota.SetValue(self.kota.upper())
        self.perusahaan_instansi = str(self.parent.rincian_data_peserta[0][10])

        self.m_text_edit_perusahaan_instansi.SetValue(self.perusahaan_instansi.upper())
        self.posisi_jabatan = str(self.parent.rincian_data_peserta[0][11])

        self.m_text_edit_posisi_jabatan.SetValue(self.posisi_jabatan.upper())
        
        
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
       
        self.m_panel23.SetSizer(sizer44)
        # print("hei")
        
#         Event Handler
        self.m_button19.Bind( wx.EVT_BUTTON, self.m_button_tutup_lihat_data )
        self.m_button18.Bind( wx.EVT_BUTTON, self.m_button_update_lihat_data )
        pass
        
    def m_button_tutup_lihat_data(self, event):
        print ("tutup aplikasi lihat data")
        self.Close()
        pass
    
    def m_button_update_lihat_data(self, event):
        from coreapps.models.query import update_jawaban,update_rincian_data_peserta
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

        # print(self.m_text_edit_no_tes)
#       Updating Rincian Data Peserta 
        rinc_data= [self.m_text_edit_no_tes.GetValue().upper(), 
        self.m_datePicker_edit_tanggal_tes.GetValue().Format("%Y/%m/%d"),
        self.m_text_edit_nama_kandidat.GetValue().upper(),
        self.m_choice_edit_jenis_kelamin.GetString(self.m_choice_edit_jenis_kelamin.GetSelection()),
        self.m_datePicker_edit_tanggal_lahir.GetValue().Format("%Y/%m/%d"),
        self.m_choice_edit_pendidikan_terakhir.GetString(self.m_choice_edit_pendidikan_terakhir.GetSelection()),
        self.m_text_edit_jurusan_pendidikan.GetValue().upper(),
        self.m_text_edit_kota.GetValue().upper(),
        self.m_text_edit_perusahaan_instansi.GetValue().upper(),
        self.m_text_edit_posisi_jabatan.GetValue().upper(),
        ]
        # self.m_text_edit_

        # print(rinc_data)

        # ]
        self.update_data = update_rincian_data_peserta(rinc_data,self.id_peserta)

        self.parent.m_listCtrl_tabel_database.DeleteAllItems()

        pass

if __name__=="__main__":
    root =wx.App()
    runapp = TurunanLihatData(None)
    runapp.Show()
    root.MainLoop()