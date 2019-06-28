'''
Created on Mar 22, 2019

@author: cireng
'''
import sqlite3


# import pathlib
# path  = pathlib.Path.cwd()/"coreapps/models/hexacodb"
def connectdb(path):
    conne = sqlite3.connect(path)
    return conne


if __name__ == '__main__':
    path = "hexacodb"
#     cekidpesertaakhir()
#     values = [cekidpesertaakhir()+1,"Edward Shaldi","23-08-1998","Laki-laki","Makasar",1]
    QueryDataPeserta()
#     insertdatapeserta(values)
#     print (cekidpesertaakhir()+1)

