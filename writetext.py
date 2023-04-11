import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while True:
    ret, frames = vid.read()

    width = int(vid.get(3))
    height = int(vid.get(4))

    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(frames,'Hello Varun!!!',(10,height-20),font,2,(0,255,0),5,cv2.LINE_AA)

    cv2.imshow('frame',img)
    if cv2.waitKey(1)==ord('q'):
        break
vid.release()
cv2.destroyAllWindows()