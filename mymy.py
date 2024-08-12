import cv2
import random
import numpy as np
#import mediapipe as mp
RTSP0 = "rtsp://172.32.0.93/live/0"
cap0 = cv2.VideoCapture(RTSP0)


size_h = 1080 # 600
size_w = 1920 # 800


while True:
        ret0,frame0=cap0.read()
        if ret0 == True:
            frame0 = cv2.resize(frame0,(1920,1080))

        cv2.imshow("SystemTech_124 ", frame0)

        key=cv2.waitKey(1)

        if key==ord('q'):
          break

cap0.release()

# test rsync
