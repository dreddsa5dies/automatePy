#! python

import PyPDF2

pdf = open('encrypted.pdf', 'rb')
pdfRead = PyPDF2.PdfFileReader(pdf)
if pdfRead.isEncrypted:
    # если зашифрован, то пароль
    pdfRead.decrypt('rosebud')
    for i in range(pdfRead.getNumPages()):
        data = pdfRead.getPage(i)
        print(data.extractText())
pdf.close()
