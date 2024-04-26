# Libraries
from PIL import Image
import cv2
import pytesseract

# BASIC WORKFLOW: 
    # Open an image using Pillow
    # Modify the image using openCV, for instance, binarize it and turn it to grayscale
    # Deliver the modified image to pytesseract to turn the image into plain text

#FUNCTIONS
# Inverting images with OpenCV
def invert(img):
    process = "invert"
    inverted_image = cv2.bitwise_not(img)
    cv2.imwrite(f'temp/{process}.jpg', inverted_image)
    temp_file = f'temp/{process}.jpg'
    temp = cv2.imread(temp_file)
    #cv2.imshow("Inverted Image", temp)
    #cv2.waitKey(1000)
    return img

#Binarize
def binarize(img):
    process = "binarize"
    binarize_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    binarize_image = cv2.adaptiveThreshold(binarize_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite("temp/binarize.jpg", binarize_image)
    temp_file = f'temp/{process}.jpg'
    temp = cv2.imread(temp_file)
    #cv2.imshow("Binarize Image", temp)
    #cv2.waitKey(1000)
    return img

def xnoise(img):
    process = "xnoise"
    xnoise_image = cv2.fastNlMeansDenoising(img, 7, 21)
    cv2.imwrite("temp/xnoise.jpg", xnoise_image)
    temp_file = f'temp/{process}.jpg'
    temp = cv2.imread(temp_file)
    #cv2.imshow("Xnoise Image", temp)
    #cv2.waitKey(1000)
    return img



# Manipulating images with PIL
#im = Image.open(image_file)
#template = im.copy()
#width, height = template.size
#pixels = template.load()
#for i in range(width):
#    for j in range(height):
#        r, g, b, p= template.getpixel((i,j))
#        grayscale = (0.299*r + 0.587*g + 0.114*b)
#        pixels[i, j] = (int(grayscale), int(grayscale), int(grayscale))
# Manipulating images with OpenCV

def main():
    process=''
    image_name = input("What is the name of your image?")
    image_file = (f"ImagesIn/{image_name}")
    temp_file = f'temp/{process}.jpg'
    img = cv2.imread(image_file)
    #cv2.imshow("original image", img)
    #cv2.waitKey(0)

    Qinput = input('Would you like to invert your image? y/n ')
    if Qinput == 'y':
        invert(img)
    else:
        pass
    # Binarize images with OpenCV

    Qgray = input('Would you like to binarize your image? y/n ')
    if Qgray == 'y':
        binarize(img)

    # Remove noise from images with OpenCV

    Qnoise = input("Would you like to remove noise from your image? y/n ")
    if Qnoise == 'y':
        xnoise(img)
        binarize(img)

    #Put the modified image through Pytesseract to OCR it!
    QOCR = input("Would you like to OCR your image? y/n ")
    if QOCR == 'y':
        ocr_result = pytesseract.image_to_string(img)
        
        print(ocr_result)
        QLike = input("Did you like the result? y/n ")
        if QLike == 'y':
            text_file = open(f'OCR_Text\{image_name}.txt', 'w')
            text_file.write(ocr_result)
        pass

if __name__ == '__main__':
    main()
    #template.save('ImagesOut/AlteredImage.png')
    #result = Image.open("ImagesOut/AlteredEmail.png")
    #result.show()