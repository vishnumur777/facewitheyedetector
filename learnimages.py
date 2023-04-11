import cv2
import numpy as np
import random

img = cv2.imread('assets/temples.jpeg',-1)

print(img)
print(type(img))

img1 = cv2.resize(img,(1000,500))

h = img1.size

for i in range(100):
    for j in range(100):
        img1[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow('Image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()