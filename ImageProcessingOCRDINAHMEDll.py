
import cv2
import pytesseract
import numpy as np
from pytesseract import Output 
img_source = cv2.imread('download (1).png')
 
 
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
 
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
 
 
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
 
 
def canny(image):
    return cv2.Canny(image, 100, 200)
 
 
gray = get_grayscale(img_source)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray)
 
for img in [img_source, gray, thresh, opening, canny]:
    d = pytesseract.image_to_string(img)
    with open('abc.txt',mode ='w') as file:     
          file.write(str(d))
    print(d)
    # back to RGB
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
 
    
 
    
    cv2.waitKey(0)