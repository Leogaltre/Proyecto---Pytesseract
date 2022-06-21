import cv2
import pytesseract

# Test 1 Pasado

pytesseract.pytesseract.tesseract_cmd = r'C:\1A- Leo\Software 4\Tesseract-OCR\tesseract'

# image = cv2.imread('t1.png')
# img = cv2.resize(image, (500, 778))
img = cv2.imread('t2.png')
text = pytesseract.image_to_string(img, lang='spa')
print('Texto: ', text)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()