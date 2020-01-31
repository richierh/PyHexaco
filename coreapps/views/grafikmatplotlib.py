#! usr/bin/python

import wx
import matplotlib
matplotlib.use('WXAgg')   
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg,FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.pyplot import plot as plt
from coreapps.views.maingui import FrameDepan

import numpy as np
from coreapps.controllers.definisi import rerata2


class UIGrafikInherit(FrameDepan):
    
    
    def __init__(self,parent):
        super().__init__(parent)
        pass
        
        
class GrafikDimensi(UIGrafikInherit):
    
    def __init__(self, parent):
        self.parent = parent
        self.np = np
        self.colors_6_dimensi = ["r", "g", "b", "m", "purple", "y", "grey"]
        self.colors_honesty_humility = ["r","r","r","r","r"]
        self.colors_emotionality = ["g","g","g","g","g"]
        self.colors_extraversion = ["b","b","b","b","b"]
        self.colors_agreeableness = ["m","m","m","m","m"]
        self.colors_conscientiousness = ["purple","purple","purple","purple","purple"]
        self.colors_openness_to_experience = ["y","y","y","y","y"]
#         self.colors_interestitial = ["grey","grey","grey","grey","grey"]
        
        'method inherit'
        self.figure = Figure()
        self.figure.subplots_adjust(bottom=None,
                                    left=None,
                                    top = None,
                                    right=0.975,
                                    wspace = 0.3,
                                    hspace = None)     
        # self.figure.tight_layout()   
        self.axes_6_dimensi = self.figure.add_subplot(121)
        self.axes_honesty_humility = self.figure.add_subplot(6,2,2)
        self.axes_Emotionality = self.figure.add_subplot(6, 2, 4)
        self.axes_Extraversion = self.figure.add_subplot(6, 2, 6)
        self.axes_Agreableness = self.figure.add_subplot(6, 2, 8)
        self.axes_Conscientiouseness = self.figure.add_subplot(6, 2, 10)
        self.axes_Openess_To_Experience = self.figure.add_subplot(6, 2, 12)
        
        'Menambah jumlah grafik di sisi sebelah kanan'
#         self.axes_Interestial_Scale = self.figure.add_subplot(7, 2, 14)
        self.canvas = FigureCanvas(self.parent.GrafikMatplotlib,-1,self.figure)
        self.sizer90 = wx.BoxSizer(wx.VERTICAL)
        self.sizer90.Add(self.canvas, 1, wx.ALL | wx.EXPAND)
        
 
    def add_toolbar(self):
        self.toolbar = NavigationToolbar2WxAgg(self.canvas)        
        self.toolbar.Realize()
        self.sizer90.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.Update()        
#         self.__draw()
#         self.manage_window = self.figure.get_current_fig_manager()
    
    def save_figure(self):
        import pathlib
        self.path = pathlib.Path().cwd()/"controllers/reporting/image1.png"
        # print(self.path)
        # print ("lewat sini nggak")
        return self.figure.savefig(self.path,dpi='figure')
        
    
    def draw(self,nilai_dimensi,nilai_sub_dimensi,versi):
        self.a = nilai_sub_dimensi
        self.axes_honesty_humility.get_xaxis().set_ticks([])
#         self.axes_honesty_humility.get_xaxis().set_ticklabels([])
        self.axes_Emotionality.get_xaxis().set_visible(False)
        self.axes_Extraversion.get_xaxis().set_visible(False)
        self.axes_Agreableness.get_xaxis().set_visible(False)
        self.axes_Conscientiouseness.get_xaxis().set_visible(False)
#         self.axes_Openess_To_Experience.get_xaxis().set_ticks([])
#         self.axes_Openess_To_Experience.get_xaxis().set_ticklabels([])
        self.data_y_6_dimensi = ["Honesty\nHumility",
                       "Emotionality\nDomain",
                       "Extraversion\nDomain",
                       "Agreeableness\nDomain",
                       "Conscientiousness\nDomain",
                       "Openness to\nExperience\n Domain",
                       "Interstitial\nScale"]
#         print(versi)
#         print (nilai_dimensi)
#         print (nilai_sub_dimensi)

        if versi == "24" :
            del self.data_y_6_dimensi[6]
            print (self.data_y_6_dimensi)
            # print("cek")
            self.y_pos = self.np.arange(len(self.data_y_6_dimensi))
            self.value = [nilai_dimensi["Honesty & Humility"],nilai_dimensi["Emotionality"],
                                nilai_dimensi["Extraversion"],
                                nilai_dimensi["Agreeableness"],nilai_dimensi["Conscientiousness"],
                                nilai_dimensi["Openness to Experience"]]
            print (self.value)
        else :
            self.y_pos = self.np.arange(len(self.data_y_6_dimensi))
            self.value = [nilai_dimensi["Honesty & Humility"],nilai_dimensi["Emotionality"],
                                nilai_dimensi["Extraversion"],
                                nilai_dimensi["Agreeableness"],nilai_dimensi["Conscientiousness"],
                                nilai_dimensi["Openness to Experience"],
                                nilai_dimensi["Interstitial"]]
