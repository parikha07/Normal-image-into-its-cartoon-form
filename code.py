import cv2
import numpy as np

num_down=2                 #no. of Downsampling Steps
num_bilateral=7            #no. of bilateral filtering steps

img=cv2.imread('IMG_20180617_182219872.jpg')
print(img.shape)           #dimensions
img=cv2.resize(img, (800,800))  #resizing to get optimal result after samplingimg_

#down sampling of image using Gaussian Pyramid
img_color=img
for _ in range (num_down):
    img_color=cv2.pyrDown(img_color)
  
#apply small bilteral filter instead of small one
for _ in range (num_bilateral):
    img_color=cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=9)

#unsample image to original
for _ in range (num_down):
    img_color=cv2.pyrUp(img_color)
 
img_gray=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_blur=cv2.medianBlur(img_gray, 7)
img_edge=cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)

#convert back to color and do bitwise end with color image
img_edge=cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
img_cartoon=cv2.bitwise_and(img_color, img_edge)

cv2.imshow("CARTOON", img_cartoon)
cv2.waitKey(0)

stack=np.hstack([img, img_cartoon])
cv2.imshow('Stacked Images', stack)
cv2.waitKey(0)
