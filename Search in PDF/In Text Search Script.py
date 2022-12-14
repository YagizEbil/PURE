from PyPDF2 import PdfFileReader
from pathlib import Path
import re

count = 0
pdfpath = str(input("Enter PDF path: "))
pdf = PdfFileReader(pdfpath)
pdfsearch = input("What you want to search: ")
pages_sentences = []
page_num = 1
for page in pdf.pages:
    page_text = page.extractText()
    if pdfsearch in page_text:
        sentence_list = ["Page "+ str(page_num) + ': ' + sentence.replace('\n', '') for sentence in re.split('\.\W+|\?\W+|\!\W+', page_text) if pdfsearch in sentence][0]
        pages_sentences.append(sentence_list)
        count += 1
    page_num = int(page_num)
    page_num = page_num + 1

text = '\n'.join(pages_sentences)
with Path('CMOS_sentences_pages.text').open(mode='w') as output_file_3:
    output_file_3.write(text)
print("Number of searched text in document: ", count)