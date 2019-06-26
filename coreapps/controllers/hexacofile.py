"""Subclass of MyFrame1, which is generated by wxFormBuilder."""

import pathlib
import wx
from coreapps.views.control_text import ControlEntry
from coreapps.controllers.grafik_matplotlib import GrafikEm, GrafikEx,\
        GrafikIA,GrafikA,GrafikC,GrafikO,GrafikH
from coreapps.views.maingui import FrameDepan
from coreapps.views.biodata import Biodata
from coreapps.views.menubar_tentang import TentangAplikasi
from coreapps.views.DataPeserta import DataPesertaHexaco
from coreapps.controllers.ev_halaman import HalamanEventControl, AmbilData
from coreapps.controllers.ev_database import DatabaseEventControl
from coreapps.controllers.ev_filter_db import BukaFilter
# from coreapps.views.huruf_besar import HurufBesar
from coreapps.controllers.ev_halaman import KamusControl
from coreapps.views.dialog_simpan import TurunanDialogSimpan
from coreapps.controllers.hitung_data import HitungData
from coreapps.controllers.tarik_data import TarikData
from coreapps.controllers.hexaco_calculation import DimensiHexaco
from coreapps.models.query import insert_data_peserta, query_input_peserta,\
    query_tabel_data_peserta


'Implementing MyFrame1'
class Hexacofile(FrameDepan):
    

    def __init__(self, parent):
        super(Hexacofile, self).__init__(parent)
#         self.huruf_besar = HurufBesar(self)
        
        'Properties Windows Utama'
    
        self.SetTitle("Aplikasi Binakarir - Hexaco")
        self.m_button1.Disable()
        pathimage = pathlib.Path.cwd() / "resources/images/binadata.png"
        self.image1 = wx.Image(str(pathimage))
        self.re_image1 = self.image1.Rescale(450,300)
        self.m_bitmap1.SetBitmap(wx.Bitmap(self.re_image1))
        self.text_entry = ControlEntry(self)
        self.Maximize(maximize=True)
        self.m_simplebook1.SetSelection(0)

        
        '''separate event into another file for simplicity
        memindahkan event di file yang lain agar lebih sederhana'''
        self.control_halaman = HalamanEventControl(self)
        self.database_peserta = DataPesertaHexaco(self.m_listCtrl_tabel_database)
        self.control_database = DatabaseEventControl(self)
        self.listbox_control = KamusControl(self)
        self.control_t = ControlEntry(self)
        


        '''Base Frame get Updated Frame Utama di Update'''
        self.Update()
        self.Refresh()
        self.Layout()
  
    def m_button_save_as_pdfOnButtonClick(self, event):
        from coreapps.controllers.definisi import rerata2
        print ("tes over here 'em'")
        if self.no_database == 1 :
            self.hasil_subdimensi = self.x
            self.hasil_dimensi = self.y
            print (self.rincian_data_peserta)
            self.bio_data = []
            for bio  in self.rincian_data_peserta[0]:
                if self.rincian_data_peserta[0].index(bio) <= 1:
                    pass
                else :
                    self.bio_data.append(bio)
            print (self.bio_data)
            if self.rincian_data_peserta[0][5] == "Laki - Laki":
                print ("laki - laki ini")
                self.m_choice1.SetSelection(0)
            else :
                print ("perempuan ini")
                self.m_choice1.SetSelection(1)        
        elif self.no_database == 0 :     
            self.bio_data = ControlEntry(self)
            print (self.bio_data.get_input_biodata())
            print ("tess ajaj")
            self.bio_data=self.bio_data.get_input_biodata()

            self.hitung = HitungData(self)
            self.hasil_subdimensi,self.hasil_dimensi = self.hitung.hitung()
        # print (self.hasil_dimensi)
        # print (self.hasil_subdimensi)

        select = self.m_choice1.GetSelection()
        self.jenis_kelamin = self.m_choice1.GetString(select)

        for k,v in self.hasil_dimensi.items():
            self.hasil_subdimensi[k]=round(v,2)
