import cv2
import numpy as np

img_rgb = cv2.imread('C:/Users/D/Desktop/opencv-template-matching-python-tutorial.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('C:/Users/D/Desktop/opencv-template-for-matching.jpg',0)
x,y= template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
locy,locx = np.where( res >= threshold)
print(locy)	 
print(locx)
x2=zip(locx,locy)

for pt in x2:
    print(pt)
    cv2.rectangle(img_rgb, pt,(pt[0]+x,pt[1]+y),(0,255,255), 1)
	

cv2.imshow('Detected',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
