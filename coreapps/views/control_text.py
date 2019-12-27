#! usr/bin/env python
'''
Created on May 5, 2019

@author: cireng
'''

import wx
from dateutil.utils import today


class TestPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        self.entry = wx.TextCtrl(self, -1)
        self.entry.Bind(wx.EVT_CHAR, self.handle_keypress)

    def handle_keypress(self, event):
        keycode = event.GetKeyCode()
        if keycode < 255:
            # valid ASCII
            if chr(keycode).isalnum():
                # Valid alphanumeric character
                event.Skip()
               
                
class ControlEntry(wx.Frame):
    
    def __init__(self, parent):
        super(ControlEntry, self).__init__(parent)
        self.parent = parent
        self.text_biodata = [self.parent.m_textCtrl1,
                           self.parent.m_datePicker1,
                           self.parent.m_textCtrl3,
                           self.parent.m_choice1,
                           self.parent.m_datePicker2,
                           self.parent.m_choice2,
                           self.parent.m_textCtrl7,
                           self.parent.m_textCtrl8,
                           self.parent.m_textCtrl9,
                           self.parent.m_textCtrl10]

        self.text_versi24 = [self.parent.m_textCtrl11,
                           self.parent.m_textCtrl12,
                           self.parent.m_textCtrl13,
                           self.parent.m_textCtrl14,
                           self.parent.m_textCtrl15,
                           self.parent.m_textCtrl16,
                           
                           self.parent.m_textCtrl17,
                           self.parent.m_textCtrl18,
                           self.parent.m_textCtrl19,
                           self.parent.m_textCtrl20,
                           self.parent.m_textCtrl21,
                           self.parent.m_textCtrl22,
                           
                           self.parent.m_textCtrl23,
                           self.parent.m_textCtrl24,
                           self.parent.m_textCtrl25,
                           self.parent.m_textCtrl26,
                           self.parent.m_textCtrl27,
                           self.parent.m_textCtrl28,
            
                           self.parent.m_textCtrl29,
                           self.parent.m_textCtrl30,
                           self.parent.m_textCtrl31,
                           self.parent.m_textCtrl32,
                           self.parent.m_textCtrl33,
                           self.parent.m_textCtrl34] 
                           
        self.text_versi60 = [self.parent.m_textCtrl42,
                           self.parent.m_textCtrl43,
                           self.parent.m_textCtrl44,
                           self.parent.m_textCtrl45,
                           self.parent.m_textCtrl46,
                           self.parent.m_textCtrl47,
                           self.parent.m_textCtrl48,
                           self.parent.m_textCtrl49,
                           self.parent.m_textCtrl50,
                           self.parent.m_textCtrl51,
                           
                           self.parent.m_textCtrl52,
                           self.parent.m_textCtrl53,
                           self.parent.m_textCtrl54,
                           self.parent.m_textCtrl55,
                           self.parent.m_textCtrl56,
                           self.parent.m_textCtrl57,
                           self.parent.m_textCtrl58,
                           self.parent.m_textCtrl59,
                           self.parent.m_textCtrl60,
                           self.parent.m_textCtrl61,
        
                           self.parent.m_textCtrl62,
                           self.parent.m_textCtrl63,
                           self.parent.m_textCtrl64,
                           self.parent.m_textCtrl65,
                           self.parent.m_textCtrl66,
                           self.parent.m_textCtrl67,
                           self.parent.m_textCtrl68,
                           self.parent.m_textCtrl69,
                           self.parent.m_textCtrl70,
                           self.parent.m_textCtrl71,
        
                           self.parent.m_textCtrl72,
                           self.parent.m_textCtrl73,
                           self.parent.m_textCtrl74,
                           self.parent.m_textCtrl75,
                           self.parent.m_textCtrl76,
                           self.parent.m_textCtrl77,
                           self.parent.m_textCtrl78,
                           self.parent.m_textCtrl79,
                           self.parent.m_textCtrl80,
                           self.parent.m_textCtrl81,
                          
                           self.parent.m_textCtrl82,
                           self.parent.m_textCtrl83,
                           self.parent.m_textCtrl84,
                           self.parent.m_textCtrl85,
                           self.parent.m_textCtrl86,
                           self.parent.m_textCtrl87,
                           self.parent.m_textCtrl88,
                           self.parent.m_textCtrl89,
                           self.parent.m_textCtrl90,
                           self.parent.m_textCtrl91,
        
                           self.parent.m_textCtrl92,
                           self.parent.m_textCtrl93,
                           self.parent.m_textCtrl94,
                           self.parent.m_textCtrl95,
                           self.parent.m_textCtrl96,
                           self.parent.m_textCtrl97,
                           self.parent.m_textCtrl98,
                           self.parent.m_textCtrl99,
                           self.parent.m_textCtrl100,
                           self.parent.m_textCtrl101]
        self.text_versi100 = [self.parent.m_textCtrl981,
                            self.parent.m_textCtrl991,
                            self.parent.m_textCtrl1001,
                            self.parent.m_textCtrl1011,
                            self.parent.m_textCtrl102,
                            self.parent.m_textCtrl103,
                            self.parent.m_textCtrl104,
                            self.parent.m_textCtrl105,
                            self.parent.m_textCtrl106,
                            self.parent.m_textCtrl107,
#                             Kolom ke 1
                            self.parent.m_textCtrl108,
                            self.parent.m_textCtrl109,
                            self.parent.m_textCtrl110,
                            self.parent.m_textCtrl111,
                            self.parent.m_textCtrl112,
                            self.parent.m_textCtrl113,
                            self.parent.m_textCtrl114,
                            self.parent.m_textCtrl115,
                            self.parent.m_textCtrl116,
                            self.parent.m_textCtrl117,
#                             Kolom ke 2
                            self.parent.m_textCtrl118,
                            self.parent.m_textCtrl119,
                            self.parent.m_textCtrl120,
                            self.parent.m_textCtrl121,
                            self.parent.m_textCtrl122,
                            self.parent.m_textCtrl123,
                            self.parent.m_textCtrl124,
                            self.parent.m_textCtrl125,
                            self.parent.m_textCtrl126,
                            self.parent.m_textCtrl127,
#                             Kolom ke 3
                            self.parent.m_textCtrl128,
                            self.parent.m_textCtrl129,
                            self.parent.m_textCtrl130,
                            self.parent.m_textCtrl131,
                            self.parent.m_textCtrl132,
                            self.parent.m_textCtrl133,
                            self.parent.m_textCtrl134,
                            self.parent.m_textCtrl135,
                            self.parent.m_textCtrl136,
                            self.parent.m_textCtrl137,
#                             Kolom ke 4
                            self.parent.m_textCtrl139,
                            self.parent.m_textCtrl140,
                            self.parent.m_textCtrl141,
                            self.parent.m_textCtrl142,
                            self.parent.m_textCtrl143,
                            self.parent.m_textCtrl144,
                            self.parent.m_textCtrl145,
                            self.parent.m_textCtrl146,
                            self.parent.m_textCtrl147,
                            self.parent.m_textCtrl148,
#                              Kolom ke 5
                            self.parent.m_textCtrl149,
                            self.parent.m_textCtrl150,
                            self.parent.m_textCtrl151,
                            self.parent.m_textCtrl152,
                            self.parent.m_textCtrl153,
                            self.parent.m_textCtrl154,
                            self.parent.m_textCtrl155,
                            self.parent.m_textCtrl156,
                            self.parent.m_textCtrl157,
                            self.parent.m_textCtrl158,
#                             Kolom ke 6
                            self.parent.m_textCtrl159,
                            self.parent.m_textCtrl160,
                            self.parent.m_textCtrl161,
                            self.parent.m_textCtrl162,
                            self.parent.m_textCtrl163,
                            self.parent.m_textCtrl164,
                            self.parent.m_textCtrl165,
                            self.parent.m_textCtrl166,
                            self.parent.m_textCtrl167,
                            self.parent.m_textCtrl168,
#                             Kolom ke 7
                            self.parent.m_textCtrl170,
                            self.parent.m_textCtrl171,
                            self.parent.m_textCtrl172,
                            self.parent.m_textCtrl173,
                            self.parent.m_textCtrl174,
                            self.parent.m_textCtrl175,
                            self.parent.m_textCtrl176,
                            self.parent.m_textCtrl177,
                            self.parent.m_textCtrl178,
                            self.parent.m_textCtrl179,
#                             Kolom ke 8
                            self.parent.m_textCtrl181,
                            self.parent.m_textCtrl182,
                            self.parent.m_textCtrl183,
                            self.parent.m_textCtrl184,
                            self.parent.m_textCtrl185,
                            self.parent.m_textCtrl186,
                            self.parent.m_textCtrl187,
                            self.parent.m_textCtrl188,
                            self.parent.m_textCtrl189,
                            self.parent.m_textCtrl190,
#                             Kolom ke 9
                            self.parent.m_textCtrl191,
                            self.parent.m_textCtrl192,
                            self.parent.m_textCtrl193,
                            self.parent.m_textCtrl194,
                            self.parent.m_textCtrl195,
                            self.parent.m_textCtrl196,
                            self.parent.m_textCtrl197,
                            self.parent.m_textCtrl198,
                            self.parent.m_textCtrl199,
                            self.parent.m_textCtrl200]
        

    def get_input_biodata(self):
