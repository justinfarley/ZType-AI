from PIL import Image
from pytesseract import pytesseract
import pyautogui as py

path_to_tesseract = 'C:\\Users\\j\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

imagesPath = 'C:\\Users\\j\\source\\repos\\ZType AI\\ZType-AI\\images\\'

image = imagesPath + 'test.png'

img = Image.open(image)

text = pytesseract.image_to_string(img)




py.write(text, interval=0.05)