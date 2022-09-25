import PyPDF2

# Open PDF file and read as binary

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    # get pdf page number
    print(reader.numPages)

   # rotate pdf
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