#         ambil data biodata

        
        self.data_biodata = []
        for self.data in self.text_biodata:
            if self.text_biodata.index(self.data) == 3 \
                or self.text_biodata.index(self.data) == 5:
                
                self.data_in = self.data.GetString(self.data.GetSelection())
                self.data_biodata.append(self.data_in)

            elif self.text_biodata.index(self.data) == 1 \
                or self.text_biodata.index(self.data) == 4:
                
                self.data_in = self.data.GetValue().Format("%Y/%m/%d")
                self.data_biodata.append(self.data_in)
           
            else :
                self.data_in = self.data.GetValue()
                self.data_biodata.append(self.data_in)
                
        return self.data_biodata

    def clear_biodata(self):
        for self.data in self.text_biodata:
            if self.text_biodata.index(self.data) == 3 \
                or self.text_biodata.index(self.data) == 5:
                self.data_in = self.data.SetSelection(0)

            elif self.text_biodata.index(self.data) == 1 \
                or self.text_biodata.index(self.data) == 4:
                
                self.data_in = self.data.SetValue(wx.DateTime.Now())
           
            else :
                self.data_in = self.data.SetValue("")
        
        for self.clear in self.text_versi24 :
            
            self.clear.SetValue("")
        
        for self.clear in self.text_versi60 :
            
            self.clear.SetValue("")


        for self.clear in self.text_versi100 :
            
            self.clear.SetValue("")
            
        if self.parent.m_button1.Enable() == True:
            self.parent.m_simplebook1.SetSelection(4)   
            
            
        for self.clear in self.text_versi24 :
            self.clear.SetValue("")
         
        for self.clear in self.text_versi60 :
            self.clear.SetValue("")

        for self.clear in self.text_versi100 :
            self.clear.SetValue("")
            
        self.parent.m_button1.Enable()
        self.parent.m_button2.Enable()
        self.parent.m_button3.Enable()
        self.parent.m_button_simpan_data.Enable()
        

        
    def get_input_versi24(self):

        self.data_versi24 = {}
        self.number = 1
        for self.data in self.text_versi24:
            self.data_in = self.data.GetValue()
            self.data_versi24[str(self.number)] = self.data_in
            self.number += 1           
        
        return self.data_versi24.items()

    def get_input_versi60(self):

        
        self.data_versi60 = {}
        self.number = 1
        for self.data in self.text_versi60:
            self.data_in = self.data.GetValue()
            self.data_versi60[str(self.number)] = self.data_in
            self.number += 1
            
        return self.data_versi60.items()
        
    def get_input_versi100(self):

        self.data_versi100 = {}
        self.number = 1
        for self.data in self.text_versi100:
            self.data_in = self.data.GetValue()
            self.data_versi100[str(self.number)] = self.data_in
            self.number += 1
              
        return self.data_versi100.items()
            

if __name__ == "__main__":
    root = wx.App()
    run_app = ControlEntry(None)
    run_app.Show()
    root.MainLoop()
    
