#k means using cv2.kmeans library
#k means is a form of clustering technique 
import numpy as np
import cv2
img=cv2.imread(r'C:\Users\vandana\Documents\IMAGE SEGMENTATION\MR images\1.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img.shape)
vectorized = img.reshape(img.shape[0]*img.shape[1],img.shape[2])
print(np.shape(vectorized))
vectorized = np.float32(vectorized)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K =5
#the value of k can be altered,optimumvalue is found using the elbow method
attempts=5
ret,label,center=cv2.kmeans(vectorized,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
center = np.uint8(center)
print(center)
res = center[label.flatten()]
result_image = res.reshape((img.shape))
#to display the segmented image
# cv2.imshow('image',result_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
