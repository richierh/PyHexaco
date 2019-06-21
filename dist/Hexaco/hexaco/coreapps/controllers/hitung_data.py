'''
Created on May 28, 2019

@author: cireng
'''
from coreapps.controllers.hexaco_calculation import DimensiHexaco



class HitungData():
    
    def __init__(self,parent):
        self.parent = parent
#         print (self.parent.versi_soal)
    
        if self.parent.versi_soal==24:
            self.get_input = self.parent.text_entry.get_input_versi24()
        elif self.parent.versi_soal==60:
            self.get_input= self.parent.text_entry.get_input_versi60()
        elif self.parent.versi_soal == 100:
            self.get_input = self.parent.text_entry.get_input_versi100()
    #    
        self.__format_data()
#         print (self.get_input_data)
        
        pass
        
    def __format_data(self):

        self.get_input_data = {}
        for data,hasil in self.get_input:
#             print (data)
            if hasil == "":
                hasil = "0"
            self.get_input_data[str(data)]=str(hasil)
        return self.get_input_data
    
    def hitung(self):
        
        self.data = DimensiHexaco(self.parent.versi_soal,self.get_input_data)
        hasil_dimensi,hasil_subdimensi = self.data.hitung()
        return hasil_dimensi,hasil_subdimensi

class HitungDataDatabase():
    
    def __init__(self,parent):
        self.parent = parent
#         print (self.parent.versi_soal)
#         if self.parent.query.tipe_soal()==24:
#             self.get_input = self.parent.text_entry.get_input_versi24()
#         elif self.parent.query.tipe_soal()==60:
#             self.get_input= self.parent.text_entry.get_input_versi60()
#         elif self.parent.query.tipe_soal() == 100:
#             self.get_input = self.parent.text_entry.get_input_versi100()
# #    
        self.__format_data()
#         print (self.get_input_data)
        
        pass
        
    def __format_data(self):

        self.get_input_data = {}
        for data,hasil in self.get_input:
#             print (data)
            if hasil == "":
                hasil = "0"
            self.get_input_data[str(data)]=str(hasil)
        return self.get_input_data
    
    def hitung(self):
        
        self.data = DimensiHexaco(self.parent.versi_soal,self.get_input_data)
        hasil_dimensi,hasil_subdimensi = self.data.hitung()
        return hasil_dimensi,hasil_subdimensi
    
if __name__=="__main__":
    run=HitungData(DimensiHexaco)
    run.hitung()
        
        