#         self.value = 3 + 10 * self.np.random.rand(len(self.data_y_6_dimensi))
#         self.#error = self.np.random.rand(len(self.data_y_6_dimensi))
        self.ax = self.axes_6_dimensi.barh(self.y_pos,
                       self.value,
                       height=0.7,
                       align='center',
                       color=self.colors_6_dimensi)
        self.axes_6_dimensi.set_xlim(left=0, right=5)
        self.axes_6_dimensi.set_ylim(bottom=-1, top=7)
#         self.axes_6_dimensi.annotate('Nilai Rata-Rata', xy=(1, -1), xytext=(1, -1.65), arrowprops=dict(facecolor='black', shrink=2, headwidth=5, width=1))
        self.axes_6_dimensi.set_xlabel("Aspek Kepribadian",
                                       fontname="Tw Cen MT",
                                       fontsize=12)
        self.axes_6_dimensi.xaxis.set_label_position("top")
        self.axes_6_dimensi.set_yticks(self.y_pos)
        self.axes_6_dimensi.set_yticklabels(self.data_y_6_dimensi,
                                            fontname="Tw Cen MT",
                                            fontsize=10)
        self.axes_6_dimensi.invert_yaxis()
 
        def autolabel(rects):
            """
            Attach a text label above each bar displaying its height
            """
            
            for rect in rects:
                width = rect.get_width()
                frac_height = width/5
                if frac_height > 0.95 :
                    label_position = width - (0.05 * width)
                else :
                    label_position = width + (0.01 * width)
                self.axes_6_dimensi.text(label_position,rect.get_y() + rect.get_height()/2.,
                        '{}' .format(round(width,2)),
                        ha='left', va='center')
        autolabel(self.ax)

#         for iterate, value_y_dimension in enumerate(self.value):
#             
#             if value_y_dimension == 0 :
#                 K = 0
#             else :
#                 K = 0.5
#             self.axes_6_dimensi.text(value_y_dimension - K,
#                                      iterate + 0.1,
#                                      str(round(value_y_dimension, 2)),
#                                      color='black')
# #                                      fontweight='bold')

        'Gambar grafik yang sisi kanan paling atas' 
        self.data_y1 = ["Sincerity",
                        "Fairness",
                        "Greed Avoidance",
                        "Modesty"]
        self.y_pos1 = self.np.arange(len(self.data_y1))
#         self.value1 = [5, 2, 3, 4]
        self.value1 = [nilai_sub_dimensi["Sincerity"],
                       nilai_sub_dimensi["Fairness"],
                       nilai_sub_dimensi["Greed Avoidance"],
                       nilai_sub_dimensi["Modesty"]
                       ]
        self.axes_honesty_humility.barh(self.y_pos1,
                         self.value1,
                         align='center',
                         color=self.colors_honesty_humility)
        self.axes_honesty_humility.set_xlim(left=0, right=5)
        self.axes_honesty_humility.set_yticks(self.y_pos1)
        self.axes_honesty_humility.set_yticklabels(self.data_y1, fontsize=9, fontname="Tw Cen MT")
        self.axes_honesty_humility.set_xlabel("Sub-Aspek Kepribadian",fontname="Tw Cen MT",
                                       fontsize=12)
        self.axes_honesty_humility.xaxis.set_label_position("top")

        'Gambar grafik yang sisi kanan paling atas kedua' 
        self.data_y2 = ["Fearfullness",
                        "Anxiety",
                        "Dependence",
                        "Sentimentality"]
        self.y_pos2 = self.np.arange(len(self.data_y2))
#         self.value1 = [5, 2, 3, 4]
        self.value2 = [nilai_sub_dimensi["Fearfullness"],
                       nilai_sub_dimensi["Anxiety"],
                       nilai_sub_dimensi["Dependence"],
                       nilai_sub_dimensi["Sentimentality"]]
        self.axes_Emotionality.barh(self.y_pos2,
                         self.value2,
                         align='center',
                         color=self.colors_emotionality)
        self.axes_Emotionality.set_xlim(left=0, right=5)
        self.axes_Emotionality.set_yticks(self.y_pos2)
        self.axes_Emotionality.set_yticklabels(self.data_y2, fontsize=8, fontname="Tw Cen MT")

        'Gambar grafik yang sisi kanan paling atas ketiga' 
        self.data_y3 = ["Social Self - Esteem",
                        "Social Boldness",
                        "Sociability",
                        "Liveliness"]
        self.y_pos3 = self.np.arange(len(self.data_y3))
#         self.value1 = [5, 2, 3, 4]
        self.value3 = [nilai_sub_dimensi["Social Self Esteem"],
                       nilai_sub_dimensi["Social Boldness"],
                       nilai_sub_dimensi["Sociability"],
                       nilai_sub_dimensi["Liveliness"]]
        self.axes_Extraversion.barh(self.y_pos3,
                         self.value3,
                         align='center',
                         color=self.colors_extraversion)
        self.axes_Extraversion.set_xlim(left=0, right=5)
        self.axes_Extraversion.set_yticks(self.y_pos3)
        self.axes_Extraversion.set_yticklabels(self.data_y3, fontsize=8, fontname="Tw Cen MT")
