import cv2

path = r"D:\Main\Pituxon\zren\pictures\tzLab1\1-1.jpg"

img = cv2.imread(path,flags=cv2.IMREAD_COLOR)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh_img = cv2.threshold(gray_img,100, 255, cv2.THRESH_BINARY)
adaptive_tresh_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                cv2.THRESH_BINARY, 401 ,15)
autoret, auto_tresh_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

window = cv2.namedWindow("window",flags=cv2.WINDOW_AUTOSIZE )
windowA = cv2.namedWindow("windowA",flags=cv2.WINDOW_AUTOSIZE )
windowAuto = cv2.namedWindow("windowAuto",flags=cv2.WINDOW_AUTOSIZE )


cv2.imshow("window", thresh_img)
cv2.imshow("windowA", adaptive_tresh_img)
cv2.imshow("windowAuto", auto_tresh_img)
cv2.waitKey(0)