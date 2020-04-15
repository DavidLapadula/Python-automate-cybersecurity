import os, PyPDF2
os.chdir(r"C:\Users\DavidLapadula\Downloads")

pdfFile = open("meetingminutes1.pdf",  "rb")

reader1 = PyPDF2.PdfFileReader(pdfFile)

page = reader1.getPage(0)
text = page.extractText()

writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

outputFile = open("combinedminutes.pdf", "wb")
writer.write(outputFile)

outputFile.close()
pdfFile.close()
