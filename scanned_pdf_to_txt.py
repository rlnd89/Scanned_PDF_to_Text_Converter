##################################################################################################################
## Scanned PDF to Text Converter
##################################################################################################################
##
## Readme:
## 
## Install pytesseract and pdf2image:
##     - pip install pytesseract
##     - pip install pdf2image
## 
## Troubleshooting errors for Windows users:
##     1) PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
##        	install poppler (in anaconda): conda install -c conda-forge poppler
##     
##     2) TesseractNotFoundError: tesseract is not installed or it's not in your PATH
##          #1: Download and install Tesseract OCR from: https://github.com/UB-Mannheim/tesseract/wiki
##          #2: After installing, find the folder "Tesseract-OCR" with "tesseract.exe" in it
##          #3: Copy the file location of "tesseract.exe" and set tesseract_cmd to this location, eg.: 
##              pt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
##                         
##################################################################################################################

### 1) Set parameters
# Import libraries  
from pdf2image import convert_from_path  # a wrapper to convert PDF to images
import pytesseract as pt                 # OCR tool to recognize and “read” the text embedded in images
import os                                # to use OS dependent functionality

# Locate tesseract
pt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Path of the pdf 
PDF_file = "D:\\PythonScripts\\Non-text-searchable.pdf"


### 2) Convert PDF to images
# Store all pages of the PDF in a variable 
pages = convert_from_path(PDF_file, dpi=200, size=(1654,2340)) 
  
# Counter to store images of each page of PDF to image 
image_counter = 1
  
# Iterate through all the pages
for page in pages: 
  
    # Declaring filename for each page of PDF as JPG: page_1.jpg, page_2.jpg ... 
    filename = "page_" + str(image_counter) + ".jpg"
      
    # Save the image of the page
    page.save(filename, 'JPEG') 
  
    # Increment the counter to update filename 
    image_counter += 1


### 3) - Read text from images using OCR ##
# Variable to get count of total number of pages 
filelimit = image_counter-1
  
# Creating a text file to write the output 
outfile = PDF_file.split('\\')[2].split('.')[0] + ".txt"
  
# Open the file in append mode so all contents of all images are added to the same file 
f = open(outfile, "a") 
  
# Iterate from 1 to total number of pages 
for i in range(1, filelimit + 1): 
  
    # Set filename to recognize text from: page_1.jpg, page_2.jpg ...
    filename = "page_" + str(i) + ".jpg"
          
    # Recognize the text as string in image using pytesseract
    text = str(((pt.image_to_string(filename))))
  
    # Replace hyphens with spaces at line endings if word not written fully
    text = text.replace('-\n', '')     
  
    # Write the processed text to file
    f.write(text)
    
    # Clean up: delete images
    os.remove(filename)
    
# Close the file
f.close()
