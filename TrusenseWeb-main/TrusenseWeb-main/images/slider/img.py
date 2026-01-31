import cv2
import numpy as np


t0=cv2.imread("sensus0.jpg")
t1=cv2.imread("sensus1.jpg")

t1=cv2.resize(t1,(t0.shape[1],t0.shape[0]))

black_img= np.zeros((t0.shape[0],t0.shape[1],3), np.uint8)
alpha=0.5

# Add the two images
g0=cv2.addWeighted(black_img,alpha,t0,1-alpha,0)
g1=cv2.addWeighted(black_img,alpha,t1,1-alpha,0)

# save
cv2.imwrite("output.jpg",g0)
cv2.imwrite("output1.jpg",g1)