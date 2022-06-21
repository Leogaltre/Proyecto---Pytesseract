import cv2
import numpy as np

imagen = cv2.imread('Conto.png')
# Imagen en escala de Grises
gray = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
# Imagen binarizada -> Blanco y Negro
_,th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

#Para versiones OpenCV3:
#img1,contornos1,hierarchy1 = cv2.findContours(th, cv2.RETR_EXTERNAL,
#      cv2.CHAIN_APPROX_NONE)
#img2,contornos2,hierarchy2 = cv2.findContours(th, cv2.RETR_EXTERNAL,
#      cv2.CHAIN_APPROX_SIMPLE)

#Para versiones OpenCV4: -> Encontrar los contornos
# cv2.findContours(1, 2, 3, 4)
# 1) Imagen Binarizada
# 2) Modo de Recuperación de contorno
      # cv2.RETR_LIST
      # cv2.RETR_EXTERNAL
      # cv2.RETR_CCOMP
      # cv2.RETR_TREE
# 3) Método de aproximación de contorno
      # cv2.CHAIN_APPROX_NONE
      # cv2.CHAIN_APPROX_SIMPLE
# 4) Desplazamiento opcional
# a,b = cv2.findContours(1, 2, 3, 4)
# a) Contornos detectados como vector de puntos
# b) Relacion de contornos

contornos1,hierarchy1 = cv2.findContours(th, cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_NONE)
# contornos2,hierarchy2 = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Obtener la posicion de cada contorno de 0 - n (no funciono)
# for i in range(len(contornos1)):
#       cv2.drawContours(imagen, contornos1, i, (255, 255, 255), 3)
#       cv2.imshow('imagen',imagen)
#       cv2.waitkey(0)

# cv2.drawContours(1, 2, 3, 4, 5)
# 1) Imagen en donde se dibujara el contorno
# 2) Contornos encontrados
# 3) Contorno que debe dibujarse (-1 = Todos los contornos)
# 4) Color
# 5) Grosor

cv2.drawContours(imagen, contornos1, -1, (255,255,0), 3)
print ('len(contornos1[2])=',len(contornos1[2]))
# print ('len(contornos2[2])=',len(contornos2[2]))
cv2.imshow('imagen', imagen)
cv2.waitKey(0)
cv2.imshow('th', th)
cv2.waitKey(0)
cv2.destroyAllWindows()