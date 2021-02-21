#Method Dos#
#For PyTesseract Config Details
#https://stackoverflow.com/questions/44619077/pytesseract-ocr-multiple-config-options/44632770
#https://stackoverflow.com/questions/46205514/highly-inconsistent-ocr-result-for-tesseract
from mtranslate import translate

import cv2
import os
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Path where the pdf-pic images are present. This is fed as input to the Image Processing Function and OCR
#FIGURE OUT HOW TO CALL THIS PROCESS for multiple images
import glob
import cv2

# img_path="C:/Users/HP/Documents/PDF_Reader/PDF Pages/PDF_1_Page_2.jpg"
images = [cv2.imread(file) for file in glob.glob("C:/Users/HP/Documents/PDF_Reader/PDF Pages/*.jpg")]
f_name = [file for file in glob.glob("C:/Users/HP/Documents/PDF_Reader/PDF Pages/*.jpg")]

# def get_strin(img_path):
def get_string(image,i):
    ### PART 1 ###
    # Read image using opencv

    # img = cv2.imread(img_path)

    # Extract the file name without the file extension
    # file_name = os.path.basename(img_path).split('.')[0]
    file_name = os.path.basename(f_name[i]).split('.')[0]
    file_name = file_name.split()[0]

    # Create a directory for outputs
    output_path = os.path.join("C:/Users/HP/Documents/PDF_Reader/Pdf Pages Filtered/", file_name)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ### PART 2 ###
    # Rescale the image, if needed.
    # img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    img = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)


    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    # Apply blur to smooth out the edges
    img = cv2.GaussianBlur(img, (5, 5), 0)
    sharpen_filter = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    img = cv2.filter2D(img, -1, sharpen_filter)

    # Apply threshold to get image with only b&w (binarization)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    ### PART 3 ###
    # Save the filtered image in the output directory
    save_path = os.path.join(output_path, file_name + "_filter_" + ".jpg")
    cv2.imwrite(save_path, img)

    # Recognize text with tesseract for python
    # --psm 6 Assume a single uniform block of text.
    result = pytesseract.image_to_string(img, lang="Malayalam", config='--psm 6')
    return result



#Print the raw Malaylam Text obtained
# print(get_string(img_path))
#Remove the for loop, and UNTAB the contents of the loop as well.
i = 0
for image in images:
    #Assign the malayalam text to this variable
    # input_to_translate = get_string(img_path).replace("\n","")
    input_to_translate = get_string(image, i).replace("\n", " ")

    #Write the Malayalam txt to a file
    with open('malayalam.txt', encoding='utf-8', mode ='a') as file:
        file.write("\n")
        file.write(input_to_translate)
        file.write("\n")

    with open('translated.txt', encoding ='utf-8',mode='a') as file:
        #print the translated text
        #print(translate(input_to_translate, 'mal', 'en'))
        file.write("\n")
        file.write(translate(input_to_translate, 'mal', 'en'))
        file.write("\n")
    i+=1

# -------------------------- # -------------------------- # ------------------------ # ---------------------- #

    # Method Uno#

    # # adds image processing capabilities
    # from PIL import Image
    #
    # # will convert the image to text string
    # import pytesseract
    #
    # # translates into preferred language
    # from googletrans import Translator
    #
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #
    # # assigning an image from the source path
    # img = Image.open('C:/Users/HP/Documents/PDF_Reader/Page_2.jpg')
    #
    # # converts the image to result and saves it into result variable
    # result = pytesseract.image_to_string(img, lang="Malayalam")
    #
    # p = Translator()
    # # translates the text into french language
    # k = p.translate(result, src='malayalam', dest='english')
    # #converts the result into string format
    # translated = str(k.text)
    #
    # with open('test.txt', mode ='w') as file:
    #   file.write(result)
    #   file.write("\n")
    #   file.write(translated)
    #   print("ready!")