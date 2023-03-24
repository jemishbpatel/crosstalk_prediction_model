#!/usr/bin/python
import sys
import cv2
import numpy as np
import argparse
import csv
import glob


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
ap.add_argument("-c", "--csv", nargs='?', const='test.csv', type=str ,help = "csv file path to store identified crosstalk points")
ap.add_argument("-l", "--lowerlimit", nargs='?', const=150, type=int, help = "lower intensity value to identify crosstalk points")
ap.add_argument("-u", "--higherlimit", nargs='?', const=255, type=int, help = "higher intensity value to identify crosstalk points")
args = vars(ap.parse_args())

if len(sys.argv) < 3:
	ap.print_help( sys.stderr )
	sys.exit( 1 )
lowerIntensity = args[ 'lowerlimit' ]
higherIntensity = args[ 'higherlimit' ]
image_file = args[ "image" ]
file_to_store = args[ "csv" ]
boundaries = [
	([ lowerIntensity, lowerIntensity, lowerIntensity ], [ higherIntensity, higherIntensity, higherIntensity ] )
]

image = cv2.imread(image_file)
print( image.shape)
print( (image.shape[ 0 ], image.shape[ 1 ] ) )
# create NumPy arrays from the boundaries
( lower, upper ) = (boundaries[ 0 ][ 0 ], boundaries[ 0 ][ 1 ] )
lower = np.array( lower, dtype = "uint8" )
upper = np.array( upper, dtype = "uint8" )
# find the colors within the specified boundaries and apply
# the mask
mask = cv2.inRange(image, lower, upper)
yx_coords = np.column_stack( np.where( mask >= lowerIntensity ))
f = open( file_to_store, 'w')
csvwriter = csv.writer( f )
fields = [ 'y', 'x' ]
csvwriter.writerow( fields )
csvwriter.writerow( [ image.shape[ 0 ], image.shape[ 1 ] ] )
for data in yx_coords:
	csvwriter.writerow( [ data[ 0 ], data[ 1 ] ] )
cv2.imshow( file_to_store, mask )
cv2.waitKey(2000)
f.close()
