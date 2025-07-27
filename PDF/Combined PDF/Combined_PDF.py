#! python3
#combinePDF.py

import PyPDF2,os

pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key/str.lower)

pdfWriter = PyPDF2.PdfWriter()

# Loop through all PDF files

for filename in pdfFiles:
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    # Loop through all pages except the 1st page

    for pageNum in range(1,len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]
        pdfWriter.add_page(pageObj)

pdfOutput = open('combined.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
