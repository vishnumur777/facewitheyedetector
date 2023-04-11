import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(1)==ord('q'):
        break


vid.release()
cv2.destroyAllWindows()