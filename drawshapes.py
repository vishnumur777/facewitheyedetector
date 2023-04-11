import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while True:
    ret, frames = vid.read()

    width = int(vid.get(3))
    height = int(vid.get(4))

    img = cv2.line(frames, (0,0),(width,height),(0,0,255),10)
    img = cv2.line(img, (0,height),(width,0),(0,0,255),10)

    img = cv2.rectangle(img,(500,200),(100,100),(0,255,0),10)

    img = cv2.circle(img,(200,200),70,(0,255,0),10)
    
    cv2.imshow('frame',img)

    if cv2.waitKey(1) == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()