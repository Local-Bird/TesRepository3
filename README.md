# TesRepository3
## Core.py
This is the file from which we derive all of the essential preprocessing and OCR functions. 

### Functions and their Recommended Uses
In it, we define the invert(), binarize(), and xnoise() functions, which are all used for preprocessing. As one may guess, invert() inverts the colors of an image, changing whites to blacks and so forth---this is often unnecessary for quality OCR now, but may still be advisable just in case. The binarize() function binarizes an image, or turns it to black and white---this is often an essential step in preprocessing and is recommended for all images. However, for some photos with highly variable lighting but clear text it is unadvisable, and instead best to go straight to OCR. The xnoise() function removes noise from the image, but in doing so makes the text considerably thinner---use this if the binarized image has many stray pixels around the text.

### Running Core.py
If a user runs this file, they will first be asked what language they are working with, then the name of their image. Having given both of these, they will then be guided through each option involved in preprocessing, asking whether they would like to perform certain changes to the image. Use this to acquire more faovrable OCR results when the usual binarize()-->OCR pipeline is not producing the desired text. Consider skipping all functions except OCR if the image is fairly clean, but with uneven lighting. Remove noise if the binarize function yields a lot of pixels around the text.

## Fast.py
This file allows users to iterate over every image in a given directory, quickly producing OCR for each without necessitating further input in between. Like Core.py, the user will first be asked which language they are working with. Then, they will be asked what speed they want to go, fast or superfast. The former allows the user to check each image's OCR for quality before saving it by inputting y/n in response to the printed results, while the latter will simply iterate over each image and automatically save the resulting text file.
