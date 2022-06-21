import cv2 #Opencv

# Identificador de figuras
image = cv2.imread('fig.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Para poder hacer el contorno
canny = cv2.Canny(gray, 10, 150)

# Para umbralizacion simple
cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# ---------------- Recorrer entre cada borde identificado
for c in cnts:
	cv2.drawContours(image, [c], 0, (255, 255, 0), 2)
	cv2.imshow('image', image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
