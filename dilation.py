@@ -0,0 +1,7 @@
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\sreeh\\Desktop\\OpenCV\\image1.jpg",0)
kernel = np.ones((5,5),np.int8)
dilation = cv2.dilate(img,kernel,iterations=1)
cv2.imwrite("dilated_image.jpg",dilation
