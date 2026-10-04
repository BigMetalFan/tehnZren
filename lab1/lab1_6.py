import cv2

path = r"..\pictures\tzLab1\1-5.jpg"

img = cv2.imread(path,flags=cv2.IMREAD_COLOR)

window = cv2.namedWindow("window",flags=cv2.WINDOW_AUTOSIZE )

median_img = cv2.medianBlur(img, 51)

cv2.imshow("window", median_img)
cv2.waitKey(0)