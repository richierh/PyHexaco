#!usr/bin/env python

'''
Created on Mar 21, 2019

from oscheck import *
import@author: cireng
'''

import gettext
import os
import pathlib
import sys



#from coreapps.controllers.keyopen import cekplatform 
from coreapps.views.app import MyApp

# print (os.getcwd())
pathwd = pathlib.Path.cwd() / "coreapps"
#pathcont = pathlib.Path.cwd() / "coreapps/controllers"
#pathview = pathlib.Path.cwd() / "coreapps/views"
#print (pathcont)

#sys.path.append(str(pathcont))
#sys.path.append(str(pathview))
sys.path.append(str(pathwd))

print (sys.path)
os.chdir(str(pathwd))
# print (os.getcwd())

# print (dir())
#cekplatform()
gettext.install("myApp")
run = MyApp(0)
run.MainLoop()