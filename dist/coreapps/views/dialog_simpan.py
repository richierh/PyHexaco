#!/usr/bin/env python

'''
Created on May 26, 2019

@author: cireng
'''


import wx
from coreapps.views.maingui import DialogSimpan

class TurunanDialogSimpan(DialogSimpan):
    
    
    def __init__(self,parent):
        super(TurunanDialogSimpan,self).__init__(parent)
        self.parent=parent
        
    
    def m_button_dialog_simpan_berhasil(self, event):
        self.Close()
        pass