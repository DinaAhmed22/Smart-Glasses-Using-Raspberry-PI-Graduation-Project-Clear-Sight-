
import cv2#image
import pytesseract#OCR
import pyttsx3 #For Audio
import numpy as np #hnst3mlha fe noise removal
from googletrans import Translator #cant work offline

#Openeing an Image with OpenCv########
image_file = "download (1).png"
img = cv2.imread(image_file)
####################Image Processing Techniques######################################    plt.show()
##Inverted############
inverted_image = cv2.bitwise_not(img)##Sora inverted
cv2.imwrite("inverted.png", inverted_image)#3mlnlha save fe folder b3d invert

####Binarization############
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = grayscale(img)
cv2.imwrite("gray.png", gray_image)
####################################################
thresh, im_bw = cv2.threshold(gray_image, 210, 230, cv2.THRESH_BINARY)
cv2.imwrite("bw_image.png", im_bw)
#######################Noise removal#######################
def noise_removal(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return (image)
no_noise = noise_removal(im_bw)
cv2.imwrite("no_noise.png", no_noise)
############Dilation and Erosion###############################
def thin_font(image):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2),np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image)
eroded_image = thin_font(no_noise)
cv2.imwrite("eroded_image.png", eroded_image)
##############################################################
def thick_font(image):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2),np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image)
dilated_image = thick_font(no_noise)
cv2.imwrite("dilated_image.jpg", dilated_image)
ocr_result = pytesseract.image_to_string(dilated_image, config='')
print(ocr_result)
####Translate from english to french#####################
translator=Translator()
translatedfr=translator.translate(ocr_result,dest='fr').text
print(translatedfr)
