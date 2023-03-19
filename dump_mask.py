import cv2
import numpy as np
import argparse
import csv
import glob
# define the list of boundaries
# red, blue, yellow, gray
boundaries = [
	([180, 180, 180], [255, 255, 255])
#	([190, 190, 190], [255, 255, 255]),
#	([200, 200, 200], [255, 255, 255]),
#	([210, 210, 210], [255, 255, 255]),
#	([220, 220, 220], [255, 255, 255])
]
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

image_file = "D_366_H_127.jpg"
file_to_store = image_file[ :-4] + ".csv"
image = cv2.imread(image_file)
#	image = cv2.resize(image, ( 3840, 2160 ) )
print((image.shape[ 0 ], image.shape[ 1 ] ))	

	# create NumPy arrays from the boundaries
(lower, upper) = ([180, 180, 180], [255, 255, 255])
lower = np.array(lower, dtype = "uint8")
upper = np.array(upper, dtype = "uint8")
# find the colors within the specified boundaries and apply
# the mask
mask = cv2.inRange(image, lower, upper)
yx_coords = np.column_stack(np.where(mask >= 180))
f = open( file_to_store, 'w')
csvwriter = csv.writer( f )
fields = [ 'y', 'x' ]
csvwriter.writerow(fields)
for data in yx_coords:
	csvwriter.writerow([ data[ 0 ], data[ 1 ] ])
cv2.imshow(file_to_store, mask)
cv2.waitKey(2000)
f.close()
