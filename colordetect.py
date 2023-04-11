import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    masks = cv2.inRange(hsv, lower_blue, upper_blue)

    results = cv2.bitwise_and(frame, frame, mask=masks)

    cv2.imshow('frame',results)
    cv2.imshow('mask',masks)

    if cv2.waitKey(1)==ord('q'):
        break

vid.release()
cv2.destroyAllWindows()