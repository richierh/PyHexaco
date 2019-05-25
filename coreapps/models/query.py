#! usr/bin/env python

'''
Created on May 4, 2019

@author: cireng
'''

import pathlib
import sqlite3

global path

def connect_db():
    path = pathlib.Path.cwd() / "models/hexacodb"
#     path = pathlib.Path.cwd() / "hexacodb"

    print ("Connecting to {}".format(path))
    print("...Processing....")
    conne = sqlite3.connect(str(path))
    return conne

def path():
    pathl = pathlib.Path.cwd() / "models/hexacodb"
    return pathl

def insert_input_peserta(values):
   
    conne = connect_db()
    cursorexe = conne.cursor()
    
    sql_cmd = """
INSERT INTO Input_Data_Jawaban_Peserta
(NoSoal, JawabanPeserta, idTipeSoal, idpeserta, idDimensi)
VALUES(?,?,?, (SELECT idpeserta
                from 'Rincian Data Peserta'
                order by idpeserta
                DESC limit 1), ?);
"""

    cursorexe.executemany(sql_cmd,values)
    conne.commit()
    conne.close
    print ("insert data done")

def insert_data_peserta(values):
    conne = connect_db()
    cursorexe = conne.cursor()
    
    sqlcmd = """INSERT INTO "Rincian Data Peserta"
(idtipesoal,"No Tes", "Tanggal Tes", "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi", "Posisi / Jabatan")
VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);    """
    
    cursorexe.execute(sqlcmd, values)
    conne.commit()
    conne.close()

    
def cek_id_peserta_terakhir():
    
    conne = connect_db()
    cursorexe = conne.cursor()
    sqlcmd = """SELECT idpeserta
                from 'Rincian Data Peserta'
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
# SELECT idpeserta, idtipesoal, "No Tes", "Tanggal Tes", "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi", "Posisi / Jabatan"
# FROM "Rincian Data Peserta"
# WHERE idpeserta = 2 ;
def query_data_peserta():
#     Menampilkan data dari Input Peserta
    conne = connect_db()
    cursorexe = conne.cursor()
    sqlcmd = """SELECT I.idinputpeserta ,
                I.NoSoal,I.JawabanPeserta,T.NamaSoal 
                FROM Input_data_Jawaban_Peserta AS I
                LEFT JOIN TipeSoal as T ON I.idTipeSoal \
                =T.idTipeSoal"""
    cursorexe.execute(sqlcmd)
    getdatas = cursorexe.fetchall()
    for data in getdatas:
        print (data)
    
    conne.close
    
def query_tabel_data_peserta(value):
    conne = connect_db()
    
    print (value[0],value[1],value[2],value[3])
    print ("ini value {},{},{},{}".format(value[0],value[1],value[2],value[3]))
    cursorexe = conne.cursor()
    
    if value[4]=="nama orang":
        sql_cmd = """
    SELECT idpeserta, idtipesoal, "No Tes", "Tanggal Tes", "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi", "Posisi / Jabatan"
    FROM "Rincian Data Peserta" 
    WHERE "Nama Kandidat" = ?;
    """
        cursorexe.execute(sql_cmd,((value[0],)))

    elif value[4] == "no tes":
        sql_cmd = """
                    SELECT idpeserta, idtipesoal, "No Tes", "Tanggal Tes", "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi", "Posisi / Jabatan"
                    FROM "Rincian Data Peserta" 
                    WHERE "No Tes" = ?;
                """
        cursorexe.execute(sql_cmd,((value[1],)))
    
    elif value[4]=="tanggal":
        sql_cmd = """
                    SELECT idpeserta, idtipesoal, "No Tes", "Tanggal Tes", "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi", "Posisi / Jabatan"
                    FROM "Rincian Data Peserta" 
                    WHERE "Tanggal Tes" BETWEEN ? AND ?;
                """
        cursorexe.execute(sql_cmd,((value[2],value[3])))

    elif value[4] == "idpeserta":
        sql_cmd = """
                    SELECT idpeserta, idtipesoal, "No Tes", "Tanggal Tes", "Nama Kandidat", "Jenis Kelamin", "Tanggal Lahir", "Pendidikan Terakhir", "Jurusan Pendidikan", Kota, "Perusahaan / Instansi", "Posisi / Jabatan"
                    FROM "Rincian Data Peserta" 
                    WHERE "idpeserta" = ?;
                """
        cursorexe.execute(sql_cmd,((value[0 ],)))
 


    getdatas = cursorexe.fetchall()
    data_list = []
    for data in getdatas:
        data_list.append(data)
    conne.close
    
    return data_list

def hapus_data_rincian_peserta(values):
    conne = connect_db()
    
    cursorexe= conne.cursor()
    sql_cmd ="""DELETE FROM "Rincian Data Peserta"
WHERE idpeserta=?;
    """
    cursorexe.execute(sql_cmd,(values),)
    conne.commit()
    conne.close
    
def hapus_data_input_peserta(values):
    conne = connect_db()
    
    cursorexe= conne.cursor()
    sql_cmd ="""DELETE FROM "Input_Data_Jawaban_Peserta"
WHERE idpeserta=?;
    """
    cursorexe.execute(sql_cmd,(values),)
    conne.commit()
    conne.close

if __name__ == "__main__":
    
    path = pathlib.Path.cwd() / "hexacodb"
#     print (path)
#     connect_db(path)
#     values = [(1,1,1,2,1),(1,1,1,1,1)]
#     insert_input_peserta(values)
    query_tabel_data_peserta("OFI SUNASTRI")
    print (query_tabel_data_peserta("OFI SUNASTRI"))
    
    
    