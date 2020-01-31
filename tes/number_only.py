# exploring the wxPython widget
# wx.TextCtrl(parent, id, value, pos, size, style)
# limit entry to numeric values with max 2 decimals
import wx


class MyFrame(wx.Frame):

    def __init__(self, parent, mytitle, mysize):
        wx.Frame.__init__(self, parent, -1, mytitle, size=mysize)
        self.SetBackgroundColour("white")
        s = "Enter the price:"
        self.label = wx.StaticText(self, -1, s, pos=(10, 10))
        self.edit = wx.TextCtrl(self, -1, pos=(10, 30))
        # respond to enter key when focus is on edit
        self.edit.Bind(wx.EVT_TEXT, self.onAction)
        # print("j")

    def onAction(self, event):
        """
        check for numeric entry and limit to 2 decimals
        accepted result is in self.value
        """
        raw_value = self.edit.GetValue().strip()
        # numeric check
        if all(x in '0123456789.+-' for x in raw_value):
            # convert to float and limit to 2 decimals
            self.value = round(float(raw_value), 2)
            self.edit.ChangeValue(str(self.value))
        else:
#             self.edit.ChangeValue("Number only")
            self.edit.ChangeValue("")


app = wx.App(0)
# create a MyFrame instance and show the frame
mytitle = 'Numeric entry test'
width = 400
height = 300
MyFrame(None, mytitle, (width, height)).Show()
app.MainLoop()
