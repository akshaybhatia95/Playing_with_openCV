import cv2
import numpy as np

img=cv2.imread('C:/Users/D/Desktop/22477228-Chess-board-Stock-Vector.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)
corners=cv2.goodFeaturesToTrack(gray,1000,0.5,100)
corners=np.int0(corners)
for corner in corners:
 x,y=corner.ravel()
 cv2.circle(img,(x,y),3,255,-1)

cv2.imshow('a',img) 

cv2.waitKey(0)
cv2.destroyAllWindows()