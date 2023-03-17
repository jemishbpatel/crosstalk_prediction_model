import numpy as np
import pandas as pd
import cv2
#import utils
import os

data = pd.read_csv('D_396_H_127.csv')  # path of the .csv file#print(data.shape)  # to check the shape
image = np.zeros((2160, 3840,3), np.uint8)  # empty matrix

white = [255,255,255]
count = 0  # initialize counter
for i in range(1, data.shape[0]):  #data.shape[0] gives no. of rows
	face = data.iloc[i]  # remove one row from the data
	image[ face[ 'y' ], face[ 'x' ] ] = white  # send this row of to the function 

cv2.imshow('img', image)
cv2.waitKey(5000)

