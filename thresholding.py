import cv2
import numpy as np

image=cv2.imread('C:/Users/D/Desktop/bookpage.jpg',0)
retval,threshold=cv2.threshold(image,12,255,cv2.THRESH_BINARY)
gauss=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,1)

cv2.imshow('original',image)
cv2.imshow('threshold',threshold)
cv2.imshow('GAUSS',gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()