#         print ("Nilai Total dimensi + sub dimensi {} {}".format(nilai_dimensi,nilai_sub_dimensi))
#         print (self.jenis_kelamin)
        self.definisi = rerata2(self.jenis_kelamin,self.hasil_subdimensi)
        # print ([*self.hasil_subdimensi])
        # print (self.definisi)
        dimensi = [*self.hasil_subdimensi]
        self.definisi.insert(20,self.definisi[30])
        self.definisi.insert(16,self.definisi[30])
        self.definisi.insert(12,self.definisi[30])
        self.definisi.insert(8,self.definisi[30])
        self.definisi.insert(4,self.definisi[30])
        self.definisi.insert(0,self.definisi[30])

        for i in range(0,6):
            del self.definisi[-1]
        self.data = []
        for k in self.definisi:
            for dim in dimensi:
                if k[0] == dim:
                    self.data.append([k[0],self.hasil_subdimensi[dim],k[1],k[2]])
#         print ("data ini {}".format(self.data))


       # print (self.data)
        for i in self.data:
            # print (i)
            pass
        print ("stop disini")

        from coreapps.controllers.reporting.report import pdf_data

        self.pdf = pdf_data(self.bio_data,self.data)










#         dlg = wx.FileDialog(self, "Save to file:", ".", "", "File Pdf (*.pdf)|*.pdf", wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
#         if dlg.ShowModal() == wx.ID_OK:
#             i = dlg.GetFilterIndex()
#             if i == 0: # Text format
#                 try:
#                     f = open(dlg.GetPath(), "w")
#                     f.write("# Date, From, SerivceCenter, Message\n")
#                     for i in self.itemDataMap.keys():
#                         entry = self.itemDataMap[i]
#                         f.write('%s,%s,%s,%s\n' % (entry[1], entry[2], entry[4].smsc, entry[3]))
#                     f.close()
# #                     wx.pySIMmessage(self, "SMS export to file was successful\n\nFilename: %s" % dlg.GetPath(), "Export OK")
#                 except:
# #                     pySIMmessage(self, "Unable to save your SMS messages to file: %s" % dlg.GetPath(), "Export error")
#                     #print_exc()
#                     pass
#             dlg.Destroy() 
  
#     def m_button_save_as_pdfOnButtonClick(self, event):
#         self.a = AmbilData(self)
#         self.a.save()
#         print ("sucess")
#         pass

    def m_button4OnButtonClick24(self, event):
        'aplikasi akan diarahkan ke halaman sesuai dengan jenis soal/versi'
        self.m_panel7.Show()
        self.m_panel8.Hide()
        self.m_button3.Enable()
        self.m_panel9.Hide()
        self.m_panel3.Update()
        self.m_panel3.Refresh()
        self.m_panel3.Layout()
        self.m_simplebook1.SetSelection(2)

        'Tipe'
        self.tipe = 1
        self.versi_soal = 24
#         print ("tes soal item {} dan tipe".format(self.versi_soal,self.tipe))

    def m_button5OnButtonClick60(self, event):
        'aplikasi akan diarahkan ke halaman sesuai dengan jenis soal/versi'
        self.m_panel7.Hide()
        self.m_panel8.Show()
        self.m_button3.Enable()
        self.m_panel9.Hide()
        self.m_panel3.Update()
        self.m_panel3.Refresh()
        self.m_panel3.Layout()
        self.m_simplebook1.SetSelection(2)

        'Tipe'
        self.tipe = 2
        self.versi_soal = 60
#         print ("tes soal item {} dan tipe".format(self.versi_soal,self.tipe))

   
    def m_button6OnButtonClick100(self, event):
        '''
        aplikasi akan diarahkan ke halaman sesuai dengan jenis soal/versi
        '''
        self.m_panel7.Hide()
        self.m_panel8.Hide()
        self.m_panel9.Show()
        self.m_button3.Enable()
        self.m_panel3.Update()
        self.m_panel3.Refresh()
        self.m_panel3.Layout()  
        self.m_simplebook1.SetSelection(2)

        'Tipe'
        self.tipe = 3
        self.versi_soal = 100
