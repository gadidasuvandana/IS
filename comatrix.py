#This code plots the co-occurence matrix of a L level image in 3d
import numpy as np
from skimage.feature import greycomatrix
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import cv2
import math
#insert the path of the image here
img=cv2.imread(r'C:\Users\vandana\Documents\IMAGE SEGMENTATION\IS\MR images\t16.jpg',0)
#gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
p=[]
h=img.shape[0]
w=img.shape[1]
print('Height and Width of the gray image:')
print(h,w)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        pix=img[i,j]
        pix=int(pix/2)
        p.append(pix)
        img[i,j]=pix
p=np.array(p)
p=np.reshape(p,(h,w))
#print(np.shape(p))
image = np.array(p, dtype=np.uint8)
result = greycomatrix(p, [1], [0],levels=128)#change levels according to intensity,ie L value
res=result[:,:,0,0]
print('Dimensions of the co-occurence matrix:')
print(np.shape(res))
#make sure the value inside arange is the value of L
x = np.arange(128)
y = np.arange(128)
xs, ys = np.meshgrid(x, y,sparse=True)
zs=res
fig = plt.figure()
ax = Axes3D(fig)
ax.grid(False)
ax.plot_surface(xs, ys, zs)
plt.show()
#This is to plot the normalised form
# norm = np.linalg.norm(res)
# normal_array = res/norm
# print('The normalised co-occurence matrix is:')
# print(normal_array)
# print(np.count_nonzero(normal_array))
# #print(np.shape(normal_array))
#savetxt(r'C:\Users\vandana\Documents\IMAGE SEGMENTATION\64(un).csv',res, delimiter=',')
# #cv2.imwrite(r'C:\Users\vandana\Documents\IMAGE SEGMENTATION\output\img(64).jpg',img)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows