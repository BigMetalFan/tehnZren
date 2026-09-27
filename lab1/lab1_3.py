import cv2
import numpy as np

path = r"D:\Main\Pituxon\zren\pictures\tzLab1\1-2.jpg"

img = cv2.imread(path)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_white = np.array([0, 0, 150])
upper_white = np.array([180, 100, 255])
hsv_mask = cv2.inRange(hsv, lower_white, upper_white)


gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
autoret, auto_tresh_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

windowHSV = cv2.namedWindow("windowHSV",flags=cv2.LDR_SIZE )
windowA = cv2.namedWindow("windowA",flags=cv2.LDR_SIZE )

cv2.imshow("windowHSV", hsv_mask)
cv2.imshow("windowA", auto_tresh_img)
cv2.waitKey(0)