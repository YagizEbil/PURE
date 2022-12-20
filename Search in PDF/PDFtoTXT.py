from PyPDF2 import PdfFileReader
from pathlib import Path

pdfpath = input("Enter PDF path: ")

pdf = PdfFileReader(pdfpath)

page_1_object = pdf.getPage(0) 
page_1_text = page_1_object.extractText()

with Path('file.txt').open(mode='w') as output_file: 
    text = ''
    for page in pdf.pages:
        text += page.extractText()
    output_file.write(text)
