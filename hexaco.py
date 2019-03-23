'''
Created on Mar 21, 2019

@author: cireng
'''

import os
import pathlib
from controllers import keyopen
from views.app import MyApp


pathwd = pathlib.Path.cwd()/"hexaco"
os.chdir(pathwd)

keyopen.cekplatform()
  
run = MyApp(0)
run.MainLoop()
print(pathwd)