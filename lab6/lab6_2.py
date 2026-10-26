import cv2
import numpy as np


def draw_line_P(line, img, color=(0, 0, 255),thickness=1, lineType=cv2.LINE_AA): 
    x0, y0, x1, y1 = line
    cv2.line(img, (x0, y0), (x1, y1),color, thickness, lineType) 

def draw_circle(circle, img, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA):
    x, y, r = circle
    cv2.circle(img, (x, y), r, color, thickness, lineType)

def opening(img, sizex, sizey, iterations):
    kernel = np.ones((sizex, sizey), np.uint8)
    workimg = cv2.erode(img,kernel,iterations=iterations)
    workimg = cv2.dilate(workimg,kernel, iterations=iterations)
    return workimg

def closing(img, sizex, sizey, iterations):
    kernel = np.ones((sizex, sizey), np.uint8)
    workimg = cv2.dilate(img,kernel, iterations=iterations)
    workimg = cv2.erode(workimg,kernel,iterations=iterations)
    return workimg

def find_largest(lines):
    lenght2 = 0
    largesti = -1
    for i, line in enumerate(lines):
        x0, y0, x1, y1 = line
        new_length2 = (x1-x0)**2+(y1-y0)**2
        if new_length2>lenght2:
            lenght2 = new_length2
            largesti = i
    return lines[largesti]

def find_largest_circle(circles):
    rl = 0
    largesti = -1
    for i, circle in enumerate(circles[0,:]):
        _, _, r = circle
        if r > rl:
            rl = r
            largesti = i
    return [round(i) for i in circles[0,largesti]]

path = r".\pictures\tzLab3\2-1.jpg"

img = cv2.imread(path,flags=cv2.IMREAD_COLOR)

grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Linii2",flags=cv2.WINDOW_AUTOSIZE)

openImg = closing(grayimg, 4, 4, 1)

lines = cv2.HoughLinesP(cv2.bitwise_not(openImg), 1, np.pi/180, 100)
circles = cv2.HoughCircles(cv2.bitwise_not(openImg),  cv2.HOUGH_GRADIENT, 1, 100, 100, 50) 
openImg2 = cv2.cvtColor(openImg, cv2.COLOR_GRAY2BGR)
draw_line_P(find_largest(lines),openImg2)
draw_circle(find_largest_circle(circles),openImg2)

cv2.imshow('Linii2', openImg2)
#cv2.imwrite("Linii12"+".jpg",img)
cv2.waitKey(0)
