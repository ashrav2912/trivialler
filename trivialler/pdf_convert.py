# importing modules
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from project import assistant_code

# creating a pdf file object

def convert_pdf(pdf_name, text, city_name):
    # initializing variables with values
    fileName = f'''{city_name}_itinerary.pdf'''
    documentTitle = 'itinerary'
    title = f'''Itinerary for {city_name}''' 
    # creating a pdf object
    pdf = canvas.Canvas(fileName)

    # setting the title of the document
    pdf.setTitle(documentTitle)
    # registering a external font in python
    pdfmetrics.registerFont(
        TTFont('abc', 'SakBunderan.ttf')
    )

    # creating the title by setting it's font 
    # and putting it on the canvas
    pdf.setFont('abc', 36)
    pdf.drawCentredString(300, 770, title)
    # colour and putting it on the canvas
    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("Courier-Bold", 24)
    # drawing a line
    pdf.line(30, 710, 550, 710)

    # creating a multiline text using
    # textline and for loop
    text = pdf.beginText(40, 680)
    text.setFont("Courier", 18)
    text.setFillColor(colors.red)
    


