import numpy as np
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print ("Video device or file couldn't be opened")
    exit()
while(cap.isOpened()):
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break