#         self.axes_Extraversion.set_ylabel("Sub-Dimensi Kepribadian")
        self.axes_Extraversion.yaxis.set_label_position("right")

        'Gambar grafik yang sisi kanan paling bawah ketiga' 
        self.data_y4 = ["Forgiveness",
                        "Gentleness",
                        "Flexibility",
                        "Patience"]
        self.y_pos4 = self.np.arange(len(self.data_y4))
#         self.value4 = [5, 2, 3, 4]
        self.value4 = [nilai_sub_dimensi["Forgiveness"],
                       nilai_sub_dimensi["Gentleness"],
                       nilai_sub_dimensi["Flexibility"],
                       nilai_sub_dimensi["Patience"]]
        self.axes_Agreableness.barh(self.y_pos4,
                         self.value4,
                         align='center',
                         color=self.colors_agreeableness)
        self.axes_Agreableness.set_xlim(left=0, right=5)
        self.axes_Agreableness.set_yticks(self.y_pos4)
        self.axes_Agreableness.set_yticklabels(self.data_y4, fontsize=8, fontname="Tw Cen MT")
 
        'Gambar grafik yang sisi kanan paling bawah kedua' 
        self.data_y5 = ['Organization',
                        'Diligence',
                        'Perfectionism',
                        'Prudence']
        self.y_pos5 = self.np.arange(len(self.data_y5))
#         self.value5 = [5, 2, 3, 4]
        self.value5 = [nilai_sub_dimensi["Organization"],
                       nilai_sub_dimensi["Diligence"],
                       nilai_sub_dimensi["Perfectionism"],
                       nilai_sub_dimensi["Prudence"]]
        self.axes_Conscientiouseness.barh(self.y_pos5,
                         self.value5,
                         align='center',
                         color=self.colors_conscientiousness)
        self.axes_Conscientiouseness.set_xlim(left=0, right=5)
        self.axes_Conscientiouseness.set_yticks(self.y_pos4)
        self.axes_Conscientiouseness.set_yticklabels(self.data_y5, fontsize=8, fontname="Tw Cen MT")

        "Gambar grafik yang sisi kanan paling bawah  "
        self.data_y6 = ['Aesthetic Appreciation',
                        'Inquitiveness',
                        'Creativity',
                        'Unconventionality']
        self.y_pos6 = self.np.arange(len(self.data_y6))
#         self.value6 = [5, 2, 3, 4]
        self.value6=[nilai_sub_dimensi["Aesthetic Appreciation"],
                     nilai_sub_dimensi["Inquisitiveness"],
                     nilai_sub_dimensi["Creativity"],
                     nilai_sub_dimensi["Unconventionality"]]
        self.axes_Openess_To_Experience.barh(self.y_pos6,
                         self.value6,
                         align='center',
                         color=self.colors_openness_to_experience)
        self.axes_Openess_To_Experience.set_xlim(left=0, right=5)
        self.axes_Openess_To_Experience.set_yticks(self.y_pos6)
        self.axes_Openess_To_Experience.set_yticklabels(self.data_y6, fontsize=8, fontname="Tw Cen MT")

#         self.parent.Fit()
#         self.parent.GrafikMatplotlib.Fit()
        pass


class Colour(object):

    
    def __init__(self):
        self.colors_6_dimensi = ["r", "g", "b", "m", "purple", "y", "grey"]
        self.colors_honesty_humility = ["r","r","r","r","r"]
        self.colors_emotionality = ["g","g","g","g","g"]
        self.colors_extraversion = ["b","b","b","b","b"]
        self.colors_agreeableness = ["m","m","m","m","m"]
        self.colors_conscientiousness = ["purple","purple","purple","purple","purple"]
        self.colors_openness_to_experience = ["y","y","y","y","y"]
        self.colors_interstitial = ["grey","grey","grey","grey","grey"]
        pass

 
from coreapps.views.grafik_terpisah import GrafikFrame

class GrafikO(GrafikFrame,Colour):
        
    def __init__(self, parent):
        super().__init__(parent)
        ''' buat konstruktor parent '''
        self.parent = parent
        
        ''' konstruktor grafik dan membuat grafik '''
        self.matplotlib = matplotlib
        self.np = np
        self.plt = plt
        self.figure = Figure(figsize=(2,2))
        self.axes_grafik_o = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.m_Grafik_Terpisah,-1,self.figure)
        self.sizer32 = wx.BoxSizer(wx.VERTICAL)
        self.sizer32.Add(self.canvas, 1, wx.ALL | wx.EXPAND)
        self.m_Grafik_Terpisah.SetSizer(self.sizer32)
        
        ' Data diambil dari parent '
        nilai_dimensi = self.parent.hasil_dimensi
        nilai_sub_dimensi = self.parent.hasil_subdimensi
