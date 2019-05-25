#! usr/bin/env python

"""c
from oscheck import *
import wx
"""
# path = "{}{}".format(os.getcwd(), "/aplikasi")
# print (type(path))

import os
import os
import pathlib
import pathlib
import sys

from aplikasi.views.app import MyApp

path = pathlib.Path.cwd() / 'aplikasi'
# print (type(path))

sys.path.append(str(path))
sys.path
print (sys.path)
# os.getcwd()
# cd = "{}{}".format(os.getcwd(), "/AppsSDS")
cd = pathlib.Path.cwd() / "aplikasi"
os.chdir(str(cd))

run = MyApp(0)
run.MainLoop()
