import cv2
import numpy as np
img=cv2.imread(r'C:\Users\vandana\Documents\IMAGE SEGMENTATION\MR images\Rainbow.jpg',0)
#cv2.imrread(img,0) reads a 16 bit gray image
print(img.shape)
#converts 16 bit gray to 8 bit gray
img8 = img.astype('uint8')
f=img8[139,55]
#prints the datatype of the data
print(np.dtype(f))
height=img.shape[0]
width=img.shape[1]
channels=img.shape[2]
print(height,width,channels)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thr = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)#does OTSU binarisation to make it black n white
px1=gray[53,164]
print(px1)
print(thr[53,164])
cv2.imshow('image',img8)
cv2.waitKey(0)
cv2.destroyAllWindows()