#         print (self.nilai_sub_dimensi)
        self.value = ('Aesthetic Appreciation', 'Inquisitiveness', 'Creativity', 'Unconventionality')
        self.performance =(nilai_sub_dimensi["Aesthetic Appreciation"],
                     nilai_sub_dimensi["Inquisitiveness"],
                     nilai_sub_dimensi["Creativity"],
                     nilai_sub_dimensi["Unconventionality"])
        self.y_pos = self.np.arange(len(self.value))
        self.color = Colour()
        self.color.colors_openness_to_experience
        self.ax = self.axes_grafik_o.bar(self.y_pos, self.performance, width = 0.3,
                align='center',
                color=self.color.colors_openness_to_experience)
  
#           Fungsi untuk menampilkan label di dalam Bar
        def autolabel(rects):
            """
            Attach a text label above each bar displaying its height
            """
            
            for rect in rects:
                height = rect.get_height()
                frac_height = height/5
                if frac_height > 0.95 :
                    label_position = height - (0.1 * height)
                else :
                    label_position = height + (0.1 * height)
                self.axes_grafik_o.text(rect.get_x() + rect.get_width()/2.,label_position,
                        '{}' .format(round(height,2)),
                        ha='center', va='bottom')
        autolabel(self.ax)
        self.axes_grafik_o.set_xticks(self.y_pos)
        self.axes_grafik_o.set_xticklabels(self.value)
#         self.axes_grafik_o.set_xlabel('Sub Dimensi')
        self.axes_grafik_o.set_ylim(bottom=0,top=5 )
        self.axes_grafik_o.set_title('Dimensi Openess To Experience Domain',
                                        fontname="Tw Cen MT",
                                        fontsize=12)
        self.figure.subplots_adjust(bottom=None,
                                    left=None,
                                    top = None,
                                    right=None,
                                    wspace = None,
                                    hspace = None)     
        self.Update()
        self.Refresh()
        self.Layout()
        
        'Penyajian definisi ke dalam grafik'
        select = self.parent.m_choice1.GetSelection()
        self.jenis_kelamin = self.parent.m_choice1.GetString(select)
        for k,v in nilai_dimensi.items():
            nilai_sub_dimensi[k]=round(v,2)
#         print ("Nilai Total dimensi + sub dimensi {} {}".format(nilai_dimensi,nilai_sub_dimensi))
#         print (self.jenis_kelamin)
        self.definisi = rerata2(self.jenis_kelamin,nilai_sub_dimensi)
        print ("ini mulai dari sini")
        print (self.definisi)
        dimensi = ["Aesthetic Appreciation",
                   "Inquisitiveness",
                   "Creativity",
                   "Unconventionality",
                   "Openness to Experience"]
        self.data = []
        for k in self.definisi:
            for dim in dimensi:
                if k[0] == dim:
                    self.data.append([k[0],k[3],k[1],k[2]])
#         print ("data ini {}".format(self.data))
        self.insert_value_list(self)


class GrafikC(GrafikFrame):
    
    def __init__(self, parent):
        super(GrafikC,self).__init__(parent)
        'buat konstruktor parent'
        self.parent = parent

        ''' konstruktor grafik dan membuat grafik '''
        self.matplotlib = matplotlib
        self.np = np
        self.plt = plt
        self.figure = Figure(figsize=(2,2))
#         self.figure.tight_layout()           
        self.axes_grafik_o = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.m_Grafik_Terpisah,-1,self.figure)
        self.sizer32 = wx.BoxSizer(wx.VERTICAL)
        self.sizer32.Add(self.canvas, 1, wx.ALL | wx.EXPAND)
        self.m_Grafik_Terpisah.SetSizer(self.sizer32)
        
        'Data diambil dari parent'
        nilai_dimensi = self.parent.hasil_dimensi
        nilai_sub_dimensi = self.parent.hasil_subdimensi
        self.value = ('Organization', 'Diligence', 'Perfectionism', 'Prudence')
        self.y_pos = self.np.arange(len(self.value))
#         self.performance = 3 + 10 * self.np.random.rand(len(self.value))
        self.performance = [nilai_sub_dimensi["Organization"],
                       nilai_sub_dimensi["Diligence"],
                       nilai_sub_dimensi["Perfectionism"],
                       nilai_sub_dimensi["Prudence"]]
#         #error = self.np.random.rand(len(self.value))
        self.color = Colour()
        self.color.colors_conscientiousness
        self.ax = self.axes_grafik_o.bar(self.y_pos, self.performance, width = 0.4,align='center',
                color=self.color.colors_conscientiousness)

        'Fungsi untuk menampilkan label di dalam Bar'
        def autolabel(rects):
            """
            Attach a text label above each bar displaying its height
            """
            
            for rect in rects:
                height = rect.get_height()
                frac_height = height/5
                if frac_height > 0.95 :
                    label_position = height - (0.1 * height)
                else :
                    label_position = height + (0.1 * height)
                self.axes_grafik_o.text(rect.get_x() + rect.get_width()/2.,label_position,
                        '{}' .format(round(height,2)),
                        ha='center', va='bottom')
        autolabel(self.ax)
        self.axes_grafik_o.set_xticks(self.y_pos)
        self.axes_grafik_o.set_xticklabels(self.value)
