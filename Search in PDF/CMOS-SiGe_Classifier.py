from PyPDF2 import PdfFileReader
from pathlib import Path
import re
import os 

CMOS_count = 0
SiGe_count = 0


pdffiles = str(input("Enter Paths(xxx.pdf,yyy.pdf,aaa.pdf): ")) #an automation should be considered for this part, such as: "cmos" + count + ".pdf"...
pdf_files = pdffiles.split(",")
pdf_files_absolute_path = []
for i in pdf_files:
    absolute_path = os.path.abspath(i)
    pdf_files_absolute_path.append(absolute_path)
for i in pdf_files_absolute_path:
    pdfpath = str(i)
    pdf = PdfFileReader(pdfpath)

    pages_sentences = []
    page_num = 1
    for page in pdf.pages:
        page_text = page.extractText()
        page_num = page_num + 1

    text = '\n'.join(pages_sentences)

    for page in pdf.pages:
        page_text = page.extractText()
        if "CMOS" in page_text:
            CMOS_count += 1
        elif "SiGe" in pdf.pages:
            SiGe_count += 1

    if SiGe_count != 0:
        if CMOS_count/SiGe_count >= 2:
            print("This amplifier build by using CMOS technique")
        elif CMOS_count/SiGe_count <= 0.5:
            print("This amplifier build by using SiGe technique")
        else:
            print("Bad written or unable to define")
    elif CMOS_count >= 2:
        print("This amplifier build by using CMOS technique")
    else:
        print("Bad written, not related or unable to define")