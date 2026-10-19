import cv2
import numpy as np

path = r".\pictures\tzLab3\2-1.jpg"

img = cv2.imread(path,flags=cv2.IMREAD_COLOR)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(img,100, 255, cv2.THRESH_BINARY)

openWindow = cv2.namedWindow("openWindow",flags=cv2.WINDOW_AUTOSIZE )
closeWindow = cv2.namedWindow("closeWindow",flags=cv2.WINDOW_AUTOSIZE )
startWindow = cv2.namedWindow("startWindow",flags=cv2.WINDOW_AUTOSIZE )
imbeddedWindow = cv2.namedWindow("imbeddedWindow",flags=cv2.WINDOW_AUTOSIZE )

def closing(img, sizex, sizey, iterations):
    kernel = np.ones((sizex, sizey), np.uint8)
    workimg = cv2.dilate(img,kernel, iterations=iterations)
    workimg = cv2.erode(workimg,kernel,iterations=iterations)
    return workimg

def opening(img, sizex, sizey, iterations):
    kernel = np.ones((sizex, sizey), np.uint8)
    workimg = cv2.erode(img,kernel,iterations=iterations)
    workimg = cv2.dilate(workimg,kernel, iterations=iterations)
    return workimg
    
openImg = opening(img, 5, 5, 1)
closeImg = closing(img, 3, 3, 1)

cv2.imwrite('result_opening.jpg', openImg)
cv2.imwrite('result_closing.jpg', closeImg)

imbeddedImg = cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8),iterations=1)

cv2.imshow("startWindow", img)
cv2.imshow("closeWindow",closeImg)
cv2.imshow("openWindow", openImg)
cv2.imshow("imbeddedWindow", imbeddedImg)
cv2.waitKey(0)