#         self.axes_grafik_o.set_xlabel('Sub Dimensi')
        self.axes_grafik_o.set_ylim(bottom=0,top=5 )
        self.axes_grafik_o.set_title('Dimensi Conscientiousness Domain',
                                        fontname="Tw Cen MT",
                                        fontsize=12)
        self.figure.subplots_adjust(bottom=None,
                                    left=None,
                                    top = None,
                                    right=None,
                                    wspace = None,
                                    hspace = None)     
        self.Update()
        self.Refresh()
        self.Layout()

        'Penyajian definisi ke dalam grafik'
        select = self.parent.m_choice1.GetSelection()
        self.jenis_kelamin = self.parent.m_choice1.GetString(select)
        print (self.jenis_kelamin)
        nilai_dimensi
        nilai_sub_dimensi
        for k,v in nilai_dimensi.items():
            nilai_sub_dimensi[k]=round(v,2)
#         print (nilai_sub_dimensi)
#         print (type(self.jenis_kelamin))
        self.definisi = rerata2(self.jenis_kelamin,nilai_sub_dimensi)
        dimensi = ['Organization',
                   'Diligence',
                   'Perfectionism',
                   'Prudence',
                   'Conscientiousness']
        self.data = []
        print (self.definisi)
        for k in self.definisi:
            for dim in dimensi:
                if k[0] == dim:
#                     print ("lolos")
#                     print (k)
#                     print(k[0])
#                     print(dimensi[0])
                    self.data.append([k[0],k[3],k[1],k[2]])
        self.insert_value_list(self)           

class GrafikA(GrafikFrame):
    
    def __init__(self, parent):
        super(GrafikA,self).__init__(parent)
#         buat konstruktor
        self.parent = parent
        self.matplotlib = matplotlib
        self.np = np
        self.plt = plt

        self.figure = Figure(figsize=(2,2))
        self.figure.subplots_adjust(bottom=None,
                                    left=None,
                                    top = None,
                                    right=0.975,
                                    wspace = 0.3,
                                    hspace = None)     
#         self.figure.tight_layout()           
        
        self.axes_grafik_o = self.figure.add_subplot(111)
        
#         Menambah jumlah grafik di sisi sebelah kanan
#         self.axes_Interestial_Scale = self.figure.add_subplot(7, 2, 14)

        self.canvas = FigureCanvas(self.m_Grafik_Terpisah,-1,self.figure)
        
        self.sizer32 = wx.BoxSizer(wx.VERTICAL)
        self.sizer32.Add(self.canvas, 1, wx.ALL | wx.EXPAND)
        self.m_Grafik_Terpisah.SetSizer(self.sizer32)
  
        
        # Example data
        nilai_dimensi = self.parent.hasil_dimensi
        nilai_sub_dimensi = self.parent.hasil_subdimensi
#       
        self.value = ["Forgiveness",
                        "Gentleness",
                        "Flexibility",
                        "Patience"]
        self.y_pos = self.np.arange(len(self.value))
#         self.performance = 3 + 10 * self.np.random.rand(len(self.value))
        self.performance = [nilai_sub_dimensi["Forgiveness"],
                       nilai_sub_dimensi["Gentleness"],
                       nilai_sub_dimensi["Flexibility"],
                       nilai_sub_dimensi["Patience"]]
 
 
        self.color = Colour()
        self.color.colors_agreeableness           
        self.ax = self.axes_grafik_o.bar(self.y_pos, self.performance,  width = 0.4,align='center',
                color=self.color.colors_agreeableness)

#           Fungsi untuk menampilkan label di dalam Bar
        def autolabel(rects):
            """
            Attach a text label above each bar displaying its height
            """
            
            for rect in rects:
                height = rect.get_height()
                frac_height = height/5
                if frac_height > 0.95 :
                    label_position = height - (0.1 * height)
                else :
                    label_position = height + (0.1 * height)
                self.axes_grafik_o.text(rect.get_x() + rect.get_width()/2.,label_position,
                        '{}' .format(round(height,2)),
                        ha='center', va='bottom')
        
        autolabel(self.ax)

        self.axes_grafik_o.set_xticks(self.y_pos)
        self.axes_grafik_o.set_xticklabels(self.value)
#         self.axes_grafik_o.set_xlabel('Sub Dimensi')
        self.axes_grafik_o.set_ylim(bottom=0,top=5 )
        self.axes_grafik_o.set_title('Dimensi Agreeableness Domain',
                                        fontname="Tw Cen MT",
                                        fontsize=12)       
        self.Update()
        self.Refresh()
        self.Layout()

