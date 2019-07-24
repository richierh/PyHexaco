#! usr/bin/env python
'''
Created on May 18, 2019

@author: cireng
'''
import wx
from coreapps.views.maingui import FrameGrafikTerpisah
from wx.lib.agw import ultimatelistctrl as ULC
from wx.lib.wordwrap import wordwrap


class PropertiesGrafikTerpisah(FrameGrafikTerpisah):
    
    def __init__(self,parent):
        super(PropertiesGrafikTerpisah,self).__init__(parent)
        self.parent = parent
        self.parent = parent
        try:
            font = wx.SystemSettings_GetFont(wx.SYS_DEFAULT_GUI_FONT)
            boldfont = wx.SystemSettings_GetFont(wx.SYS_DEFAULT_GUI_FONT)
        except AttributeError:
            # wxPython 4 / Phoenix updated SystemSettings
            font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
            boldfont = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
 
        boldfont.SetWeight(wx.BOLD)
        boldfont.SetPointSize(12)
      
        info = ULC.UltimateListItem()
        info._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_CHECK
#         info.SetWidth(50)
        info._image = []
        info._format = 0
#         info._kind = 0
        info._text = "Dimensi"
        self.ultimateList.InsertColumnInfo(0, info)
 
        info = ULC.UltimateListItem()
        info._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT #| ULC.ULC_MASK_FONT
        info._format = wx.LIST_FORMAT_LEFT
        info._image = []
#         info._width = 300

        info._text = "Definisi"
#         info._font = boldfont
        self.ultimateList.InsertColumnInfo(2, info)
 
        info = ULC.UltimateListItem()
        info._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT 
#         info._width = 500
        info._format = wx.LIST_FORMAT_LEFT
        
        info._text = "Ciri - Ciri"
#         info._font = font
        info._image = []
        self.ultimateList.InsertColumnInfo(3, info)


        info = ULC.UltimateListItem()
        info._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT #| ULC.ULC_MASK_FONT
        info._format = wx.LIST_FORMAT_LEFT
        info._image = []
#         info._width = 300

        info._text = "Nilai"
#         info._font = boldfont
        self.ultimateList.InsertColumnInfo(1, info)


        self.ultimateList.SetColumnWidth(0, 200)
        self.ultimateList.SetColumnWidth(1, 150)
        self.ultimateList.SetColumnWidth(2, 400)
        self.ultimateList.SetColumnWidth(3, 400)
        
        self.ultimateList.DeleteAllItems()

        
        self.Update()
        self.Refresh()
        self.Layout()
        self.ultimateList.Bind(wx.EVT_LIST_COL_BEGIN_DRAG ,self.runnow  )


    def insert_value_list(self,parent):
        self.ultimateList.DeleteAllItems()

#         items = [("aaahfhfghfghfghfghfghfghfhfghfghfghfghfghfghfg","bbbb",'dsfasfsdfsdfsdf'),
#                  ("jhgjgjgjgjhjgj","ddd",'sdfsfdsdfsf')]

        self.parent = parent
        items = self.parent.data
        print ("ini items {}".format(items))
        item_wordwrap=[]
        
        index = 0 
        for item in items :
            print (item)
            item1 = wordwrap(item[0],self.ultimateList.GetColumnWidth(0),wx.ClientDC(self),breakLongWords=True, margin=0)
            item2 = wordwrap(item[1],self.ultimateList.GetColumnWidth(1)-10,wx.ClientDC(self),breakLongWords=True, margin=0)
            item3 = wordwrap(item[2],self.ultimateList.GetColumnWidth(2)-75,wx.ClientDC(self),breakLongWords=True, margin=0)
#   Adding one more column
            item4 = wordwrap(item[3],self.ultimateList.GetColumnWidth(3)-75,wx.ClientDC(self),breakLongWords=True, margin=0)

            item_wordwrap.append((item1, item2,item3,item4))
            index+=1
        print (item_wordwrap)        

        indexitem=0
        for item in item_wordwrap:
            self.ultimateList.InsertStringItem(indexitem, item[0])
            self.ultimateList.SetStringItem(indexitem,1,item[1])
            self.ultimateList.SetStringItem(indexitem,2,item[2])
            self.ultimateList.SetStringItem(indexitem,3,item[3])

            indexitem += 1
            
       
        self.Update()
        self.Refresh()
        self.Layout()
        
    def runnow(self,event):
        print ("drag finished")
        self.insert_value_list(self)
        
        
        
        

class GrafikFrame(PropertiesGrafikTerpisah):
    
    
    def __init__(self,parent):
        super(GrafikFrame,self).__init__(parent)
        self.parent = parent
        



if __name__== "__main__":
    root = wx.App()
    run = GrafikFrame(None).Show()
    root.MainLoop()