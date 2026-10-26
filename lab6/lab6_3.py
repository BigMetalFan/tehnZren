import cv2
import numpy as np

def draw_circles(circles, img, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA):
    if circles is None:
        print('пустое множество')
        return
    for circle in circles[0,:]:
            x, y, r = (round(i) for i in circle)
            cv2.circle(img, (x, y), r, color, thickness, lineType)

paths = [r".\pictures\tzLab6\4_5_1.jpg", r".\pictures\tzLab6\4_5_2.jpg",r".\pictures\tzLab6\4_5_3.jpg",
        r".\pictures\tzLab6\4_5_4.jpg",r".\pictures\tzLab6\4_5_5.jpg", r".\pictures\tzLab6\4_5_6.jpg"]
for i, path in enumerate(paths):
    img = cv2.imread(path,flags=cv2.IMREAD_COLOR)
    blur_img = cv2.medianBlur(img, 101)
    gray_img = cv2.cvtColor(blur_img, cv2.COLOR_BGR2GRAY)
    #cv2.namedWindow("circles1",flags=cv2.WINDOW_AUTOSIZE)

    circles = circles = cv2.HoughCircles(
        cv2.bitwise_not(gray_img),
        cv2.HOUGH_GRADIENT,
        dp=2,
        minDist=800,
        param1=100,
        param2=200,
        minRadius=250,
        maxRadius=800,
    )
    draw_circles(circles, img)

    #cv2.imshow('circles1', img)
    cv2.imwrite("circles"+str(i)+".jpg",img)
    #cv2.waitKey(0)
