from PIL import Image
import cv2
import pytesseract
import os
from Core import invert, binarize
language = input("What language are you using?")
language = language[0:3].lower()

directory = r"C:\Users\john1\OneDrive\Desktop\CS32Project\TesRepository3\ImagesIn"+f'{language}'

for filename in os.listdir(directory):
    image_file = (f"ImagesIn{language}/{filename}")
    img = cv2.imread(image_file)

    invert(img)
    binarize(img)

    ocr_result = pytesseract.image_to_string(img,lang=f'{language}')
    print(ocr_result)
    text_file = open(f'OCR_Text\{filename}.txt', 'w', encoding='utf-8')
    text_file.write(ocr_result)