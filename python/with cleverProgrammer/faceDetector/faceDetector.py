import cv2
import re

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# defining function for face detection
# this function need to have a imagePath as argument

def detectFace(imgPath):
	img = cv2.imread(imgPath)
	# image converted to grayscale
	gray_scaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Detect Faces
	face_coordinates = trained_face_data.detectMultiScale(gray_scaled_img)

	# Draw rectangle
	for (x, y, w, h) in face_coordinates:
	    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
	
	cv2.imshow('face', img)
	cv2.waitKey(1000)

# to get the path from the user
imagePath = input('Enter the image path : ')

# calling the function to detect the face
detectFace(imagePath)
