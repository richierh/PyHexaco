#! /usr/bin/env python  

from fpdf import FPDF
import pathlib
import webbrowser



data_hasil_perhitungan = (
    {"Nama Biodata" : "andri","No Tes":"3351","Tanggal Tes":"20/06/201",
        "Jenis Kelamin":"Laki-Laki","Tanggal Lahir":"16/03/1995","Pendidikan Terakhir":"S1",
        "Jurusan Pendidikan":"Psikologi","Kota":"Jakarta",
        "Perusahaan / Instansi":"PT Cipta Semesta ALam","Posisi / Jabatan":"Senior IT"
        },
    {"Openness to Experience" : "2.6","Unconvenionality":"3.4","Creativity":"4.5","Inquisitiveness":"3.7","Aesthetic Appreciation":""},
    {"Conscientiousness":"4.5","Prudence":"1.6","Perfectionism":"3.6","Diligence":"3.2","Organization":"4.6"},
    {"Agreeableness":"3.55","Patience":"4.3","Flexibility":"2.8","Gentleness":"2.6","Forgiveness":"2.44"},
    {"Extraversion":"2.7","Liveliness":"4.9","Sociability":"4.2","Social Boldness":"2.56","Social Self Esteem":"2.33"},
    {"Emotionality":"1.5","Sentimentality":"2.55","Dependence":"3.7","Anxiety":"4.6","Fearfulness":"4.56"},
    {"Honesty & Humility" : "3.22","Modesty":"2.14","Greed Avoidance":"4.33","Fairness":"3.22","Sincerity":"2.66"},
    {"Interstitial":"3.2"}
)
# print(type(data_hasil_perhitungan))
# print(data_hasil_perhitungan[1].keys())




# pdf = FPDF()
# pdf.add_page()
# pdf.set_font('Arial', 'B', 16)
# image1="binadata.png"
# pdf1 = "tuto1.pdf"
# name_loc = str(pathlib.Path.cwd()/"coreapps/controllers/reporting")
# print (name_loc)
# pdf.image(name_loc+"/"+image1,x=30,y=10,w=50,h=25,type="PNG")
# position_x =40
# position_y =10
# pdf.cell(40, 10, 'Hello World!')
# pdf.cell(40, 10, 'Powered by FPDF.', 0, 1, 'L')

# # pdf.cell(position_x,position_y,"disini data dari binakarir akan di sajikan")
# pdf.output(name_loc+"/"+pdf1, 'F')


# Import FPDF class
from fpdf import FPDF
 
# Create instance of FPDF class
# Letter size paper, use inches as unit of measure
pdf=FPDF(format='letter', unit='in')
 
# Add new page. Without this you cannot create the document.
pdf.add_page()
 
# Remember to always put one of these at least once.
pdf.set_font('Times','',10.0) 
 
# Effective page width, or just epw

epw = pdf.w - 2*pdf.l_margin
print (pdf.l_margin)
 
# Set column width to 1/4 of effective page width to distribute content 
# evenly across table and page
col_width = epw/4
 
# Since we do not need to draw lines anymore, there is no need to separate
# headers from data matrix.
 
data = [['First name','Last name','Age','City'],
['Jule','Smith',34,'San Juan'],
['Mary','Ramos',45,'Orlando'],
['Carlson','Banks',19,'Los Angeles']
]
 
# Document title centered, 'B'old, 14 pt
pdf.set_font('Times','B',14.0) 
pdf.cell(epw, 0.0, 'Demographic data', align='C')
pdf.set_font('Times','',10.0) 
pdf.ln(0.5)
print (pdf.font_size)
# Text height is the same as current font size
th = pdf.font_size
 
for row in data:
    for datum in row:
        # Enter data in colums
        # Notice the use of the function str to coerce any input to the 
        # string type. This is needed
        # since pyFPDF expects a string, not a number.
        pdf.cell(col_width, th, str(datum), border=1)
 
    pdf.ln(th)
 
# Line break equivalent to 4 lines
pdf.ln(4*th)
 
pdf.set_font('Times','B',14.0) 
pdf.cell(epw, 0.0, 'With more padding', align='C')
pdf.set_font('Times','',10.0) 
pdf.ln(0.5)
 
# Here we add more padding by passing 2*th as height
for row in data:
    for datum in row:
        # Enter data in colums
        pdf.cell(col_width, 2*th, str(datum), border=1)
 
    pdf.ln(2*th)
 
pdf.output("tedst.pdf", 'F')
