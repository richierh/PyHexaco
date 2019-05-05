#! usr/bin/python


import matplotlib
import wx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from coreapps.views.maingui import FrameDepan


class GrafikMatplotlib():

    def __init__(self):
        matplotlib.rcParams['toolbar'] = 'None'
        # Fixing random state for reproducibility
        np.random.seed(19680801)
        
        plt.rcdefaults()
        self.fig, self.ax = plt.subplots()
        
        # Example data
        colors = list('rgbmk')
        self.people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
        self.y_pos = np.arange(len(self.people))
        self.performance = 3 + 10 * np.random.rand(len(self.people))
        error = np.random.rand(len(self.people))
        
        self.ax.barh(self.y_pos, self.performance, xerr=error, align='center',
                color=colors, ecolor='black')
        self.ax.set_yticks(self.y_pos)
        self.ax.set_yticklabels(self.people)
        self.ax.invert_yaxis()  # labels read top-to-bottom
        self.ax.set_xlabel('Performance')
        self.ax.set_title('How fast do you want to go today?')
        
        plt.show()


class GrafikDimensi(FrameDepan):
    
    def __init__(self,parent):
        self.parent = parent
        self.np = np
#        method inherit
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        
#        grafik di petakan oleh add_subplot
#        digit 111 menyatakan posisi 
#        1 = row , 1 = column , 1 = grafik
        self.canvas = FigureCanvas(self.parent.GrafikMatplotlib,
                                   -1,
                                   self.figure)
        
        self.sizer90 = wx.BoxSizer(wx.VERTICAL)
        self.sizer90.Add(self.canvas,1,wx.ALL|wx.EXPAND)
#         memasukkan grafik ke dalam panel yang ada di hexacofile
#         print (self)

    def draw(self):
        
        self.data_y = ["O","C","A","Ex","EM","H"]
        self.y_pos = self.np.arange(len(self.data_y))
        print (len(self.data_y))
        self.value = 3 + 10 * self.np.random.rand(len(self.data_y))
#         self.error = self.np.random.rand(len(self.data_y))
        self.colors = ["r","g","b","m","k","y"]
        
        
        self.axes.barh(self.y_pos,
                       self.value,
#                        xerr=self.error, 
                       align='center',
                       color=self.colors)
#                        ecolor='black')
        self.axes.set_yticks(self.y_pos)
        self.axes.set_yticklabels((self.data_y))
        self.axes.invert_yaxis()
        pass
    
    
class GrafikO():
        
    def __init__(self,parent):
#         buat konstruktor
        self.parent = parent
        self.matplotlib = matplotlib
        self.np = np
        self.plt = plt

#         metode untuk menghilangkan toolbar
        self.matplotlib.rcParams['toolbar'] = 'None'
        
        
        # Fixing random state for reproducibility
        self.np.random.seed(19680801)
        
        self.plt.rcdefaults()
        self.fig, self.ax = self.plt.subplots()
        
        # Example data
        self.people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
        self.y_pos = self.np.arange(len(self.people))
        self.performance = 3 + 10 * self.np.random.rand(len(self.people))
        error = self.np.random.rand(len(self.people))
        
        self.ax.barh(self.y_pos, self.performance, xerr=error, align='center',
                color='green', ecolor='black')
        self.ax.set_yticks(self.y_pos)
        self.ax.set_yticklabels(self.people)
        self.ax.invert_yaxis()  # labels read top-to-bottom
        self.ax.set_xlabel('Performance')
        self.ax.set_title('How fast do you want to go today?')
        
        self.plt.show()        


class GrafikC():
    
    def __init__(self,parent):
#         buat konstruktor
        self.parent = parent
        self.matplotlib = matplotlib
        self.np = np
        self.plt = plt

#         metode untuk menghilangkan toolbar
        self.matplotlib.rcParams['toolbar'] = 'None'
        
        # Fixing random state for reproducibility
        self.np.random.seed(19680801)
        
        self.plt.rcdefaults()
        self.fig, self.ax = self.plt.subplots()
        
        # Example data
        self.people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
        self.y_pos = self.np.arange(len(self.people))
        self.performance = 3 + 10 * self.np.random.rand(len(self.people))
        error = self.np.random.rand(len(self.people))
        
        self.ax.barh(self.y_pos, self.performance, xerr=error, align='center',
                color='green', ecolor='black')
        self.ax.set_yticks(self.y_pos)
        self.ax.set_yticklabels(self.people)
        self.ax.invert_yaxis()  # labels read top-to-bottom
        self.ax.set_xlabel('Performance')
        self.ax.set_title('How fast do you want to go today?')
        
        self.plt.show()     
        
    
