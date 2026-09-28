import cv2

def calc_next_time(time):
    return 4000 if time + 2000 > 11000 else time + 2000

path = r"D:\Main\Pituxon\zren\pictures\tzLab1\1-1.jpg"

img = cv2.imread(path,flags=cv2.IMREAD_COLOR)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
resized_gray_img = cv2.resize(gray_img, (0, 0), fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
b, g, r = cv2.split(img)
swapped_img = cv2.merge([b, r, g])

imageList = [img, gray_img, resized_img, resized_gray_img, swapped_img ] 

time = 5000

for i, image in enumerate(imageList):
    window = cv2.namedWindow("window",flags=cv2.WINDOW_AUTOSIZE )
    cv2.imshow("window", image)
    if(i != len(imageList)-1):
        cv2.waitKey(time)& 0xFF == 27
        time = calc_next_time(time)
        cv2.destroyWindow("window")
    else:
        while time>0:
            if cv2.waitKey(1) & 0xFF == 27:
                break
            else: time -= 1
        cv2.destroyWindow("window")



