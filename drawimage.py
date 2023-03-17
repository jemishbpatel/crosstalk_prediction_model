import cv2
import numpy as np

width = 100
height = 100

# Make empty black image of size (100,100)
img = np.zeros((height, width, 3), np.uint8)

red = [0,0,255]

# Change pixel (50,50) to red
img[50,50] = red

cv2.imshow('img', img)
cv2.waitKey(5000)
