import cv2
import random
import numpy as np
#import mediapipe as mp
RTSP1 = "rtsp://172.32.0.93/live/0"
RTSP0 = "rtsp://192.168.0.124:554/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp?real_stream"
#RTSP1 = "rtsp://192.168.0.125:554/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp?real_stream"
cap0 = cv2.VideoCapture(RTSP0)
cap1 = cv2.VideoCapture(RTSP1)

size_h = 1080
size_w = 1920


while True:
        ret0,frame0=cap0.read()
        if ret0 == True:
            frame0 = cv2.resize(frame0,(800,600))
        ret1,frame1=cap1.read()
        if ret1 == True:
            frame1 = cv2.resize(frame1,(800,600))
        cv2.imshow("SystemTech_124 ", frame0)
        cv2.imshow("SystemTech_125 ", frame1)
        key=cv2.waitKey(1)

        if key==ord('q'):
          break

cap0.release()
cap1.release()

