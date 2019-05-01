#! usr/bin/env python


import pathlib
import os
"""c
from oscheck import *
import wx
"""

import os
import sys
import pathlib

# path = "{}{}".format(os.getcwd(), "/aplikasi")
# print (type(path))
path = pathlib.Path.cwd() / 'aplikasi'
# print (type(path))

sys.path.append(str(path))
sys.path
print (sys.path)
# os.getcwd()
# cd = "{}{}".format(os.getcwd(), "/AppsSDS")
cd = pathlib.Path.cwd() / "aplikasi"
os.chdir(str(cd))

from aplikasi.views.app import MyApp

run = MyApp(0)
run.MainLoop()
