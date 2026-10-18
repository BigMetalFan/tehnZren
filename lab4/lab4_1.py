import cv2
import numpy as np

paths = [r".\pictures\tzLab4\3-1.jpg", r".\pictures\tzLab4\3-2.jpg", r".\pictures\tzLab4\3-3.jpg"]

imgs = [ cv2.imread(path,flags=cv2.IMREAD_COLOR) for path in paths]
grayimg = [ cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in imgs]

sobelImgsX = [cv2.Sobel(img, cv2.CV_32F, 1, 0, 3, 1) for img in grayimg]
sobelImgsY = [cv2.Sobel(img, cv2.CV_32F, 0, 1, 3, 1) for img in grayimg]
sobelImgs = [cv2.magnitude(sobelImgsX[i], sobelImgsY[i]) for i in range(len(grayimg))]
laplasImgs = [cv2.Laplacian(img, cv2.CV_32F, 3, 1) for img in grayimg]

for img in sobelImgs:
    cv2.imshow("Sobel "+str(id(img)), cv2.convertScaleAbs(img))
    cv2.imwrite("lab4/Sobel"+str(id(img))+".jpg",cv2.convertScaleAbs(img))

for img in laplasImgs:
    cv2.imshow("Laplas "+str(id(img)), cv2.convertScaleAbs(img))
    cv2.imwrite("lab4/Laplas"+str(id(img))+".jpg",cv2.convertScaleAbs(img))


cv2.waitKey(0)
