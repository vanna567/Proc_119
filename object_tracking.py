import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

# Carga el rastreador 
tracker = cv2.TrackerCSRT_create()

# Lee el primer cuadro del video
returned, img = video.read()

# Selecciona el campo delimitador de la imagen
bbox = cv2.selectROI("Rastreando", img, False)

# Inicializa el rastreador en la imagen y el campo delimitador
tracker.init(img, bbox)
print(bbox)

def drawBox(img, bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y), ((x+w), (y+h)),(255,0,255), 3,1)
    cv2.putText(img, "Rastreando", (75,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

while True:
    check,img = video.read()  

    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "Perdido", (75,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

        cv2.imshow("resultado",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("¡Alto!")
        break


video.release()
cv2.destroyALLwindows()







