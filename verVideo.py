import cv2

cap = cv2.VideoCapture('PV.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# import cv2
# import numpy as np
#
# captura = cv2.VideoCapture('Video Prueba 5.avi')
#
# while(captura.isOpened()):
#     ret, imagen = captura.read()
#     if ret == True:
#         cv2.imshow('Video',imagen)
#         # Para maquina de 64bits
#         if cv2.waitKey(50) & 0xFF == ord('s'):
#             break
# captura.release()
# cv2.destroyAllWindows()