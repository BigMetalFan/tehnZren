import cv2

path = r"../pictures/tzLab3/2-1.jpg"

img = cv2.imread(path,flags=cv2.IMREAD_COLOR)
window = cv2.namedWindow("window",flags=cv2.WINDOW_AUTOSIZE )

cv2.imshow("window", img)
cv2.waitKey(0)

#def oppening():
    #cv2.dilate()
    #cv2.erode()
    
    