#! /usr/bin/env python
'''
Created on Jun 12, 2019

@author: cireng
'''
"""
Class untuk memanggil grafik baik yang ada di dalam Frame Utama ataupun
Frame Terpisah
"""


from coreapps.views.grafikmatplotlib import GrafikDimensi,\
GrafikA,GrafikC,GrafikEm,GrafikEx,GrafikH,GrafikIA,GrafikO



class GrafikDimensi(GrafikDimensi):
    
    
    def __init__(self,parent):
        super().__init__(parent)
    
    def save_file(self):
        self.save = self.save_figure()        
        return self.save

class GrafikA(GrafikA):
    
    
    def __init__(self,parent):
        super().__init__(parent)

class GrafikC(GrafikC):
    
    
    def __init__(self,parent):
        super().__init__(parent)
        

class GrafikEm(GrafikEm):
    
    
    def __init__(self,parent):
        super().__init__(parent)
        

class GrafikEx(GrafikEx):
    
    
    def __init__(self,parent):
        super().__init__(parent)
    

class GrafikH(GrafikH):
    

    def __init__(self,parent):
        super().__init__(parent)
        
        
class GrafikIA(GrafikIA):
    

    def __init__(self,parent):
        super().__init__(parent)
        
        
class GrafikO(GrafikO):


    def __init__(self,parent):
        super().__init__(parent)