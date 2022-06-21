import cv2
captura = cv2.VideoCapture(0) #0
# (Nombre.formato, blabla, Numero de imagenes por segundo, tamaño de la imagen)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
salidaV = cv2.VideoWriter('Video Prueba 5.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (1280, 960))
''' No grabo de manera correcta '''
while(captura.isOpened()):
    ret, imagen = captura.read()
    if ret == True:
        imagen = cv2.flip(imagen,1) #Girar la imagen
        cv2.imshow('Video', imagen)
        salidaV.write(imagen)   # Mostrar la imagen
        # Para maquina de 64bits
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

captura.release()
salidaV.release()
cv2.destroyAllWindows()