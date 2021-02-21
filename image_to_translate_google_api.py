#For PyTesseract Config Details
#https://stackoverflow.com/questions/44619077/pytesseract-ocr-multiple-config-options/44632770
#https://stackoverflow.com/questions/46205514/highly-inconsistent-ocr-result-for-tesseract
from mtranslate import translate
import cv2
import os
import numpy as np
import pytesseract
import glob
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

images = [cv2.imread(file) for file in glob.glob("C:/Users/HP/Documents/PDF_Reader/PDF Pages/*.jpg")]
f_name = [file for file in glob.glob("C:/Users/HP/Documents/PDF_Reader/PDF Pages/*.jpg")]

def get_string(image,i):

    ### PART 1 ###
    # Read image using opencv

    # Extract the file name without the file extension
    file_name = os.path.basename(f_name[i]).split('.')[0]
    file_name = file_name.split()[0]

    # Create a directory for outputs
    output_path = os.path.join("C:/Users/HP/Documents/PDF_Reader/Pdf Pages Filtered/", file_name)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

        
    ### PART 2 ###
    # Rescale the image, if needed.
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



i = 0
for image in images:
    #Assign the malayalam text to this variable
    input_to_translate = get_string(image, i).replace("\n", " ")

    #Write the Malayalam txt to a file
    with open('malayalam.txt', encoding='utf-8', mode ='a') as file:
        file.write("\n")
        file.write(input_to_translate)
        file.write("\n")

    with open('translated.txt', encoding ='utf-8',mode='a') as file:
        file.write("\n")
        file.write(translate(input_to_translate, 'mal', 'en'))
        file.write("\n")
    i+=1
