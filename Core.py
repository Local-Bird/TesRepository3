# Libraries
from PIL import Image
import cv2
import pytesseract

# BASIC WORKFLOW: 
    # Open an image using Pillow
    # Modify the image using openCV, for instance, binarize it and turn it to grayscale
    # Deliver the modified image to pytesseract to turn the image into plain text

process=''
image_file = "ImagesIn/GajaLakshmi.png"
temp_file = f'temp/{process}.jpg'
# Manipulating images with PIL
im = Image.open(image_file)
template = im.copy()
width, height = template.size
pixels = template.load()
for i in range(width):
    for j in range(height):
        r, g, b, p = template.getpixel((i,j))
        grayscale = (0.299*r + 0.587*g + 0.114*b)
        pixels[i, j] = (int(grayscale), int(grayscale), int(grayscale))
# Manipulating images with OpenCV
img = cv2.imread(image_file)
cv2.imshow("original image", img)
cv2.waitKey(0)

# Inverting images with OpenCV
def invert(img):
    process = "invert"
    temp_file = f'temp/{process}.jpg'
    inverted_image = cv2.bitwise_not(img)
    cv2.imwrite(f'temp/{process}.jpg', inverted_image)
    temp = cv2.imread(temp_file)
    cv2.imshow("Inverted Image", temp)
    cv2.waitKey(0)
    return
Qinput = input('Would you like to invert your image? y/n')
if Qinput == 'y':
    invert(img)

# Grayscale images with OpenCV
def grayscale(image):
    process = "grayscale"
    temp_file = f'temp/{process}.jpg'
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("temp/grayscale.jpg", grayscale_image)
    temp = cv2.imread(temp_file)
    cv2.imshow("Grayscale Image", temp)
    cv2.waitKey(0)
    return
Qgray = input('Would you like to grayscale your image? y/n')
if Qgray == 'y':
    grayscale(img)
#template.save('ImagesOut/AlteredImage.png')
#result = Image.open("ImagesOut/AlteredEmail.png")
#result.show()