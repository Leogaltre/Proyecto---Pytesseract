import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\1A- Leo\Software 4\Para Python - Tesseract\tesseract.exe'

image = cv2.imread('IMG1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Dimensiones de la Laptop -> 1366 x 768
# Dimensiones de la Hoja tamaño carta 8.5 x 11

canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)

# Contornos
cnts = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]

image = cv2.resize(image, (556, 720))
canny = cv2.resize(canny, (556, 720))
gray = cv2.resize(canny, (556, 720))
for c in cnts:
    epsilon = cv2.arcLength(c, True)*0.02
    approx = cv2.approxPolyDP(c, epsilon, True) # Los vertices detectados
    print('Aprox', approx)
    if len(approx) >= 4:
        cv2.drawContours(image, [approx], 0, (255, 255, 0), 2)


cv2.imshow('Imagen', image)
cv2.waitKey(0)
cv2.imshow('Canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()