# Identificador de figuras
import cv2 #Opencv

image = cv2.imread('fig.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Para poder hacer el contorno
canny = cv2.Canny(gray, 10, 150)
# Para cuando la linea no es muy marcada (Trinagulo)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)

# Para umbralizacion simple
#_, th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# OpenCV 4
#cv2.drawContours(image, cnts, -1, (0,255,0), 2)

# ---------------- Recorrer entre cada borde identificado
for c in cnts:
	# Epsilon modifica la precision de los puntos de contorno más peque más preciso
	epsilon = 0.005*cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, epsilon, True)
	print(len(approx))

	#Colocar el texto para lo puntos resultantes
	# Posición (x,y), ancho() y alto()
	x,y,w,h = cv2.boundingRect(approx)

	''' Usaremos len(approx) para la identificación de 
	figuras de acuerdo a su numero de vertices obtenido'''

	if len(approx)==3:
		# cv2.putText(imagen, Nombre, Posicion)
		cv2.putText(image,'Triangulo', (x,y),1,1,(0,255,0),1)

	''' Identificar diferencias entre cuadrado y rectangulo
	aspect ratio = ancho(width)/alto(height) '''
	if len(approx)==4:
		aspect_ratio = float(w) / h
		# print('aspect_ratio= ', aspect_ratio)
		if aspect_ratio == 1:
			cv2.putText(image,'Cuadrado', (x,y-5 ),1,1,(0,255,0),1)
		else:
			cv2.putText(image,'Rectangulo', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==5:
		cv2.putText(image,'Pentagono', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==7:
		cv2.putText(image,'Hexagono', (x,y-5),1,1,(0,255,0),1)

	if len(approx)>13:
		cv2.putText(image,'Circulo', (x,y-5),1,1,(0,255,0),1)

	cv2.drawContours(image, [approx], 0, (255, 255, 0), 2)
	cv2.imshow('image', image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()