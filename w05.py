import cv2 as cv
import numpy as np

# rectangle = np.zeros((300,300,3), dtype="uint8")
# rectangle[:] = [255,255,255]
# cv.rectangle(rectangle, (25,25), (275,275), (0,0,255), -1)
# cv.imshow("rectangle", rectangle)

# circle = np.zeros((300, 300,3), dtype = "uint8")
# circle[:] = [255,255,255]
# cv.circle(circle, (150,150), 150, (0,0,255), -1)
# cv.imshow("circle", circle)
# bitwise_xor = cv.bitwise_xor(rectangle,circle)

capture = cv.VideoCapture(0)
while(capture.isOpened()):
   ret, frame = capture.read()
   if ret == True:
       hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
       # Red mask (wraps around hue 0/179)
       lower_red1 = np.array([0, 120, 100])
       upper_red1 = np.array([8, 255, 255])
       lower_red2 = np.array([170, 120, 100])
       upper_red2 = np.array([179, 255, 255])
       mask_red = cv.bitwise_or(cv.inRange(hsv, lower_red1, upper_red1),
                                 cv.inRange(hsv, lower_red2, upper_red2))
       # Yellow mask
       lower_yellow = np.array([20, 120, 100])
       upper_yellow = np.array([35, 255, 255])
       mask_yellow = cv.inRange(hsv, lower_yellow, upper_yellow)
       # Green mask
       lower_green = np.array([45, 100, 60])
       upper_green = np.array([75, 255, 255])
       mask_green = cv.inRange(hsv, lower_green, upper_green)
       pre = cv.bitwise_or(mask_red, mask_yellow)
       pre2 = cv.bitwise_or(pre, mask_green)
       result = cv.bitwise_and(frame, frame, mask=pre2)
       cv.imshow('Frame', result)
       key = cv.waitKey(33)
       if key == ord('d'):
           break
       if cv.waitKey(25) & 0xFF == ord('d'):
           break
   else:
       break
capture.release()
cv.waitKey(0)
cv.destroyAllWindows()