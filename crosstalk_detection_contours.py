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

for image_file in glob.glob("crosstalk_images_with_label/*.jpg"):
	file_to_store = image_file[ :-4] + ".csv"
	image = cv2.imread(image_file)
	image = cv2.resize(image, ( 3840, 2160 ) )
	print((image.shape[ 0 ], image.shape[ 1 ] ))	

#image = cv2.imread(args["image"])
# loop over the boundaries
#for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	(lower, upper) = ([180, 180, 180], [255, 255, 255])
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	#f.write( contours )
	f = open( file_to_store, 'w')
	csvwriter = csv.writer( f )
	fields = [ 'x', 'y' ]
	csvwriter.writerow(fields)
	value = np.asarray( contours )
	for c in range(len(contours)):
		n_contour = contours[c]
		for d in range(len(n_contour)):
			XY_Coordinates = n_contour[d]
			coordinates = [ XY_Coordinates[ 0 ][ 0 ], XY_Coordinates[ 0 ][ 1 ] ]
			csvwriter.writerow(coordinates)

	cv2.drawContours(output, contours, -1, (0, 255, 0), 3)
	# show the images
	#cv2.imshow(image_name, np.hstack([image, output]))
	cv2.imshow(file_to_store, output)
	cv2.waitKey(10000)
	f.close()
