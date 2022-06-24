import numpy as np
import cv2
from time import sleep

video = cv2.VideoCapture(0)
_, background = video.read()
sleep(2)
_, background = video.read()
background = cv2.resize(background, (1280, 720))
background = cv2.flip(background, 1)

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (1280, 720))
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_r = np.array([0, 150, 20])
    u_r = np.array([8, 255, 255])
    mask = cv2.inRange(hsv, l_r, u_r)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    f = frame-res
    new_vid = np.where(f==0, background, f)

    cv2.imshow('new video', new_vid)

    k = cv2.waitKey(1)
    if k==ord('q'):
        break