#         Penyajian definisi ke dalam grafik

        select = self.parent.m_choice1.GetSelection()
        self.jenis_kelamin = self.parent.m_choice1.GetString(select)
        print (self.jenis_kelamin)
        nilai_dimensi
        nilai_sub_dimensi
        
        for k,v in nilai_dimensi.items():
            nilai_sub_dimensi[k]=round(v,2)
        
        print (nilai_sub_dimensi)
            
        print (type(self.jenis_kelamin))
        
        self.definisi = rerata2(self.jenis_kelamin,nilai_sub_dimensi)
        
 
        dimensi = [ "Agreeableness",
                    "Forgiveness",
                    "Gentleness",
                    "Flexibility",
                    "Patience"]
        
        self.data = []
        # print (self.definisi)
        for k in self.definisi:
            for dim in dimensi:
     
                if k[0] == dim:
                    # print ("lolos")
                    # print (k)
                    # print(k[0])
                    # print(dimensi[0])
                    self.data.append([k[0],k[3],k[1],k[2]])
        print (self.data)
        self.insert_value_list(self)

class GrafikEx(GrafikFrame):
        
    def __init__(self, parent):
        super(GrafikEx,self).__init__(parent)
        'buat konstruktor untuk parent'
        self.parent = parent

        'Konstruktr untuk grafik'
        self.matplotlib = matplotlib
        self.np = np
        self.plt = plt
        self.figure = Figure(figsize=(2,2))
        self.figure.subplots_adjust(bottom=None,
                                    left=None,
                                    top = None,
                                    right=0.975,
                                    wspace = 0.3,
                                    hspace = None)     
#         self.figure.tight_layout()           
        self.axes_grafik_o = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.m_Grafik_Terpisah,-1,self.figure)
        self.sizer32 = wx.BoxSizer(wx.VERTICAL)
        self.sizer32.Add(self.canvas, 1, wx.ALL | wx.EXPAND)
        self.m_Grafik_Terpisah.SetSizer(self.sizer32)
  
        'Data diambil dari parent'
        nilai_dimensi = self.parent.hasil_dimensi
        nilai_sub_dimensi = self.parent.hasil_subdimensi
        self.value = ["Social Self Esteem",
                        "Social Boldness",
                        "Sociability",
                        "Liveliness"]
        self.y_pos = self.np.arange(len(self.value))
        self.performance = [nilai_sub_dimensi["Social Self Esteem"],
                       nilai_sub_dimensi["Social Boldness"],
                       nilai_sub_dimensi["Sociability"],
                       nilai_sub_dimensi["Liveliness"]]
        self.color = Colour()
        self.color.colors_extraversion
        self.ax =  self.axes_grafik_o.bar(self.y_pos, self.performance, width = 0.4,align='center',
                color=self.color.colors_extraversion)
       
        'Fungsi untuk menampilkan label di dalam Bar'
        def autolabel(rects):
            """
            Attach a text label above each bar displaying its height
            """
            
            for rect in rects:
                height = rect.get_height()
                frac_height = height/5
                if frac_height > 0.95 :
                    label_position = height - (0.1 * height)
                else :
                    label_position = height + (0.1 * height)
                self.axes_grafik_o.text(rect.get_x() + rect.get_width()/2.,label_position,
                        '{}' .format(round(height,2)),
                        ha='center', va='bottom')
        autolabel(self.ax)
        self.axes_grafik_o.set_xticks(self.y_pos)
        self.axes_grafik_o.set_xticklabels(self.value)
        self.axes_grafik_o.set_ylim(bottom=0,top=5 )
#         self.axes_grafik_o.set_ylabel('Performance')
        self.axes_grafik_o.set_title('Dimensi  Extraversion Domain')
        self.Update()
        self.Refresh()
        self.Layout()

        'Penyajian definisi ke dalam grafik'
        select = self.parent.m_choice1.GetSelection()
        self.jenis_kelamin = self.parent.m_choice1.GetString(select)
#         print (self.jenis_kelamin)
#         nilai_dimensi
#         nilai_sub_dimensi
        for k,v in nilai_dimensi.items():
            nilai_sub_dimensi[k]=round(v,2)
#         print (nilai_sub_dimensi)
#         print (type(self.jenis_kelamin))
        self.definisi = rerata2(self.jenis_kelamin,nilai_sub_dimensi)
        dimensi = [ "Social Self Esteem",
                    "Social Boldness",
                    "Sociability",
                    "Liveliness",
                    "Extraversion"]
        
        self.data = []
        print (self.definisi)
        for k in self.definisi:
            for dim in dimensi:
     
                if k[0] == dim:
#                     print ("lolos")
#                     print (k)
#                     print(k[0])
#                     print(dimensi[0])
                    self.data.append([k[0],k[3],k[1],k[2]])
            
        self.insert_value_list(self)

class GrafikEm(GrafikFrame):
        
    def __init__(self, parent):
        super(GrafikEm,self).__init__(parent)
        'buat konstruktor parent'
        self.parent = parent
        
        'Buat konstruktor grafik terpisah'
        self.matplotlib = matplotlib
        self.np = np
        self.plt = plt
        self.figure = Figure(figsize=(2,2))
        self.figure.subplots_adjust(bottom=None,
                                    left=None,
                                    top = None,
                                    right=0.975,
                                    wspace = 0.3,
                                    hspace = None)     
