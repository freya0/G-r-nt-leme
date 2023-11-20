import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while(True):
    ret,image = vid.read()

    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    lower_red = np.array([160,50,50])
    upper_red = np.array([180,255,255])

    mask = cv2.inRange(hsv,lower_red,upper_red)

    result = cv2.bitwise_and(image,image,mask = mask)

    cv2.imshow("image",image)

    cv2.imshow("Masked Image", result)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break