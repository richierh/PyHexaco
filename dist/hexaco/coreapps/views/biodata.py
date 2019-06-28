'''
Created on Jun 14, 2019

@author: cireng
'''

from coreapps.views.maingui import Biodata
from coreapps.views.control_text import ControlEntry

class Biodata(Biodata):
    
    
    def __init__(self,parent):
        super().__init__(parent)
        
        self.parent = parent
#         print ("diturunkan dari class Biodata")
    
    def set_biodata(self,titik):
        if titik == 1 :
            self.m_textCtrl1.SetValue(str(self.parent.rincian_data_peserta[0][2]))
            self.m_textCtrl205.SetValue(str(self.parent.rincian_data_peserta[0][3]))
            self.m_textCtrl3.SetValue(str(self.parent.rincian_data_peserta[0][4]))
            self.m_textCtrl206.SetValue(str(self.parent.rincian_data_peserta[0][5]))
            self.m_textCtrl207.SetValue(str(self.parent.rincian_data_peserta[0][6]))
            self.m_textCtrl208.SetValue(str(self.parent.rincian_data_peserta[0][7]))
            self.m_textCtrl7.SetValue(str(self.parent.rincian_data_peserta[0][8]))
            self.m_textCtrl8.SetValue(str(self.parent.rincian_data_peserta[0][9]))
            self.m_textCtrl9.SetValue(str(self.parent.rincian_data_peserta[0][10]))
            self.m_textCtrl10.SetValue(str(self.parent.rincian_data_peserta[0][11]))

        else :
            print (self.parent.control_t.get_input_biodata())
            self.m_textCtrl1.SetValue(str(self.parent.control_t.get_input_biodata()[0]))
            self.m_textCtrl205.SetValue(str(self.parent.control_t.get_input_biodata()[1]))
            self.m_textCtrl3.SetValue(str(self.parent.control_t.get_input_biodata()[2]))
            self.m_textCtrl206.SetValue(str(self.parent.control_t.get_input_biodata()[3]))
            self.m_textCtrl207.SetValue(str(self.parent.control_t.get_input_biodata()[4]))
            self.m_textCtrl208.SetValue(str(self.parent.control_t.get_input_biodata()[5]))
            self.m_textCtrl7.SetValue(str(self.parent.control_t.get_input_biodata()[6]))
            self.m_textCtrl8.SetValue(str(self.parent.control_t.get_input_biodata()[7]))
            self.m_textCtrl9.SetValue(str(self.parent.control_t.get_input_biodata()[8]))
            self.m_textCtrl10.SetValue(str(self.parent.control_t.get_input_biodata()[9]))
