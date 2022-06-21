# ROI Necesario para el proyecto!

import cv2
import numpy as np

# Pizarra = 0 * np.ones((500, 500, 3), dtype=np.uint8)
image = cv2.imread('ColorRGB.png')

# cv2.imshow('Color RGB', image)
# cv2.waitKey(0)

# ROI ----------------------------------------------
# Que es ROI?
ROI = cv2.selectROI(image)
print("Recorte es de: ", ROI)
# Pizarra_cropped
Pizarra_recortada = image[int(ROI[1]): int(ROI[1]+ROI[3]), int(ROI[0]): int(ROI[0]+ROI[2])]

#print("Color posición 0,0: "  + str(Pizarra[250,250]))
for fila in range(10):   # Tamaño de Imagen en X
    for columna in range(10):    # Tamaño de Imagen en Y
         print("Color", ": Fila:", + fila, "; Columna:", + columna, " -> ", str(Pizarra_recortada[fila, columna]))

cv2.imshow('Imagen Recortada', Pizarra_recortada)
cv2.waitKey(0)
cv2.destroyAllWindows()