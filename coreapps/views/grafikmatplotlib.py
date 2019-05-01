#! usr/bin/python

import matplotlib
import wx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure


class GrafikMatplotlib():

    def __init__(self):
        matplotlib.rcParams['toolbar'] = 'None'
        # Fixing random state for reproducibility
        np.random.seed(19680801)
        
        plt.rcdefaults()
        self.fig, self.ax = plt.subplots()
        
        # Example data
        self.people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
        self.y_pos = np.arange(len(self.people))
        self.performance = 3 + 10 * np.random.rand(len(self.people))
        error = np.random.rand(len(self.people))
        
        self.ax.barh(self.y_pos, self.performance, xerr=error, align='center',
                color='green', ecolor='black')
        self.ax.set_yticks(self.y_pos)
        self.ax.set_yticklabels(self.people)
        self.ax.invert_yaxis()  # labels read top-to-bottom
        self.ax.set_xlabel('Performance')
        self.ax.set_title('How fast do you want to go today?')
        
        plt.show()

class PanelObjek():
    
    
    def __init__(self,parent):
        self.parent = parent
        
#         self.parent.GrafikMatplotlib.SetBackgroundColor(wx.RED)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.parent.GrafikMatplotlib,-1,self.figure)
        
        self.sizer90 = wx.BoxSizer(wx.VERTICAL)
        self.sizer90.Add(self.canvas,1,wx.ALL|wx.EXPAND)
      
#         self.parent.GrafikMatplotlib.SetSizer(self.sizer90)
        

        
               

        
        pass
    
    
    
if __name__=="__main__":
    app = GrafikMatplotlib()