import cv2

path = r"D:\Main\Pituxon\zren\pictures\tzLab1\1-4.png"

img = cv2.imread(path,flags=cv2.IMREAD_COLOR)
#img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

blur_img = cv2.blur(img, (5,5))
gaus_img = cv2.GaussianBlur(img,(5,5),0.5)
median_img = cv2.medianBlur(img, 3)
bilateral_img = cv2.bilateralFilter(img, 5, 50, 75)

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