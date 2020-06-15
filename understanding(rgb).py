import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
img=cv2.imread(r'C:\Users\vandana\Documents\IMAGE SEGMENTATION\MR images\Rainbow.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
r, g, b = cv2.split(img)
r = np.array(r)
g = np.array(g)
b = np.array(b)
#plotting 
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(r,g,b)
plt.show()