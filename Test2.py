import cv2
import pytesseract

# Test 1 Pasado

pytesseract.pytesseract.tesseract_cmd = r'C:\1A- Leo\Software 4\Tesseract-OCR\tesseract'

image = cv2.imread('placas.png')
img = cv2.resize(image, (600, 600))
text = pytesseract.image_to_string(img, lang='spa')
print('Texto: ', text)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()