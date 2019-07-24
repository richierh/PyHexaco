#! usr/bin/env python

'''
Created on May 18, 2019

@author: cireng
'''
import sqlite3
import pathlib

def connect_db():
    path = pathlib.Path.cwd()/"hexacodb"
    
    try:  
        connect = sqlite3.connect(path)
    except :
        print ("tidak konek database")

    return connect
    
class ReferensiDimensi():
    
    
    def __init__(self,parent):
        self.con = parent
#         print ("Sukses")

        pass
    
    def __query(self):
        self.cursor = self.con.cursor()
        
        sql_cmd = """
        SELECT *
        FROM "Referensi Dimensi";"""
        
        self.cursor.execute(sql_cmd)
        
        self.data_tabel = self.cursor.fetchall()
#         for data in self.data_tabel:
#             print (data)
        
        self.con.close()
    
        return self.data_tabel
    
    def hasil(self,parent2,**values):
        self.query = self.__query()
        self.parent = parent2
#         print (self.query[0])
        
        data_pria = {}
        data_wanita = {}
        nilai_tinggi = {}
        nilai_rendah = {}
        prilaku_tinggi = {}
        prilaku_rendah ={}
        for query in self.query:
#             print (query[1])
            data_pria[query[1]]=query[2]
            data_wanita[query[1]]=query[3]
            nilai_tinggi[query[1]]=query[4]
            nilai_rendah[query[1]]=query[5]
            prilaku_tinggi[query[1]]=query[6]        
            prilaku_rendah[query[1]]=query[7]
            
#         print (data_pria)
#         print (data_wanita)
        
        self.data_output=[]
        
        if self.parent == "L" :
            print ("Laki-laki")
            for key,value in values.items():
#                 print (values[value])
                if values[key]>data_pria[key]:
#                     print ("nilai tinggi")
                    self.dimensi = key
                    self.nilai_kandidat = values[key]
                    self.penilaian = nilai_tinggi[key]
                    self.prilaku = prilaku_tinggi[key]
#                     print (key)
#                     print (values[key])
#                     print (nilai_tinggi[key])
#                     print (prilaku_tinggi[key])
                    self.data_output.append([self.dimensi,self.nilai_kandidat,self.penilaian,self.prilaku,"Tinggi"])
                else :
#                     print ("nilai rendah")
                    self.dimensi = key
                    self.nilai_kandidat = values[key]
                    self.penilaian = nilai_rendah[key]
                    self.prilaku = prilaku_rendah[key]
#                     print (key)
#                     print (values[key])
#                     print (nilai_tinggi[key])
#                     print (prilaku_tinggi[key])
                    self.data_output.append([self.dimensi,self.nilai_kandidat,self.penilaian,self.prilaku,"Rendah"])


#                 print ("ini dari referensi {}".format(data_pria))
#                 print ("ini dari hasil {}".format(values))
            print ("Nilai Pria")
        elif self.parent =="P":
            print ("Perempuan")
            for key,value in values.items():
#                 print (values[value])
                if values[key]>data_wanita[key]:
                    print ("nilai tinggi")
                    self.dimensi = key
                    self.nilai_kandidat = values[key]
                    self.penilaian = nilai_tinggi[key]
                    self.prilaku = prilaku_tinggi[key]
                    self.data_output.append([self.dimensi,self.nilai_kandidat,self.penilaian,self.prilaku,"Tinggi"])
                    
                else :
                    print ("nilai rendah")
                    self.dimensi = key
                    self.nilai_kandidat = values[key]
                    self.penilaian = nilai_rendah[key]
                    self.prilaku = prilaku_rendah[key]

                    self.data_output.append([self.dimensi,self.nilai_kandidat,self.penilaian,self.prilaku,"Rendah"])

#                 print ("ini dari referensi {}".format(data_pria))
#                 print ("ini dari hasil {}".format(values))
            print ("Nilai wanita")      
        else :
            print ("Anda salah dalam menentukan pilihan")
        
        return self.data_output

if __name__=="__main__":
    konekto = connect_db()
    dimensi_values ={
'Sincerity': 3.25,
'Fairness': 3.23,
'Greed Avoidance': 2.18,
'Modesty': 3.29,
'Honesty – Humility': 3.17,
'Fearfullness': 2.58,
'Anxiety': 3.33,
'Dependence': 2.60,
'Sentimentality': 2.76,
'Emotionality': 2.2,
'Social Self Esteem': 3.11,
'Social Boldness': 3.2,
'Sociability': 2.33,
'Liveliness': 3.45,
'Extraversion': 3.67,
'Forgiveness': 2.89,
'Gentleness': 2.99,
'Flexibility': 2.28,
'Patience': 3.11,
'Agreeableness': 2.13,
'Organization': 3.15,
'Diligence': 3.45,
'Perfectionism': 3.99,
'Prudence': 3.99,
'Conscientiouseness': 3.99,
'Aesthetic Appreciation': 3.91,
'Inquitiveness': 4.94,
'Creativity': 3.12,
'Unconventionality': 3.26,
'Openess To Experience': 3.23,
'(Interstitial Facet Scale) Interstitial': 3.26,
'Interestial Scale': 2.5}
    print (dimensi_values)
        
        
    run_app = ReferensiDimensi(konekto)
#     print (run_app.query()[0][6])
    print (run_app.hasil("L",**dimensi_values))
    
    
    
        
        
        
        