#         print ("tes soal item {} dan tipe".format(self.versi_soal,self.tipe))

    def m_button7OnButtonClick(self, event):
        print ("not know what is this function for")
        pass
            
    def m_menuItem1OnMenuSelection(self, event):
        print ("Aplikasi ditutup")
        self.Close()
            
    def m_button_cOnButtonClick(self, event):
        print ("tes over here 'c' grafik Conscientouseness " )
        
        if self.no_database == 1 :
            self.hasil_subdimensi = self.x
            self.hasil_dimensi = self.y
            print (self.rincian_data_peserta)
            print (self.rincian_data_peserta[0][5])
            if self.rincian_data_peserta[0][5] == "Laki - Laki":
                print ("laki - laki ini")
                self.m_choice1.SetSelection(0)
            else :
                print ("perempuan ini")
                self.m_choice1.SetSelection(1)

            pass

        elif self.no_database == 0 :
        
            self.hitung = HitungData(self)
            self.hasil_subdimensi,self.hasil_dimensi = self.hitung.hitung()
        # print (self.hasil_subdimensi)
  
        self.grafik = GrafikC(self)
        self.grafik.Show()
        pass

    def m_button_aOnButtonClick(self, event):
        print ("tes over here 'a' grafik Agreeableness")
        if self.no_database == 1 :
            self.hasil_subdimensi = self.x
            self.hasil_dimensi = self.y
            print (self.rincian_data_peserta)
            print (self.rincian_data_peserta[0][5])

            if self.rincian_data_peserta[0][5] == "Laki - Laki":
                print ("laki - laki ini")
                self.m_choice1.SetSelection(0)
            else :
                print ("perempuan ini")
                self.m_choice1.SetSelection(1)        
        elif self.no_database == 0 :
        
            self.hitung = HitungData(self)
            self.hasil_subdimensi,self.hasil_dimensi = self.hitung.hitung()
        print (self.hasil_subdimensi)
       
        self.grafik = GrafikA(self)
        
        self.grafik.Show()
        pass
    
    def m_button_emOnButtonClick(self, event):
        print ("tes over here 'em'")
        if self.no_database == 1 :
            self.hasil_subdimensi = self.x
            self.hasil_dimensi = self.y
            print (self.rincian_data_peserta)
            print (self.rincian_data_peserta[0][5])
            if self.rincian_data_peserta[0][5] == "Laki - Laki":
                print ("laki - laki ini")
                self.m_choice1.SetSelection(0)
            else :
                print ("perempuan ini")
                self.m_choice1.SetSelection(1)        
        elif self.no_database == 0 :     
            self.hitung = HitungData(self)
            self.hasil_subdimensi,self.hasil_dimensi = self.hitung.hitung()
        print (self.hasil_subdimensi)

        self.grafik = GrafikEm(self)
        self.grafik.Show()
        pass
    
    def m_button_hOnButtonClick(self, event):
        print ("tes over here 'h'")
        
        if self.no_database == 1 :
            self.hasil_subdimensi = self.x
            self.hasil_dimensi = self.y
            print (self.rincian_data_peserta)
            print (self.rincian_data_peserta[0][5])
            if self.rincian_data_peserta[0][5] == "Laki - Laki":
                print ("laki - laki ini")
                self.m_choice1.SetSelection(0)
            else :
                print ("perempuan ini")
                self.m_choice1.SetSelection(1)        
        elif self.no_database == 0 :
        
            self.hitung = HitungData(self)
            self.hasil_subdimensi,self.hasil_dimensi = self.hitung.hitung()
        print (self.hasil_subdimensi)

        self.grafik = GrafikH(self)
        self.grafik.Show()
        pass

    def m_button_exOnButtonClick(self, event):
        print ("tes over here ' ex '")
        
        if self.no_database == 1 :
            self.hasil_subdimensi = self.x
            self.hasil_dimensi = self.y
            print (self.rincian_data_peserta)
            print (self.rincian_data_peserta[0][5])
            if self.rincian_data_peserta[0][5] == "Laki - Laki":
                print ("laki - laki ini")
                self.m_choice1.SetSelection(0)
            else :
                print ("perempuan ini")
                self.m_choice1.SetSelection(1)        
        elif self.no_database == 0 :
        
            self.hitung = HitungData(self)
            self.hasil_subdimensi,self.hasil_dimensi = self.hitung.hitung()
        print (self.hasil_subdimensi)

        self.grafik = GrafikEx(self)
        self.grafik.Show()
        pass

    def m_button_oOnButtonClick(self, event):
        print ("print over here 'openness to experience grafik terpisah'")
         
        if self.no_database == 1 :
            self.hasil_subdimensi = self.x
            self.hasil_dimensi = self.y
            print (self.rincian_data_peserta)
            print (self.rincian_data_peserta[0][5])
            if self.rincian_data_peserta[0][5] == "Laki - Laki":
                print ("laki - laki ini")
                self.m_choice1.SetSelection(0)
            else :
                print ("perempuan ini")
                self.m_choice1.SetSelection(1)        
        elif self.no_database == 0 :
        
            self.hitung = HitungData(self)
            self.hasil_subdimensi,self.hasil_dimensi = self.hitung.hitung()
        print (self.hasil_subdimensi)
            
        self.grafik = GrafikO(self)
        self.grafik.Show()
        pass
    
    def m_button_iaOnButtonClick(self, event):
        print ("print over here 'ia'")

        if self.no_database == 1 :
            self.hasil_subdimensi = self.x
            self.hasil_dimensi = self.y
            print (self.rincian_data_peserta)
            print (self.rincian_data_peserta[0][5])
            if self.rincian_data_peserta[0][5] == "Laki - Laki":
                print ("laki - laki ini")
                self.m_choice1.SetSelection(0)
            else :
                print ("perempuan ini")
                self.m_choice1.SetSelection(1)        
        elif self.no_database == 0 :
        
            self.hitung = HitungData(self)
            self.hasil_subdimensi,self.hasil_dimensi = self.hitung.hitung()
        print (self.hasil_subdimensi)
            
        self.grafik = GrafikIA(self)
        self.grafik.Show()
        pass
    
    def m_menuItem2OnMenuSelection(self, event):
        self.buka = TentangAplikasi(self)
        self.buka.Show()
    
    def m_button_lihat_biodata(self, event):
        if self.m_button1.IsEnabled()==False:
            
            self.item = self.m_listCtrl_tabel_database.GetFocusedItem()
            self.get_item_id_name = self.m_listCtrl_tabel_database.GetItemText(self.item,col=1)
            self.get_item_no_tes = self.m_listCtrl_tabel_database.GetItemText(self.item,col=5)
           
            print ("akhi")
            self.rinci_list = ["idpeserta",self.get_item_id_name.upper()]
            self.rincian_input_data_peserta = query_input_peserta(self.rinci_list)
            self.rincian_data_peserta = query_tabel_data_peserta([self.get_item_id_name.upper(),"","","","idpeserta"])
            
            print (self.rincian_input_data_peserta)
            print (self.rincian_data_peserta)
            print ("dimana ini")
            self.titik = 1
        else :
            self.titik = 0    
        self.buka_lihat_biodata = Biodata(self)
        self.buka_lihat_biodata.set_biodata(self.titik)
        self.buka_lihat_biodata.Show()
        
    
    
    def m_button_lihatOnButtonClick(self, event):
        print ("You have click 'Lihat'")
        self.no_database = 1
        self.item = self.m_listCtrl_tabel_database.GetFocusedItem()
        self.get_item_id_name = self.m_listCtrl_tabel_database.GetItemText(self.item,col=1)
        self.query = TarikData(["idpeserta",self.get_item_id_name])

        self.rinci_list = ["idpeserta",self.get_item_id_name.upper()]
        self.rincian_data_peserta = query_tabel_data_peserta([self.get_item_id_name.upper(),"","","","idpeserta"])

        print (self.query.lihat_keseluruhan())
        print (self.query.data_versi())
        print ("Jumlah soal = {}".format(self.query.tipe_soal()))
        print (type(self.query.asdict()))
        print (self.query.asdict())
        self.tipe_soal= self.query.tipe_soal()
        self.hexaco_calculations = DimensiHexaco(self.query.tipe_soal(),self.query.asdict())
        self.x,self.y = self.hexaco_calculations.hitung()
        
        self.ambil = AmbilData(self)
        self.ambil.save()

        print (self.x)
        print (self.y)
        
        
        
        self.m_button1.Disable()
        self.m_button2.Disable()
        self.m_button3.Disable()
        self.m_button_simpan_data.Disable()
        
        self.m_simplebook1.SetSelection(3)
