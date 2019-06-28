#! /usr/bin/env python

'''
Created on Jun 12, 2019

@author: cireng
'''

from coreapps.models.query import query_data_jawaban

class TarikData():
    
    
    def __init__(self,parent):
        self.parent = parent
        self.query = query_data_jawaban(self.parent)
        pass
        
    
    def lihat_keseluruhan(self):
        return self.query
    
    def data_versi(self):
        self.data_versi = {}
        for data in self.query:
            self.data_versi[str(data[2])]=data[3]
            
        self.get_input_data = {}
        for data,hasil in self.data_versi.items():
#             print (data)
            if hasil == "":
                hasil = "0"
            self.get_input_data[str(data)]=str(hasil)
        return self.get_input_data
    
    def asdict(self):        
        return self.get_input_data
        
    def tipe_soal(self):
        if self.query[0][4] == "tipe 24":
            self.tipe = 24
        elif self.query[0][4] == "tipe 60":
            self.tipe = 60
        elif self.query[0][4] == "tipe 100":
            self.tipe = 100
        return self.tipe