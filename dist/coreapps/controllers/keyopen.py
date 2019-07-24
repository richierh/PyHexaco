'''
Created on Mar 21, 2019

@author: cireng
'''
import platform


def cekplatform():
    myplatform = platform.system()
    print (myplatform)
    
    if myplatform == "Windows":
        print ("sistem operasi {}".format(myplatform))
        
    elif myplatform == "Linux" :
        print ("sistem operasi {}".format(myplatform))
    
    else :
        print ("sistem operasi tidak dikenali {}".format(myplatform))

