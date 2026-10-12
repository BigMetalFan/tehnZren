import cv2
import numpy as np

paths = [r".\pictures\tzLab4\3-1.jpg", r".\pictures\tzLab4\3-2.jpg", r".\pictures\tzLab4\3-3.jpg"]

imgs = [ cv2.imread(path,flags=cv2.IMREAD_COLOR) for path in paths]
greyimgs = [ cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in imgs]

sobelImgs = [cv2.Sobel(img, cv2.CV_32F, 1, 1, 3, 1) for img in greyimgs]
laplasImgs = [cv2.Laplacian(img, cv2.CV_32F, 3, 1) for img in greyimgs]

for img in sobelImgs:
    cv2.imshow("Sobel "+str(img), img)

for img in laplasImgs:
    cv2.imshow("Laplas "+str(img), img)

cv2.waitKey(0)
