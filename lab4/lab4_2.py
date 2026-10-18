import cv2
import numpy as np

paths = [r".\pictures\tzLab1\1-4.png", r".\pictures\tzLab1\1-2.jpg"]

imgs = [ cv2.imread(path,flags=cv2.IMREAD_COLOR) for path in paths]
grayimgs = [ cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in imgs]

filtredimg = []
filtredimg.append(cv2.medianBlur(grayimgs[0], 3))
filtredimg.append(cv2.GaussianBlur(grayimgs[1],(5,5),0.5))

cannyImgs = []
cannyImgs.append(cv2.Canny(filtredimg[0], 100, 200, 15 )) 
cannyImgs.append(cv2.Canny(filtredimg[1], 100, 200, 5 ))

for img in cannyImgs:
    cv2.imshow("Canny "+str(id(img)), img)
    cv2.imwrite("lab4/Canny"+str(id(img))+".jpg",cv2.convertScaleAbs(img))

cv2.waitKey(0)
