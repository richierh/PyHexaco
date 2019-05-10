#! usr/bin/python


import matplotlib
import wx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from coreapps.views.maingui import FrameDepan


class GrafikDimensi(FrameDepan):
    
    def __init__(self,parent):
        self.parent = parent
        self.np = np
        
        self.colors_6_dimensi = ["r","g","b","m","purple","y","grey"]
        self.colors_honesty_humility = []
        self.colors_emotionality = []
        self.colors_extraversion = []
        self.colors_agreeableness = []
        self.colors_conscientiousness = []
        self.colors_openness_to_experience = []
        self.colors_interestitial = []
#        method inherit
        self.figure = Figure()#figsize=(0,4))
#         self.figure.subplots_adjust(1,1,0,1)
        
        
        
        self.axes_6_dimensi = self.figure.add_subplot(121)
        self.axes_honesty_humility = self.figure.add_subplot(6,2,2)
        self.axes_2 = self.figure.add_subplot(6,2,4)
        self.axes_3 = self.figure.add_subplot(6,2,6)
        self.axes_4 = self.figure.add_subplot(6,2,8)
        self.axes_5 = self.figure.add_subplot(6,2,10)
        self.axes_6 = self.figure.add_subplot(6,2,12)
        
        self.axes_honesty_humility.get_xaxis().set_visible(False)
        self.axes_2.get_xaxis().set_visible(False)
        self.axes_3.get_xaxis().set_visible(False)
        self.axes_4.get_xaxis().set_visible(False)
        self.axes_5.get_xaxis().set_visible(False)

        self.canvas = FigureCanvas(self.parent.GrafikMatplotlib,
                                   -1,
                                   self.figure)
        

        self.sizer90 = wx.BoxSizer(wx.VERTICAL)
        self.sizer90.Add(self.canvas,1,wx.ALL|wx.EXPAND)
#         memasukkan grafik ke dalam panel yang ada di hexacofile
#         print (self)

    def draw(self):
       
        self.data_y = ["Honesty\nHumility",
                       "Emotionality\nDomain",
                       "Extraversion\nDomain",
                       "Agreeableness\nDomain",
                       "Conscientiousness\nDomain",
                       "Openness to\nExperience\n Domain",
                       "Interstitial\nScale"]

        if self.parent.versi_soal == 24 :
            del self.data_y[6]
            print (self.data_y)
#             print ("tes")
        

        self.y_pos = self.np.arange(len(self.data_y))
        self.value = [3.14,5,4.56,1.45,3.67,2.67]
#         self.value = 3 + 10 * self.np.random.rand(len(self.data_y))
#         self.error = self.np.random.rand(len(self.data_y))
        self.axes_6_dimensi.barh(self.y_pos,
                       self.value,
                       height=0.7,
                       align='center',
                       color=self.colors_6_dimensi)
        
        self.axes_6_dimensi.set_xlim(left=0,right=5)
        self.axes_6_dimensi.set_ylim(bottom=-1, top=6)
        self.axes_6_dimensi.annotate('Nilai Rata-Rata', 
                                     xy=(1,-1),
                                     xytext=(1,-1.65),
                                     arrowprops = dict(facecolor='black',
                                                       shrink=2,
                                                       headwidth=5,
                                                       width=1))

        self.axes_6_dimensi.set_yticks(self.y_pos)
        self.axes_6_dimensi.set_yticklabels(self.data_y,
                                            fontname="Tw Cen MT",
                                            fontsize=14)
        self.axes_6_dimensi.invert_yaxis()
        
        for iterate,value_y_dimension in enumerate(self.value):
            if value_y_dimension == 0 :
                K = 0
            else :
                K = 0.5
                
            self.axes_6_dimensi.text(value_y_dimension-K,
                                     iterate+0.1,
                                     str(round(value_y_dimension,2)),
                                     color='black')
#                                      fontweight='bold')
        
        
        
        self.data_y1 = ["Sincerity",
                        "Fairness",
                        "Greed Avoidance",
                        "Modesty"]
        
        self.y_pos1 = self.np.arange(len(self.data_y1))
        self.value1 = [5,2,3,4]
        self.axes_honesty_humility.barh(self.y_pos1,
                         self.value1,
                         align='center',
                         color="r")
        
        self.axes_honesty_humility.set_xlim(left=0,right=5)
        self.axes_honesty_humility.set_yticks(self.y_pos1)
        self.axes_honesty_humility.set_yticklabels(self.data_y1,fontsize=8,fontname="Tw Cen MT")
        
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
    
    