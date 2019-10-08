import cv2
import numpy as np

img=cv2.imread("C:/Users/D/Desktop/watch2.jpg",cv2.IMREAD_GRAYSCALE)
print (img.shape)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()