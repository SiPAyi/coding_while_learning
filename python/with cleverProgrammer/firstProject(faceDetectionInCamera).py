import cv2

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# # choose an image to detect faces in
# img = cv2.imread('siddu.jpg')
#
# # # to show the image
# # cv2.imshow('Showing the image', img)
# # cv2.waitKey()
#
# # image converted to grayscale
# grayScaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # # to show the image to the user
# # cv2.imshow('Face Detector', grayScaled_img)
# #
# # # stop the program for the user to enter any key
# # cv2.waitKey()
#
#
# # Detect Faces
# face_coordinates = trained_face_data.detectMultiScale(grayScaled_img)
#
# # Draw rectangle
# for (x, y, w, h) in face_coordinates:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
# cv2.imshow('face', img)
# cv2.waitKey(0)


# to capture the video
webcam = cv2.VideoCapture(0)
#webcam = cv2.VideoCapture('Python Artificial Intelligence Tutorial - AI Full Course for Beginners in 9 Hours [2021].mp4')


while True:
    # read the current frame
    camera_condition, frame = webcam.read()

    # convert the image to gray scale
    gray_scaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(gray_scaled_img)

    # Draw rectangle
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


    # showing the image
    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)

    # press q to quit the camera
    if key == 81 or key == 113:
        break

webcam.release()




print('completed successfully !')
