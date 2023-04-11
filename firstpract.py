import cv2
import numpy as np

img = cv2.imread('assets/temples.jpeg')
img1 = cv2.resize(img,(1000,500))

cv2.imshow('Image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()