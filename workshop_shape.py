"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 7-17] 도형 알아맞히기 워크숍
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/5shapes.jpg")
img2 = img.copy()

gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(src=gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)

im, contours, hierarchy = cv2.findContours(image=th, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image=img, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=1)

for countour in contours:
    approx = cv2.approxPolyDP(curve=countour, epsilon=cv2.arcLength(curve=countour, closed=True) * 0.01, closed=True)
    # 10 star?
    # 16 circle?
    # 3 triangle
    # 4 rectangle
    # 4 rectangle

    vertices = len(approx)

    mnt = cv2.moments(array=countour)

    cx, cy = int(mnt['m10'] / mnt['m00']), int(mnt['m01'] / mnt['m00'])

    name = "Unknown"

    if vertices == 3:
        name = "Triangle"
        color = (0, 255, 0)
    elif vertices == 4:
        x, y, w, h = cv2.boundingRect(points=countour)
        if abs(w - h) <= 3:
            name = "Square"
            color = (0, 125, 255)
        else:
            name = "Rectangle"
            color = (0, 0, 255)
    elif vertices == 10:
        name = "Star"
        color = (255, 255, 0)
    elif vertices >= 15:
        name = "Circle"
        color = (0, 255, 255)

    cv2.drawContours(image=img2, contours=[countour], contourIdx=-1, color=color, thickness=-1)
    cv2.putText(img=img2, text=name, org=(cx - 50, cy), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1,
                color=(100, 100, 100), thickness=1)

cv2.imshow(winname="5shapes", mat=np.hstack((img, img2)))
cv2.waitKey()
cv2.destroyAllWindows()
