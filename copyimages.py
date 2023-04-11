import cv2
import numpy as np 

img = cv2.imread('assets/temples.jpeg',1)

img1 = cv2.resize(img,(1000,500))

tag = img1[100:200, 200:250]
img1[200:300,400:450] = tag

cv2.imshow('Images',img1)
cv2.waitKey()
cv2.destroyAllWindows()