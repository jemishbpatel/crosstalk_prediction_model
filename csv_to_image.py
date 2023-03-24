#!/usr/bin/python
import sys
import csv
import numpy as np
import pandas as pd
import cv2
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--csv", nargs='?', const='test.csv', type=str, help = "path to the csv file")
ap.add_argument("-p", "--processed", help = "path to for processed image")
ap.add_argument("-i", "--intensity", nargs='?', const=128, type=int, help = "crosstalk points intensity")
ap.add_argument("-d", "--default", nargs='?', const=0, type=int, help = "defalut black/white")
args = vars(ap.parse_args())

if len( sys.argv ) < 3:
	ap.print_help( sys.stderr )
	sys.exit( 1 )
csv_file = args[ "csv" ]
processed_image = args[ "processed" ]
intensity = int( args[ "intensity" ] )
default_intensity = int( args[ "default" ] )
data = pd.read_csv( csv_file )  # path of the .csv file#print(data.shape)  # to check the shape
print (data.shape)
image_shape = data.iloc[ 0 ]
print ( ( image_shape[ 'y' ], image_shape[ 'x' ] ) )
image = np.full(( image_shape[ 'y' ], image_shape[ 'x' ], 3), default_intensity, dtype=np.uint8)

white = [ intensity, intensity , intensity ]
for i in range( 1, data.shape[ 0 ] ):  #data.shape[0] gives no. of rows
	face = data.iloc[ i ]  # remove one row from the data
	image[ face[ 'y' ], face[ 'x' ] ] = white  # send this row of to the function 

cv2.imshow( 'img', image )
cv2.imwrite( processed_image, image )
cv2.waitKey( 5000 )

