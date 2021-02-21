#pdf2image will need Poppler. Download Poppler and add the bin path to System Environment Variable Path
#https://stackoverflow.com/questions/18381713/how-to-install-poppler-on-windows
#Highest voted Answer
#http://blog.alivate.com.au/poppler-windows/

from PyPDF2 import PdfFileReader, PdfFileWriter
from pdf2image import convert_from_path

#CODE FOR PDF2IMAGE
pdfs = r"C:/Users/HP/Documents/PDF_Reader/നുറുങ്ങ് ഓർമ്മകൾ രണ്ടാം ഭാഗം.pdf"
pages = convert_from_path(pdfs, 350)

i = 1
for page in pages:
    image_name = "PDF_1_Page_0" + str(i) + ".jpg"
    page.save("C:/Users/HP/Documents/PDF_Reader/Pdf Pages/"+image_name, "JPEG")
    i = i+1
#Images will be created in your Project Path


#CODE FOR CAPTURING ENGLISH TEXT FROM PDF
# directory = "C:/Users/HP/Documents/PDF_Reader/നുറുങ്ങ് ഓർമ്മകൾ രണ്ടാം ഭാഗം.pdf"
# f = open(directory, 'rb')
# reader = PdfFileReader(f)
# contents = reader.getPage(0).extractText().split('\n')
# f.close()
# print(contents)