class GrafikA():
        
    def __init__(self,parent):
#         buat konstruktor
        self.parent = parent
        self.matplotlib = matplotlib
        self.np = np
        self.plt = plt

#         metode untuk menghilangkan toolbar
        self.matplotlib.rcParams['toolbar'] = 'None'
        
        
        # Fixing random state for reproducibility
        self.np.random.seed(19680801)
        
        self.plt.rcdefaults()
        self.fig, self.ax = self.plt.subplots()
        
        # Example data
        self.people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
        self.y_pos = self.np.arange(len(self.people))
        self.performance = 3 + 10 * self.np.random.rand(len(self.people))
        error = self.np.random.rand(len(self.people))
        
        self.ax.barh(self.y_pos, self.performance, xerr=error, align='center',
                color='green', ecolor='black')
        self.ax.set_yticks(self.y_pos)
        self.ax.set_yticklabels(self.people)
        self.ax.invert_yaxis()  # labels read top-to-bottom
        self.ax.set_xlabel('Performance')
        self.ax.set_title('How fast do you want to go today?')
        
        self.plt.show()    

class GrafikEx():
        
    def __init__(self,parent):
#         buat konstruktor
        self.parent = parent
        self.matplotlib = matplotlib
        self.np = np
        self.plt = plt

#         metode untuk menghilangkan toolbar
        self.matplotlib.rcParams['toolbar'] = 'None'
        
        
        # Fixing random state for reproducibility
        self.np.random.seed(19680801)
        
        self.plt.rcdefaults()
        self.fig, self.ax = self.plt.subplots()
        
        # Example data
        self.people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
        self.y_pos = self.np.arange(len(self.people))
        self.performance = 3 + 10 * self.np.random.rand(len(self.people))
        error = self.np.random.rand(len(self.people))
        
        self.ax.barh(self.y_pos, self.performance, xerr=error, align='center',
                color='green', ecolor='black')
        self.ax.set_yticks(self.y_pos)
        self.ax.set_yticklabels(self.people)
        self.ax.invert_yaxis()  # labels read top-to-bottom
        self.ax.set_xlabel('Performance')
        self.ax.set_title('How fast do you want to go today?')
        
        self.plt.show()    


class GrafikEm():
        
    def __init__(self,parent):
#         buat konstruktor
        self.parent = parent
        self.matplotlib = matplotlib
        self.np = np
        self.plt = plt

#         metode untuk menghilangkan toolbar
        self.matplotlib.rcParams['toolbar'] = 'None'
        
        
        # Fixing random state for reproducibility
        self.np.random.seed(19680801)
        
        self.plt.rcdefaults()
        self.fig, self.ax = self.plt.subplots()
        
        # Example data
        self.people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
        self.y_pos = self.np.arange(len(self.people))
        self.performance = 3 + 10 * self.np.random.rand(len(self.people))
        error = self.np.random.rand(len(self.people))
        
        self.ax.barh(self.y_pos, self.performance, xerr=error, align='center',
                color='green', ecolor='black')
        self.ax.set_yticks(self.y_pos)
        self.ax.set_yticklabels(self.people)
        self.ax.invert_yaxis()  # labels read top-to-bottom
        self.ax.set_xlabel('Performance')
        self.ax.set_title('How fast do you want to go today?')
        
        self.plt.show()   
        
   
class GrafikH():
        
    def __init__(self,parent):
#         buat konstruktor
        self.parent = parent
        self.matplotlib = matplotlib
        self.np = np
        self.plt = plt

#         metode untuk menghilangkan toolbar
        self.matplotlib.rcParams['toolbar'] = 'None'
        
        
        # Fixing random state for reproducibility
        self.np.random.seed(19680801)
        
        self.plt.rcdefaults()
        self.fig, self.ax = self.plt.subplots()
        
        # Example data
        self.people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
        self.y_pos = self.np.arange(len(self.people))
        self.performance = 3 + 10 * self.np.random.rand(len(self.people))
        error = self.np.random.rand(len(self.people))
        
        self.ax.barh(self.y_pos, self.performance, xerr=error, align='center',
                color='green', ecolor='black')
        self.ax.set_yticks(self.y_pos)
        self.ax.set_yticklabels(self.people)
        self.ax.invert_yaxis()  # labels read top-to-bottom
        self.ax.set_xlabel('Performance')
        self.ax.set_title('How fast do you want to go today?')
        
        self.plt.show()           
if __name__=="__main__":
    app = GrafikDimensi()
    app.draw()
    
    