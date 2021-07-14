"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 7-6] 볼록 선체
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/hand.jpg")
img2 = img.copy()

gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(src=gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)

im, contours, hierarchy = cv2.findContours(image=th, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

cntr = contours[0]
cv2.drawContours(image=img, contours=[cntr], contourIdx=-1, color=(0,255,0), thickness=1)

hull = cv2.convexHull(points=cntr)
cv2.drawContours(image=img2, contours=[hull], contourIdx=-1, color=(0,255,0), thickness=1)

hull2 = cv2.convexHull(points=cntr, returnPoints=False)

defects = cv2.convexityDefects(contour=cntr, convexhull=hull2)

for i in range(defects.shape[0]):
    startP, endP, farthestP, distance = defects[i, 0]

    farthest = tuple(cntr[farthestP][0])

    dist = distance / 256.0

    if dist > 1:
        cv2.circle(img=img2, center=farthest, radius=3, color=(0,0,255), thickness=-1)

cv2.imshow(winname="contour", mat=img)
cv2.imshow(winname="convex hull", mat=img2)
cv2.waitKey()
cv2.destroyAllWindows()
