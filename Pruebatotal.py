import numpy as np
import cv2 #Opencv

# Dimensiones proporcionales ingresando la altura
sizeAl = float(input('Tamaño de la altura en pixeles: '))
sizeAn = sizeAl * 0.77272
print(int(sizeAl), 'X', int(sizeAn))
Pizarra = 0 * np.ones((int(sizeAl), int(sizeAn), 3), dtype=np.uint8)

cv2.imshow('Pizarra', Pizarra)
cv2.waitKey(0)
cv2.destroyAllWindows()