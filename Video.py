import cv2
captura = cv2.VideoCapture(0) #0 o 1

while(captura.isOpened()):
    ret, imagen = captura.read()
    if ret == True:
        cv2.imshow('Video',imagen)
        # Para maquina de 64bits
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
captura.release()
cv2.destroyAllWindows()