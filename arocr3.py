import cv2
import numpy as np
import pytesseract
from PIL import Image
import arabic_reshaper
from bidi.algorithm import get_display


# read image using OpenCV
img = cv2.imread("arabic_image.jpg")

# convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# perform thresholding to make text more visible
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# perform morphological operations to remove noise
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# invert the image to make text black
invert = cv2.bitwise_not(morph)

# convert image to PIL format for use with pytesseract
pil_img = Image.fromarray(invert)

# perform OCR using pytesseract
text = pytesseract.image_to_string(pil_img, lang='ara')

# reshape the text to correct the Arabic text shaping
reshaped_text = arabic_reshaper.reshape(text)
display_text = get_display(reshaped_text)

# print the OCR result
print(display_text)
