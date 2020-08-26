import numpy as np
import cv2
import matplotlib.pyplot as plt
thr=30
img=cv2.imread('add path')
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# h,w=gray.shape
# p=[]
# for i in range(0,w):
#     for j in range(0,h):
#         p.append(gray[i,j])
# plt.hist(p)
# plt.show()
#seed is the peak of the histogram
#threshold is as desired
thr=10
l=[]
x = [ 0, -1, 1, 0]
y = [ -1, 0, 0, 1]
seed=130
print("seed value")
print(seed)
lt=seed-thr
ht=seed+thr
for i in range(1,254):
    for j in range(1,254):
        for k in range(4):
            p=[i+x[k],j+y[k]]
            p1=gray[i+x[k],j+y[k]]
            #print(p1)
            if(lt<p1<ht):
                if(p not in l):
                    #print(p)
                    l.append([i+x[k],j+y[k]])
                    img[i+x[k],j+y[k]]=[120,120,120]

cv2.imwrite('add path',img)
# cv2.imshow("y",img)
# cv2.waitKey(0)
# cv2.destroyWindow("y")
