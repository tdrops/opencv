"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

findContours
"""



import cv2
import numpy as np


img = cv2.imread(filename="./img/shapes.png")
img2 = img.copy()

img_gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
ret, img_gray = cv2.threshold(src=img_gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)

im2,contour1,hierarchy = cv2.findContours(image=img_gray, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
im2,contour2,hierarchy = cv2.findContours(image=img_gray, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

print(f"len(contour1):{len(contour1)} len(contour2):{len(contour2)}")

cv2.drawContours(image=img, contours=contour1, contourIdx=-1, color=(0,255,0), thickness=4)
cv2.drawContours(image=img2, contours=contour2, contourIdx=-1, color=(0,255,0), thickness=4)

for i in contour1:
    for j in i:
        cv2.circle(img=img, center=tuple(j[0]), radius=1, color=(255, 0, 0), thickness=-1)

for i in contour2:
    for j in i:
        cv2.circle(img=img2, center=tuple(j[0]), radius=1, color=(255, 0, 0), thickness=-1)

cv2.imshow(winname="img", mat=img)
cv2.imshow(winname="img2", mat=img2)

cv2.waitKey()
cv2.destroyAllWindows()
