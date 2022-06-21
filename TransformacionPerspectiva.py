import cv2 #Opencv
import numpy as np
from matplotlib import pyplot as plt
# Usando eventos de mouse hacer la transformacion de perspectiva

def clics(event, x, y, flags, parm):
    global puntos
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen, (x, y), 5, (0, 255, 0), 2)
        puntos.append([x, y])

def uniendo4puntos(puntos): #(0,1),(0,2),(2,3),(3,1)
    cv2.line(imagen, tuple(puntos[0]), tuple(puntos[1]), (255, 0, 0), 1)
    cv2.line(imagen, tuple(puntos[0]), tuple(puntos[2]), (255, 0, 0), 1)
    cv2.line(imagen, tuple(puntos[2]), tuple(puntos[3]), (255, 0, 0), 1)
    cv2.line(imagen, tuple(puntos[1]), tuple(puntos[3]), (255, 0, 0), 1)

puntos = []
img = cv2.imread('IMG1.png')
# Dimensiones de la Laptop -> 1366 x 768
# Dimensiones de la Hoja tamaño carta 8.5 x 11
# sizeAl = float(input('Tamaño de la altura en pixeles: '))
# sizeAn = sizeAl * 0.77272
# print(int(sizeAl), 'X', int(sizeAn))
# Pizarra = 0 * np.ones((int(sizeAl), int(sizeAn), 3), dtype=np.uint8)

imagen = cv2.resize(img, (556, 720))
aux = imagen.copy()
cv2.namedWindow('Imagen')
cv2.setMouseCallback('Imagen',clics)

#algoritmo weibled investigar para no perder informacion
while True:
    if len(puntos) == 4:
        uniendo4puntos(puntos)
        pts1 = np.float32([puntos])
        # Dimensiones -> 2465 x 2945 dar en tamaños estandar
        # Redimencionado -> 556 x 720
        pts2 = np.float32([[0, 0], [556, 0], [0, 720], [556, 720]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(imagen, M, (556, 720))

        cv2.imshow('DST',dst)

    cv2.imshow('Imagen', imagen)

    # Borrar puntos con clic Izquierdo
    k = cv2.waitKey(1) & 0xFF
    if k == ord('n'):
        imagen = aux.copy()
        puntos = []
    elif k == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()