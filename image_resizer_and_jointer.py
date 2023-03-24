#!/usr/bin/python
import sys
import argparse
import subprocess

ap = argparse.ArgumentParser()

ap.add_argument("-i1", "--image1", help = "path to first image")
ap.add_argument("-i2", "--image2", help = "path to second image")
ap.add_argument("-r", "--resize", help = "resize resolution")
ap.add_argument("-o", "--outputimage", help = "output image name")
args = vars(ap.parse_args())

if len(sys.argv) < 9:
	ap.print_help( sys.stderr )
	sys.exit( 1 )
image1 = args[ "image1" ]
image2 = args[ "image2" ]
resize_resolution = args[ "resize" ]
outputImage = args[ "outputimage" ]

print ( image1 ) 
print ( image2 ) 
print ( resize_resolution.split('x')[ 0 ] )
print ( resize_resolution.split('x')[ 1 ] )
print ( outputImage ) 

width = int( resize_resolution.split('x')[ 0 ] ) / 2
height = int( resize_resolution.split('x')[ 1 ] )
print( "Resizing image1 %s " % image1 )
subprocess.call([ 'ffmpeg', '-i', image1, '-vf', 'scale={}:{}'.format( width, height ), "resize1_{}_{}.jpg".format( width, height ) ])
print( "Resizing image2 %s " % image2 )
subprocess.call(['ffmpeg', '-i', image2, '-vf', 'scale={}:{}'.format( width, height ), "resize2_{}_{}.jpg".format( width, height ) ])
print( "Merging resize image1 and resize image 2 in output image %s " % outputImage )
subprocess.call( [ 'ffmpeg', '-i', "resize1_{}_{}.jpg".format( width, height ), "-i", "resize2_{}_{}.jpg".format( width, height ), '-filter_complex', 'hstack', outputImage ]  )
print( "Creating video from single image" )
subprocess.call( [ 'ffmpeg', '-loop', '1', '-i', outputImage, '-c:v', 'libx264', '-t', '15', '-pix_fmt', 'yuv420p', '-vf', 'scale=1280:720', outputImage + "video.mp4" ] )
