import cv2

path = r"D:\Main\Pituxon\zren\pictures\tzLab1\1-5.jpg"

img = cv2.imread(path,flags=cv2.IMREAD_COLOR)

window = cv2.namedWindow("window",flags=cv2.WINDOW_AUTOSIZE )

median_img = cv2.medianBlur(img, 51)
bilateral_img = cv2.bilateralFilter(median_img, 5, 50, 75)
gaus_img = cv2.GaussianBlur(median_img,(5,5),0.5)


cv2.imshow("window", gaus_img)
cv2.waitKey(0)