#         self.figure.tight_layout()           
        self.axes_grafik_o = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.m_Grafik_Terpisah,-1,self.figure)
        self.sizer32 = wx.BoxSizer(wx.VERTICAL)
        self.sizer32.Add(self.canvas, 1, wx.ALL | wx.EXPAND)
        self.m_Grafik_Terpisah.SetSizer(self.sizer32)
  
        'Data diambil dari parent'
        nilai_dimensi = self.parent.hasil_dimensi
        nilai_sub_dimensi = self.parent.hasil_subdimensi
        self.value = ["Fearfullness",
                      "Anxiety",
                      "Dependence",
                      "Sentimentality"]
        self.y_pos = self.np.arange(len(self.value))
        self.performance =(nilai_sub_dimensi["Fearfullness"],
                     nilai_sub_dimensi["Anxiety"],
                     nilai_sub_dimensi["Dependence"],
                     nilai_sub_dimensi["Sentimentality"])
        self.color = Colour()
        self.ax = self.axes_grafik_o.bar(self.y_pos, self.performance,  width = 0.4,align='center',
                color=self.color.colors_emotionality)

        'Fungsi untuk menampilkan label di dalam Bar'
        def autolabel(rects):
            """
            Attach a text label above each bar displaying its height
            """
            
            for rect in rects:
                height = rect.get_height()
                frac_height = height/5
                if frac_height > 0.95 :
                    label_position = height - (0.1 * height)
                else :
                    label_position = height + (0.1 * height)
                self.axes_grafik_o.text(rect.get_x() + rect.get_width()/2.,label_position,
                        '{}' .format(round(height,2)),
                        ha='center', va='bottom')
        autolabel(self.ax)
        self.axes_grafik_o.set_xticks(self.y_pos)
        self.axes_grafik_o.set_xticklabels(self.value)
        self.axes_grafik_o.set_ylim(bottom=0,top=5 )
        self.axes_grafik_o.set_title('Dimensi Emotionality Domain')
        self.Update()
        self.Refresh()
        self.Layout()
 
        'Penyajian definisi ke dalam grafik'
        select = self.parent.m_choice1.GetSelection()
        self.jenis_kelamin = self.parent.m_choice1.GetString(select)
        print (self.jenis_kelamin)
        for k,v in nilai_dimensi.items():
            nilai_sub_dimensi[k]=round(v,2)
#         print (nilai_sub_dimensi)
#         print (type(self.jenis_kelamin))
        self.definisi = rerata2(self.jenis_kelamin,nilai_sub_dimensi)
        dimensi = ["Fearfullness",
                   "Anxiety",
                   "Dependence",
                   "Sentimentality",
                   "Emotionality"]
        self.data = []
#         print (self.definisi)
        for k in self.definisi:
            for dim in dimensi:
                if k[0] == dim:
#                     print ("lolos")
#                     print (k)
#                     print(k[0])
#                     print(dimensi[0])
                    self.data.append([k[0],k[3],k[1],k[2]])
        self.insert_value_list(self)
       
   
class GrafikH(GrafikFrame):
        
    def __init__(self, parent):
        super(GrafikH,self).__init__(parent)
        'buat konstruktor untuk parent'
        self.parent = parent
        
        'buat konstruktor untuk grafik terpisah'
        self.matplotlib = matplotlib
        self.np = np
        self.plt = plt
        self.figure = Figure(figsize=(2,2))
        self.figure.subplots_adjust(bottom=None,
                                    left=None,
                                    top = None,
                                    right=0.975,
                                    wspace = 0.3,
                                    hspace = None)     
#         self.figure.tight_layout()           
        self.axes_grafik_o = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.m_Grafik_Terpisah,-1,self.figure)
        self.sizer32 = wx.BoxSizer(wx.VERTICAL)
        self.sizer32.Add(self.canvas, 1, wx.ALL | wx.EXPAND)
        self.m_Grafik_Terpisah.SetSizer(self.sizer32)
  
        'Data diambil dari parent'
        nilai_dimensi = self.parent.hasil_dimensi
        nilai_sub_dimensi = self.parent.hasil_subdimensi
        self.value = ["Sincerity",
                      "Fairness",
                      "Greed Avoidance",
                      "Modesty"]
        self.y_pos = self.np.arange(len(self.value))
        self.performance =(nilai_sub_dimensi["Sincerity"],
                     nilai_sub_dimensi["Fairness"],
                     nilai_sub_dimensi["Greed Avoidance"],
                     nilai_sub_dimensi["Modesty"])
        self.color = Colour()
        self.ax  = self.axes_grafik_o.bar(self.y_pos, self.performance, width = 0.4,align='center',
                color=self.color.colors_honesty_humility)

        'Fungsi untuk menampilkan label di dalam Bar'
        def autolabel(rects):
            """
            Attach a text label above each bar displaying its height
            """
            
            for rect in rects:
                height = rect.get_height()
                frac_height = height/5
                if frac_height > 0.95 :
                    label_position = height - (0.1 * height)
                else :
                    label_position = height + (0.1 * height)
                self.axes_grafik_o.text(rect.get_x() + rect.get_width()/2.,label_position,
                        '{}' .format(round(height,2)),
                        ha='center', va='bottom')
        autolabel(self.ax)
        self.axes_grafik_o.set_xticks(self.y_pos)
        self.axes_grafik_o.set_xticklabels(self.value)
