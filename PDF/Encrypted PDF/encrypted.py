import PyPDF2
pdfFile = open('meetingminutes.pdf','rb')
pdfReader = PyPDF2.PdfReader(pdfFile)
pdfWriter = PyPDF2.PdfWriter()

for pageNum in range(len(pdfReader.pages)):
    pdfWriter.add_page(pdfReader.pages[pageNum])

pdfWriter.encrypt('swordfish')
resultPdf = open('encryptedminutes.pdf','wb')
pdfWriter.write(resultPdf)
resultPdf.close()
