# import cv2 as cv 
# import numpy as np
# vdo = cv.VideoCapture(0)

# while (vdo.isOpened()):
#     ret, frame = vdo.read()
#     if ret == True:
#         frame = cv.resize(frame,fx=0.5, fy=0.5, dsize=(0,0), interpolation=cv.INTER_AREA)
#         cv.imshow("Video_resize", frame)
#         cv.imshow("video", frame)
#         if cv.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break 

# vdo.release()
# cv.destroyAllWindows()

# img = cv.imread("silly.png")
# crop = img[100:400, 100:500]
# rotate = cv.rotate(crop, cv.ROTATE_180)
# print(img.shape)
# cv.imshow('dasf', img)
# cv.imshow("wasd", crop)
# cv.imshow("rotate", rotate)

# img = cv.imread("silly.png")
# mat = np.float32([0,0,0,],
#                  [0,0,0,])
# rotate = cv.warpAffine(img, mat, (img.shape[1], img.shape[0]))
# cv.imshow("image", img)
# cv.imshow("rotate", rotate)                 
# cv.waitKey(0)
# cv.destroyAllWindows()
# print (img.shape)
# img_crop = img[100:100+270]
# img_rotate = cv.rotate(img, cv.ROTATE_180)
# cv.imshow("Image Crop",img_crop)
# cv.imshow("Image rotate",img_rotate)
# cv.waitKey(0)
import cv2 as cv
import numpy as np
img=cv.imread("silly.png")
hight=img.shape[0]
width=img.shape[1]

mat = np.float32([[1,0,50],
                  [0,1,50]])
rotate1 = cv.getRotationMatrix2D((width/2, hight/2),27,1)
rotate2 = cv.getRotationMatrix2D((width/2, hight/2),95,1)
rotated = cv.warpAffine(img,rotate1,(width,hight))
moved_img = cv.warpAffine(img,mat,(width,hight))
streched_img1 = cv.resize(img ,fx=2 ,fy=1,dsize=(0,0),interpolation=cv.INTER_AREA)
streched_img2 = cv.resize(img ,fx=1 ,fy=2,dsize=(0,0),interpolation=cv.INTER_AREA)
combind_img = cv.warpAffine(streched_img2,rotate2,(width,hight))
cv.imshow("Rotate",rotated)
cv.imshow("Moved",moved_img)
cv.imshow("Stretched",combind_img)
s1 = cv.resize(streched_img1,(width,hight))
s2 = cv.resize(streched_img2,(width,hight))
cv.imshow("Stretched1 & Stretched2",cv.addWeighted(s1,0.5,s2,0.5,0))
cv.waitKey(0)

