'''
Created on Mar 21, 2019

@author: cireng
'''
import os
import pathlib
import gettext
import sys
# print (os.getcwd())

pathwd = pathlib.Path.cwd()/"hexaco"
pathcont = pathlib.Path.cwd()/"hexaco/controllers"
pathview = pathlib.Path.cwd()/"hexaco/views"
print (pathcont)

sys.path.append(str(pathcont))
sys.path.append(str(pathview))
print (sys.path)
os.chdir(str(pathwd))
# print (os.getcwd())

from hexaco.controllers import cekplatform 
from hexaco.views import MyApp
# print (dir())
cekplatform()
gettext.install("myApp")
run = MyApp(0)
run.MainLoop()
# print(pathwd)