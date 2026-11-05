import cv2 as cv

img = cv.imread("images.jpg")

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
gray_img = cv.cvtColor(img, cv.C0LOR_RGB2GRAY)

scale = 1.1
minNeighbor = 3
face_detect = face_cascade.detectMultiScale(gray_img, scale,minNeighbor)
x, y, w, h = face_detect [0]
print(face_detect)
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=10)
cv.imshow("face detect", img)
cv.waitKey(0)
cv.destroyAllWindows()