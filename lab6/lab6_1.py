import cv2
import numpy as np
import math

def draw_line(line, img, color=(0, 0, 255), thickness=1, lineType=cv2.LINE_AA): 
    rho, theta = line[0]
    cos_t = math.cos(theta) 
    sin_t = math.sin(theta) 
    x0 = cos_t * rho 
    y0 = sin_t * rho 
    pt1 = int(x0 - 1000 * sin_t), int(y0 + 1000 * cos_t) 
    pt2 = int(x0 + 1000 * sin_t), int(y0 - 1000 * cos_t) 
    cv2.line(img, pt1, pt2, color, thickness, lineType) 


def draw_lines(lines, img, color=(0, 0, 255), thickness=1):
    for line in lines:
        draw_line(line, img, color, thickness)
    

if __name__ == '__main__':

    path = r".\pictures\tzLab6\4_1.jpg"

    img = cv2.imread(path, flags=cv2.IMREAD_COLOR)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary_img = cv2.threshold(gray_img,100,255,cv2.THRESH_BINARY_INV)

    cv2.namedWindow("Linii",flags=cv2.WINDOW_AUTOSIZE)

    lines = cv2.HoughLines(binary_img,1,np.pi/180,300)

    draw_lines(lines, img, color = (255,255,255), thickness = 10)
    
    cv2.imshow('Linii', img)
    cv2.imwrite("Linii1"+".jpg",img)
    cv2.waitKey(0)
