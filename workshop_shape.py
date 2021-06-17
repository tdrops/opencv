"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

요약요약요약요약요약요약요약요약요약요약요약요약요약요약요약요약요약요약요약요약
"""
import cv2
import numpy as np

img = cv2.imread(filename="./img/5shapes.jpg")
img2 = img.copy()

gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(src=gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)

_, contours, _ = cv2.findContours(image=th, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv2.approxPolyDP(curve=contour, epsilon=cv2.arcLength(curve=contour, closed=True) * 0.01, closed=True)
    len_approx = len(approx)
    mmt = cv2.moments(array=contour)
    cx = int(mmt["m10"] / mmt["m00"])
    cy = int(mmt["m01"] / mmt["m00"])
    name = "Unknown"
    color = (0, 0, 0)
    if len_approx == 3:
        name = "Triangle"
        color = (0, 255, 0)
    elif len_approx == 4:
        x, y, w, h = cv2.boundingRect(points=contour)
        if abs(w - h) <= 3:
            name = "Square"
            color = (0, 125, 255)
        else:
            name = "Rectagle"
            color = (255, 255, 0)
    elif len_approx == 10:
        name = "Star"
        color = (255, 255, 0)
    elif len_approx >= 11:
        name = "Circle"
        color = (0, 255, 255)
    cv2.drawContours(image=img2, contours=[contour], contourIdx=-1, color=color, thickness=-1)
    cv2.putText(img=img2, text=name, org=(cx, cy), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),
                thickness=1)

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="img2", mat=img2)
cv2.waitKey()
cv2.destroyAllWindows()
