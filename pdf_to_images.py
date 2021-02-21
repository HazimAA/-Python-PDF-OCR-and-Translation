#pdf2image will need Poppler. Download Poppler and add the bin path to System Environment Variable Path
#https://stackoverflow.com/questions/18381713/how-to-install-poppler-on-windows
#Refer Highest voted Answer for clarity
#http://blog.alivate.com.au/poppler-windows/

from PyPDF2 import PdfFileReader, PdfFileWriter
from pdf2image import convert_from_path

#CODE FOR PDF2IMAGE
pdfs = r"##PATH WITH FILENAME##"
#SAMPLE ENTRY FOR pdfs VARIABLE
# pdfs = r"C:/Users/HP/Documents/PDF_Reader/##FILENAME##.pdf"
pages = convert_from_path(pdfs, 350)

i = 1
for page in pages:
    image_name = "PDF_1_Page_0" + str(i) + ".jpg"
    page.save("##UPDATE PATH VARIABLE##"+image_name, "JPEG")
    #SAMPLE ENTRY FOR PATH
    #page.save("C:/Users/HP/Documents/PDF_Reader/Pdf Pages/"+image_name, "JPEG")
    i = i+1
#Images will be created in your Project Path
