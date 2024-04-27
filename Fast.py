from PIL import Image
import cv2
import pytesseract
import os
from Core import invert, binarize, xnoise
language = input("What language are you using?")
language = language[0:3].lower()
speed = input("How fast would you like to go? Options: 'fast' or 'superfast'")
directory = r"C:\Users\john1\OneDrive\Desktop\CS32Project\TesRepository3\ImagesIn"+f'{language}'

for filename in os.listdir(directory):
    image_file = (f"ImagesIn{language}/{filename}")
    temp = Image.open(image_file)
    test = temp.getpixel((1,1))
    img = cv2.imread(image_file)
    wb = test[0] + test[1] + test[2]
    print(wb)

    if wb > 300:
        img = invert(img)
        img = binarize(img)

    ocr_result = pytesseract.image_to_string(img,lang=f'{language}')
    print(f"THIS IS {filename}", ocr_result)
    if speed == 'fast':
        save = input("Did you like the result?")
        if save == 'y':
            text_file = open(f'OCR_Text\{filename}.txt', 'w', encoding='utf-8')
            text_file.write(ocr_result)
        else:
            pass
    if speed == 'superfast':
        text_file = open(f'OCR_Text\{filename}.txt', 'w', encoding='utf-8')
        text_file.write(ocr_result)