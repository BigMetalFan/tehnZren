import cv2
import numpy as np


path = r".\pictures\tzLab7\task.png"

def log_hu(m):
    hu = cv2.HuMoments(m).flatten()
    return -np.sign(hu) * np.log10(np.abs(hu) + 1e-300)

def find_deepest(hierarchy):
    max_depth = -1
    deepest_contour_idx = -1
    for idx, info in enumerate(hierarchy[0]):
        next_idx, prev_idx, first_child, parent = info

        if first_child == -1:
            current_depth = 0
            current_parent = parent

            while current_parent != -1:
                current_depth += 1
                current_parent = hierarchy[0,current_parent][3]
 
            if current_depth > max_depth:
                max_depth = current_depth
                deepest_contour_idx = idx
    return deepest_contour_idx

img = cv2.imread(path, flags=cv2.IMREAD_COLOR)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
_, thresh_img = cv2.threshold(gray_img,240, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

sampleId = find_deepest(hierarchy)

sample = cv2.moments(contours[find_deepest(hierarchy)])

#sampleHu = cv2.HuMoments(sample)
sampleLH = log_hu(sample)
print(sampleLH)
cv2.drawContours(img, contours, sampleId, (0, 0, 255), 2)
similar = []

for i, contour in enumerate(contours):
    if i == sampleId: continue

    currentMoments = cv2.moments(contour)
    currentMomentsHu = cv2.HuMoments(currentMoments)
    currentMomentsLH = log_hu(currentMoments)
    if abs((currentMomentsLH[3] - sampleLH[3])/sampleLH[3])<0.1:
        similar.append(i)

for i in similar:
    cv2.drawContours(img, contours, i, (0, 0, 0), 2)
cv2.imshow('Contours2', img)
cv2.imwrite("Contours2"+".jpg",img)
cv2.waitKey(0)