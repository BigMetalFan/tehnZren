import cv2
import numpy as np

path = r".\pictures\tzLab5\6-1.png"

img = cv2.imread(path, flags=cv2.IMREAD_COLOR)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);


def isXAngle(n, contour):
    perimeter = cv2.arcLength(contour, True)
    if cv2.contourArea(contour)<100: return False
    epsilon = 0.04 * perimeter
    approx = cv2.approxPolyDP(contour, epsilon, True)
    return len(approx) == n

def isCircle(contour):
    area = cv2.contourArea(contour)
    if area<100: return False
    perimeter = cv2.arcLength(contour, True)
    return (4*np.pi*area/perimeter/perimeter)>0.8

def findSquares(contours):
    squares = []
    for i,contour in enumerate(contours):
        if(isXAngle(4,contour)): squares.append(i)
    return squares

def findTriangels(contours):
    triangels  = []
    for i,contour in enumerate(contours):
        if(isXAngle(3,contour)): triangels.append(i)
    return triangels

def findCircles(contours):
    circles  = []
    for i,contour in enumerate(contours):
        if(isCircle(contour)): circles.append(i)
    return circles


ret, thresh_img = cv2.threshold(gray_img,100, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy =  cv2.findContours(thresh_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
print(hierarchy)

squares = findSquares(contours)
triangels = findTriangels(contours)
circles = findCircles(contours)

for i in squares:
    cv2.drawContours(img, contours, i, (0, 0, 255), 2)
for i in triangels:
    cv2.drawContours(img, contours, i, (255, 0, 255), 2)
for i in circles:
    cv2.drawContours(img, contours, i, (255, 0, 0), 2)

cv2.imshow('Contours', img)
cv2.imwrite("Contours"+".jpg",img)
cv2.waitKey(0)