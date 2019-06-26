from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors

width, height = A4
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
styleN.alignment = TA_LEFT
styleBH = styles["Normal"]
styleBH.alignment = TA_CENTER

def coord(x, y, unit=1):
    x, y = x * unit, height -  y * unit
    return x, y

# Headers
hdescrpcion = Paragraph('''<b>descrpcion</b>''', styleBH)
hpartida = Paragraph('''<b>partida</b>''', styleBH)
hcandidad = Paragraph('''<b>candidad</b>''', styleBH)
hprecio_unitario = Paragraph('''<b>precio_unitario</b>''', styleBH)
hprecio_total = Paragraph('''<b>precio_total</b>''', styleBH)

# Texts
descrpcion = Paragraph('long paragsadfsdafsdfsdfsdfsdfsdfsdfsdfsdfsdfdsfdsfraph', styleN)
partida = Paragraph('1', styleN)
candidad = Paragraph('120', styleN)
precio_unitario = Paragraph('$52.00', styleN)
precio_total = Paragraph('$6240.00', styleN)

data= [[hdescrpcion, hcandidad,hcandidad, hprecio_unitario, hprecio_total],
       [partida, candidad, descrpcion, precio_unitario, precio_total]]

table = Table(data, colWidths=[2.05 * cm, 2.7 * cm, 5 * cm,
                               3* cm, 3 * cm])

table.setStyle(TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]))

c = canvas.Canvas("/home/cireng/Projects/pyhexaco/coreapps/controllers/reporting/a.pdf", pagesize=A4)
table.wrapOn(c, width, height)
table.drawOn(c, *coord(1.8, 9.6, cm))
c.save()