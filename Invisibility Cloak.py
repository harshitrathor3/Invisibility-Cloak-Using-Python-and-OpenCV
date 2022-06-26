# Necessary imports
import numpy as np
import cv2
from time import sleep

# To capture the first view of video so that it can be replaced when the cloth with red color comes in front of the screen
video = cv2.VideoCapture(0)
_, background = video.read()
sleep(2)
_, background = video.read()
background = cv2.resize(background, (1280, 720))
background = cv2.flip(background, 1)

# To capture the video for infinite time
while True:
    # getting the video
    ret, frame = video.read()

    # Mirroring the video
    frame = cv2.flip(frame, 1)

    # Resiizing the video
    frame = cv2.resize(frame, (1280, 720))
    
    # Color converting
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Lower bound for red color
    l_r = np.array([0, 150, 20])
    # Upper bound for red color
    u_r = np.array([8, 255, 255])

    # Mask for red color
    # Only red color will be white, everything else will be black
    mask = cv2.inRange(hsv, l_r, u_r)

    # Red color will be red, everything else will be black
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Red color will be black, everything else will be normal
    f = frame-res

    # That black color will be replaced by the background image which we captured earlier
    new_vid = np.where(f==0, background, f)

    # To visualize the output
    # You can try replacing the new_vid with the mask, res, f to visualize the steps which we took
    cv2.imshow('new video', new_vid)

    # If we press q then program will stop capturing the video and program terminates
    k = cv2.waitKey(1)
    if k==ord('q'):
        break