#         self.no_database = 0
        pass
    
    def m_button21_bersihkan(self, event):
        
        self.control_t.clear_biodata()
        self.no_database = 0
        self.data_induk = AmbilData(self)
#       self.data_induk.data_induk()
  
        print ("bersihkan is here")
    
    
    def m_button_simpan_dataOnButtonClick(self, event):
        from coreapps.models.query import insert_input_peserta
        
        self.control_entry = ControlEntry(self)
        print (self.control_entry.get_input_biodata())
        
        if self.tipe == 1 :
                self.control_entry.panjang_data = len(self.control_entry.get_input_versi24())
                self.control_entry.get_input = self.control_entry.get_input_versi24()

        elif self.tipe == 2 :   
                self.control_entry.panjang_data= len(self.control_entry.get_input_versi60())
                self.control_entry.get_input = self.control_entry.get_input_versi60()

        elif self.tipe == 3 :
                self.control_entry.panjang_data = len(self.control_entry.get_input_versi100())
                self.control_entry.get_input = self.control_entry.get_input_versi100()

        else :
                print ("error di pilih tipe")
        
        self.no_tes = self.control_entry.get_input_biodata()[0]
        self.tanggal_tes = self.control_entry.get_input_biodata()[1]
        self.nama_kandidat = self.control_entry.get_input_biodata()[2]
        self.jenis_kelamin = self.control_entry.get_input_biodata()[3]
        self.tanggal_lahir = self.control_entry.get_input_biodata()[4]
        self.pendidikan_terakhir = self.control_entry.get_input_biodata()[5]
        self.jurusan_pendidikan = self.control_entry.get_input_biodata()[6]
        self.kota = self.control_entry.get_input_biodata()[7]
        self.perusahaan_instansi = self.control_entry.get_input_biodata()[8]
        self.posisi_jabatan = self.control_entry.get_input_biodata()[9]
        print (self.tanggal_tes)
        
        values_id_peserta = [self.tipe, 
                            self.no_tes,
                            self.tanggal_tes,
                            self.nama_kandidat,
                            self.jenis_kelamin,
                            self.tanggal_lahir,
                            self.pendidikan_terakhir,
                            self.jurusan_pendidikan,
                            self.kota,
                            self.perusahaan_instansi,
                            self.posisi_jabatan]

        """
        Instruksi untuk memasukkan ke dalam database (rincian data peserta)
        Id Peserta harus di generasi terlebih dahulu oleh instruksi di bawah ini
        """
        self.input_data_peserta = insert_data_peserta(values_id_peserta)
        values = []
        print (self.control_entry.get_input)
        print (len(self.control_entry.get_input))
        for key in self.control_entry.get_input:
                values.append((key[0],key[1],self.tipe,1))
                print (key[0])
        print (values)
        
        '''
        Instruksi untuk memasukkan ke dalam database
        '''
        self.input_jawaban_peserta = insert_input_peserta(values)
        
        '''
        wx.Message Box return OK
        '''
        self.dialog_simpan = TurunanDialogSimpan(self)
        self.dialog_simpan.Show()
        pass
    

    def m_button_buka_windows_filterOnButtonClick(self, event):
        self.buka_jendela_filter = BukaFilter(self)
        self.buka_jendela_filter.Show()
            
    def m_button_hapus_data_listctrlOnButtonClick(self, event):
        from coreapps.models.query import hapus_data_input_peserta,hapus_data_rincian_peserta
        
        '''
        Memperoleh data id untuk dihapus berdasarkan idpeserta
        print (self.m_listCtrl_tabel_database.GetFocusedItem())
        print (self.m_listCtrl_tabel_database.GetItemText(0,1))
        '''
        self.values = [self.m_listCtrl_tabel_database.GetItemText(0,1)]
        self.hapus_datainput = hapus_data_input_peserta(self.values)
        self.hapus_datarincian = hapus_data_rincian_peserta(self.values)        
        self.m_listCtrl_tabel_database.DeleteItem(self.m_listCtrl_tabel_database.GetFocusedItem())              
        pass
    
    def m_radioBtn1OnRadioButtonSoal24(self, event):
        event.Skip()
    
    def m_radioBtn2OnRadioButtonSoal60(self, event):
        event.Skip()
            
    def m_radioBtn3OnRadioButtonSoal100(self, event):
        event.Skip()

