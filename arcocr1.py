import io
import pytesseract #OCR
import cv2#image
import pyocr.builders
from PIL import Image #For Image
###image Processing techniques###############
image_file = "image.jpg"
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
# Initialize the OCR engine
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]

# Perform OCR on the image
text = tool.image_to_string(
        lang='ara',
        builder=pyocr.builders.TextBuilder(),
        config= "."
    )
#reshape_text=arabic_reshaper.reshape(ocr_result)
with open('abc.txt',mode ='w',encoding="utf-8") as fileX:     
         fileX.write(text)
             
print(text)