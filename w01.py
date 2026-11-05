import cv2 as cv
img = cv.imread("silly.png")
height, width, channels = img.shape
for x in range(height):
    for y in range(width):
        gray = 0.114*img[x,y,0] + 0.587*img[x,y,1]+0.299*img[x,y,2]
        if gray >= 90:
            img[x,y] = [255,255,255]
        else:
            img[x,y] = [0,0,0]

print(img)
cv.imshow('cat',img)
cv.waitKey(0)
cv.destroyAllWindows()                