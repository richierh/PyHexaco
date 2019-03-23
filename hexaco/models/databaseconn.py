'''
Created on Mar 22, 2019

@author: cireng
'''
import sqlite3
# import pathlib
# path  = pathlib.Path.cwd()/"hexaco/models/hexacodb"



def connectdb(path):
    conne = sqlite3.connect(path)
    return conne

    
def insertdatapeserta(values):
    conne = connectdb(path)
    cursorexe = conne.cursor()
    
    sqlcmd = """
    INSERT INTO datapeserta (idpeserta , namapeserta , tgllhr , jnskelamin , alamat , jnspeserta )
    VALUES (?,?,?,?,?,?)
    """
    cursorexe.execute(sqlcmd,values)
    conne.commit()
    conne.close()

def cekidpesertaakhir():
    
    conne = connectdb(path)
    cursorexe = conne.cursor()
    sqlcmd = """
    SELECT idpeserta from datapeserta order by idpeserta DESC limit 1
    """
    cursorexe.execute(sqlcmd)
    getid = cursorexe.fetchone()
#     print (getid[0])
    conne.close()
    return getid[0]

if __name__ == '__main__':
    path = "hexacodb"
    cekidpesertaakhir()
    values = [cekidpesertaakhir()+1,"Edward Shaldi","23-08-1998","Laki-laki","Makasar",1]
   
    insertdatapeserta(values)
    print (cekidpesertaakhir()+1)

