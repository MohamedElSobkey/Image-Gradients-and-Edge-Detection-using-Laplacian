import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('messi5.jpg',0)
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
#override
lap = np.uint8(np.absolute(lap))


cv2.imshow('image',img)
cv2.imshow('Laplacian', lap)

cv2.waitKey(0)
cv2.destroyAllWindows()
