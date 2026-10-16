import cv2
import numpy as np

paths = [r".\pictures\tzLab1\1-4.png", r".\pictures\tzLab1\1-2.jpg"]

imgs = [ cv2.imread(path,flags=cv2.IMREAD_COLOR) for path in paths]
greyimgs = [ cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in imgs]

#cannyImgs = [cv2.Canny(img, 100, 200, 5 ) for img in greyimgs]
cannyImgs = []
cannyImgs.append(cv2.Canny(greyimgs[0], 120, 250, 3 )) 
cannyImgs.append(cv2.Canny(greyimgs[1], 100, 200, 5 ))

for img in cannyImgs:
    cv2.imshow("Canny "+str(id(img)), img)
    cv2.imwrite("lab4/Canny"+str(id(img))+".jpg",cv2.convertScaleAbs(img))

cv2.waitKey(0)
