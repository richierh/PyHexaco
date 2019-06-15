#! /usr/bin/env python
import wx
# from ObjectListView import ObjectListView, ColumnDefn
# 
# random_objects = [
#     {"parameter": "Test", "value": "1"},
#     {"parameter": "Test2", "value": "2"}
# ]
# 
# 
# class MainFrame(wx.Frame):
#     def __init__(self):
#         super(MainFrame, self).__init__(parent=None, title="OLV Test")
#         panel = MainPanel(self)
#         self.Show()
# 
# 
# class MainPanel(wx.Panel):
#     def __init__(self, parent):
#         super(MainPanel, self).__init__(parent)
# 
#         self.olv = ObjectListView(parent=self, style=wx.LC_REPORT | wx.BORDER_SUNKEN, sortable=True,
#                                   useAlternateBackColors=False, cellEditMode=ObjectListView.CELLEDIT_DOUBLECLICK)
#         self.olv.SetColumns([
#             ColumnDefn(title="Parameter", valueGetter="parameter", isSpaceFilling=True, isEditable=False),
#             ColumnDefn(title="Value", valueGetter="value", isSpaceFilling=True)
#         ])
# 
#         get_button = wx.Button(self, label="Print objects")
# 
#         top_sizer = wx.BoxSizer(wx.VERTICAL)  # Root sizer
#         olv_sizer = wx.BoxSizer(wx.VERTICAL)  # For the ObjectListView
#         button_sizer = wx.BoxSizer(wx.HORIZONTAL)
# 
#         olv_sizer.Add(self.olv, 1, wx.LEFT | wx.RIGHT | wx.EXPAND | wx.ALIGN_TOP, 5)
#         button_sizer.Add(get_button, 0, wx.ALL | wx.ALIGN_LEFT, 5)
# 
#         top_sizer.Add(olv_sizer, 1, wx.ALL | wx.EXPAND, 5)
#         top_sizer.Add(button_sizer, 0, wx.ALL | wx.EXPAND, 5)
# 
#         self.SetSizerAndFit(top_sizer)
#         self.Bind(wx.EVT_BUTTON, handler=self.get_objects, source=get_button)
# 
#         self.olv.SetObjects(random_objects)
# 
#     def get_objects(self, event):
#         for item in self.olv.GetObjects():
#             print("Parameter: {param}".format(param=item['parameter']))
#             print("Value: {val}".format(val=item['value']))
# 
# 
# if __name__ == "__main__":
#     wx_app = wx.App()
#     frame = MainFrame()
#     wx_app.MainLoop()