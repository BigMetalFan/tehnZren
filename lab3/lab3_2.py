import cv2
import numpy as np

path = r".\pictures\tzLab3\2-2.jpg"

img = cv2.imread(path,flags=cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_inverted = cv2.bitwise_not(img)
openWindow = cv2.namedWindow("openWindow",flags=cv2.WINDOW_AUTOSIZE )


openImg = cv2.morphologyEx(img_inverted, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8),iterations=1)

openImg = cv2.bitwise_not(openImg)
cv2.imshow("openWindow", openImg)
cv2.imwrite("lab3/morph"+str(id(img))+".jpg",openImg)
cv2.waitKey(0)