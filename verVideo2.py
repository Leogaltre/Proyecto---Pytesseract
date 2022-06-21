import cv2
from PIL import Image
cap = cv2.VideoCapture('PV.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()
#
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     # dsize
#     Al = 0.5 * height
#     An = 0.5 * width
#     dsize = (An, width)
#     # cambiar el tamaño de la image
#     output = cv2.resize(filepath, dsize)
#     # Redimg1 = cv2.resize(img1, (620, 620))
#     cv2.imshow('frame', output)
#     if cv2.waitKey(1) & 0xFF == ord('s'):
#         break