#         self.axes_grafik_o.set_ylabel('Performance')
        self.axes_grafik_o.set_ylim(bottom=0,top=5 )
        self.axes_grafik_o.set_title('Dimensi Honesty and Humility Domain')
        self.Update()
        self.Refresh()
        self.Layout()        

        'Penyajian definisi ke dalam grafik'
        select = self.parent.m_choice1.GetSelection()
        self.jenis_kelamin = self.parent.m_choice1.GetString(select)
#         print (self.jenis_kelamin)
        for k,v in nilai_dimensi.items():
            nilai_sub_dimensi[k]=round(v,2)
#         print (nilai_sub_dimensi)
#         print (type(self.jenis_kelamin))
        self.definisi = rerata2(self.jenis_kelamin,nilai_sub_dimensi)
        dimensi = ["Honesty & Humility",
                   "Sincerity",
                   "Fairness",
                   "Greed Avoidance",
                   "Modesty"]
        self.data = []
#         print (self.definisi)
        for k in self.definisi:
            for dim in dimensi:
                if k[0] == dim:
#                     print ("lolos")
#                     print (k)
#                     print(k[0])
#                     print(dimensi[0])
                    self.data.append([k[0],k[3],k[1],k[2]])
        self.insert_value_list(self)
 

class GrafikIA(GrafikFrame):
    
    
    def __init__(self, parent):
        super(GrafikIA,self).__init__(parent)
        'buat konstruktor parent'
        self.parent = parent
        
        'buat konstruktor grafik terpisah'
        self.matplotlib = matplotlib
        self.np = np
        self.plt = plt
        self.figure = Figure(figsize=(2,2))
        self.figure.subplots_adjust(bottom=None,
                                    left=None,
                                    top = None,
                                    right=0.975,
                                    wspace = 0.3,
                                    hspace = None)     
#         self.figure.tight_layout()           
        self.axes_grafik_o = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.m_Grafik_Terpisah,-1,self.figure)
        self.sizer32 = wx.BoxSizer(wx.VERTICAL)
        self.sizer32.Add(self.canvas, 1, wx.ALL | wx.EXPAND)
        self.m_Grafik_Terpisah.SetSizer(self.sizer32)

        'Data diambil dari parent'
        nilai_dimensi = self.parent.hasil_dimensi
        nilai_sub_dimensi = self.parent.hasil_subdimensi
        self.value = ["Interstitial"]
        self.y_pos = self.np.arange(len(self.value))
        self.performance =(nilai_sub_dimensi["Interstitial"]) 
        
        self.color = Colour()
        self.ax = self.axes_grafik_o.bar(self.y_pos, self.performance, width = 0.4,align='center',
                color=self.color.colors_interstitial)
        
        'Fungsi untuk menampilkan label di dalam Bar'
        def autolabel(rects):
            """
            Attach a text label above each bar displaying its height
            """
            
            for rect in rects:
                height = rect.get_height()
                frac_height = height/5
                if frac_height > 0.95 :
                    label_position = height - (0.1 * height)
                else :
                    label_position = height + (0.1 * height)
                self.axes_grafik_o.text(rect.get_x() + rect.get_width()/2.,label_position,
                        '{}' .format(round(height,2)),
                        ha='center', va='bottom')
        autolabel(self.ax)
        self.axes_grafik_o.set_xticks(self.y_pos)
        self.axes_grafik_o.set_xticklabels(self.value)
#         self.axes_grafik_o.set_ylabel('Performance')
        self.axes_grafik_o.set_ylim(bottom=0,top=5 )
        self.axes_grafik_o.set_title('Dimensi Interstitial Domain')
        self.Update()
        self.Refresh()
        self.Layout()
        
        'Penyajian definisi ke dalam grafik'
        select = self.parent.m_choice1.GetSelection()
        self.jenis_kelamin = self.parent.m_choice1.GetString(select)
        for k,v in nilai_dimensi.items():
            nilai_sub_dimensi[k]=round(v,2)
#         print (nilai_sub_dimensi)
#         print (type(self.jenis_kelamin))
        self.definisi = rerata2(self.jenis_kelamin,nilai_sub_dimensi)
        dimensi = ["Interstitial"]
        self.data = []
#         print (self.definisi)
        for k in self.definisi:
            for dim in dimensi:
                if k[0] == dim:
#                     print ("lolos")
#                     print (k)
#                     print(k[0])
#                     print(dimensi[0])
                    self.data.append([k[0],k[3],k[1],k[2]])
        self.insert_value_list(self)

if __name__ == "__main__":
    app = GrafikDimensi()
    app.draw()
    
