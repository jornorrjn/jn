import cv2 as cv
import numpy as np
import random
img = np.zeros((512, 512, 3), np.uint8)
drawing = False
ix, iy = -1, -1

# def click_position(event,x,y, flages,param) :
#      if event == cv. EVENT_LBUTTONDOWN:
#         cv.putText(img, "67",(x,y), 1,3,(0,0,255),3)
#         cv. imshow("click puttext", img)

def draw_circle(event, x, y,flags,param) :
      global ix, iy, drawing, img

      if event == cv.EVENT_LBUTTONDOWN:
         drawing = True  
         ix, iy = x, y

      elif event == cv.EVENT_MOUSEMOVE:   
         if drawing:
             img_copy=img.copy()
             radius = int(((x-ix)**2 + (y-iy)**2)**0.5)
             cv.circle(img_copy, (ix, iy), radius, (0, 250, 0), 2)
             cv.imshow("circle window", img_copy)

      elif event == cv.EVENT_LBUTTONUP: 
          drawing = False
          radius = int(((x - ix)**2 + (y-iy)**2)**0.5)
          color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
          cv.circle(img, (ix, iy), radius, color, 2)
          cv.imshow("circle window", img)      
        
         
cv.imshow("circle window", img)
cv.setMouseCallback("circle window",draw_circle)
cv.waitKey(0)
cv.destroyAllWindows ()