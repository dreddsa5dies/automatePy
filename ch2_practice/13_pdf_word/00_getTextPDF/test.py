#! python

import PyPDF2

pdf = open('meetingminutes.pdf', 'rb')
pdfRead = PyPDF2.PdfFileReader(pdf)
for i in range(pdfRead.getNumPages()):
    data = pdfRead.getPage(i)
    print(data.extractText())
pdf.close()
