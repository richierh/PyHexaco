#! usr/bin/env python

'''
Created on May 4, 2019

@author: cireng
'''


import sqlite3
import pathlib

def connect_db(path):
    conne = sqlite3.connect(str(path))
    return conne

def insert_data_peserta(values):
    conne = connect_db(path)
    cursorexe = conne.cursor()
    
    sqlcmd = """
    INSERT INTO datapeserta (idpeserta , namapeserta , tgllhr , jnskelamin , alamat , jnspeserta )
    VALUES (?,?,?,?,?,?)
    """
    cursorexe.execute(sqlcmd, values)
    conne.commit()
    conne.close()
    
def cek_id_peserta_terakhir():
    
    conne = connect_db(path)
    cursorexe = conne.cursor()
    sqlcmd = """SELECT idpeserta
                from datapeserta
                order by idpeserta
                DESC limit 1"""
    cursorexe.execute(sqlcmd)
    getid = cursorexe.fetchone()
#     print (getid[0])
    conne.close()
    return getid[0]


def query_input_peserta():
#     Menampilkan data dari Input Peserta
    conne = connect_db(path)
    cursorexe = conne.cursor()
    sqlcmd = """SELECT I.idinputpeserta ,I.NoSoal,
                I.JawabanPeserta,T.NamaSoal 
                FROM InputPeserta AS I
                LEFT JOIN TipeSoal as T ON I.idTipeSoal 
                = T.idTipeSoal"""

    cursorexe.execute(sqlcmd)
    getdatas = cursorexe.fetchall()
    for data in getdatas:
        print (data)
    
    conne.close

def query_data_peserta():
#     Menampilkan data dari Input Peserta
    conne = connect_db(path)
    cursorexe = conne.cursor()
    sqlcmd = """SELECT I.idinputpeserta ,
                I.NoSoal,I.JawabanPeserta,T.NamaSoal 
                FROM InputPeserta AS I
                LEFT JOIN TipeSoal as T ON I.idTipeSoal \
                =T.idTipeSoal"""
    cursorexe.execute(sqlcmd)
    getdatas = cursorexe.fetchall()
    for data in getdatas:
        print (data)
    
    conne.close
    
if __name__=="__main__":
    
    path  = pathlib.Path.cwd()/"hexacodb"
    print (path)
    connect_db(path)

