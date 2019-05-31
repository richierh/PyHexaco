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
#         print (self.get_input_data)
#         print (self.parent.versi_soal)
       
        
#         self.get_input_data = {'1': '4', '2': '2', '3': '5', '4': '3', '5': '5',
#                 '6': '4', '7': '1', '8': '1', '9': '1', '10': '1',
#                 '11': '4', '12': '2', '13': '2', '14': '1',
#                 '15': '5', '16': '1', '17': '2', '18': '1',
#                 '19': '5', '20': '1', '21': '4', '22': '1',
#                 '23': '1', '24': '4', '25': '5', '26': '5',
#                 '27': '1', '28': '2', '29': '4', '30': '1',
#                 '31': '1', '32': '5', '33': '2', '34': '2',
#                 '35': '4', '36': '1', '37': '4', '38': '1',
#                 '39': '3', '40': '3', '41': '4', '42': '2',
#                 '43': '3', '44': '2', '45': '3', '46': '5',
#                 '47': '1', '48': '1', '49': '3', '50': '2',
#                 '51': '4', '52': '3', '53': '1', '54': '3',
#                 '55': '5', '56': '1', '57': '3', '58': '5',
#                 '59': '2', '60': '5'}
        
        self.data = DimensiHexaco(self.parent.versi_soal,self.get_input_data)
        hasil_dimensi,hasil_subdimensi = self.data.hitung()
        return hasil_dimensi,hasil_subdimensi

    
    
if __name__=="__main__":
    run=HitungData(DimensiHexaco)
    run.hitung()
        
        