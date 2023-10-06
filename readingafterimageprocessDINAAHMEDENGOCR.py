import pytesseract #OCR
from PIL import Image #For Image
import pyttsx3 #For Audio
from google.cloud import vision

image_file = "download (1).png"
no_noise="no_noise.png"
img=Image.open(no_noise)
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
ocr_result=pytesseract.image_to_string(img)
with open('abc.txt',mode ='w') as file:     
         file.write(ocr_result)
             
print(ocr_result) 
engine = pyttsx3.init()
  
# an audio will be played which speaks the test if pyttsx3 recognizes it
engine.say(ocr_result)                             
engine.runAndWait()

