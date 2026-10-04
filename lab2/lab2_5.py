import cv2

path = r"..\pictures\tzLab1\1-4.png"

img = cv2.imread(path,flags=cv2.IMREAD_COLOR)


blur_img = cv2.blur(img, (7,7))
gaus_img = cv2.GaussianBlur(img,(7,7),0.9)
median_img = cv2.medianBlur(img, 21)
bilateral_img = cv2.bilateralFilter(img, 9, 250, 75)

window = cv2.namedWindow("window",flags=cv2.WINDOW_AUTOSIZE )
windowBlur = cv2.namedWindow("windowBlur",flags=cv2.WINDOW_AUTOSIZE )
windowGaus = cv2.namedWindow("windowGaus",flags=cv2.WINDOW_AUTOSIZE )
windowMedian = cv2.namedWindow("windowMedian",flags=cv2.WINDOW_AUTOSIZE )
windowBilateral = cv2.namedWindow("windowBilateral",flags=cv2.WINDOW_AUTOSIZE )

cv2.imshow("window", img)
cv2.imshow("windowBlur", blur_img)
cv2.imshow("windowGaus", gaus_img)
cv2.imshow("windowMedian", median_img)
cv2.imshow("windowBilateral", bilateral_img)

cv2.waitKey(0)