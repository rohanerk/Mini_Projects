import PyPDF2

    
minutesFile = open('meetingminutes.pdf','rb')
pdfFileReader = PyPDF2.PdfReader(minutesFile)

pdfWriter = PyPDF2.PdfWriter()

for i in range(len(pdfFileReader.pages)):
    page = pdfFileReader.pages[i]
    page.rotate(90)
    pdfWriter.add_page(page)

with open('newrotated.pdf','wb') as resultPdfFile:
    pdfWriter.write(resultPdfFile)

minutesFile.close()
    

       

    
