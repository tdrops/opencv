"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-22] HSV 색상으로 마스킹
"""
import cv2
import numpy as np


img = cv2.imread(filename="../img/cube.jpg")
hsv = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2HSV)

blue1 = np.array([90, 50, 50])
blue2 = np.array([120, 255, 255])

green1 = np.array([45, 50, 50])
green2 = np.array([75, 255, 255])

red1 = np.array([0, 50, 50])
red2 = np.array([15, 255, 255])

red3 = np.array([165, 50, 50])
red4 = np.array([180, 255, 255])

yellow1 = np.array([20, 50, 50])
yellow2 = np.array([35, 255, 255])

mask_blue = cv2.inRange(src=hsv, lowerb=blue1, upperb=blue2)
mask_green = cv2.inRange(src=hsv, lowerb=green1, upperb=green2)
mask_red = cv2.inRange(src=hsv, lowerb=red1, upperb=red2)
mask_red2 = cv2.inRange(src=hsv, lowerb=red3, upperb=red4)
mask_yellow = cv2.inRange(src=hsv, lowerb=yellow1, upperb=yellow2)

res_blue = cv2.bitwise_and(src1=img, src2=img, mask=mask_blue)
res_green = cv2.bitwise_and(src1=img, src2=img, mask=mask_green)
res_red1 = cv2.bitwise_and(src1=img, src2=img, mask=mask_red)
res_red2 = cv2.bitwise_and(src1=img, src2=img, mask=mask_red2)
res_red = cv2.bitwise_or(src1=res_red1, src2=res_red2)
res_yellow = cv2.bitwise_and(src1=img, src2=img, mask=mask_yellow)

cv2.imshow(winname="res_blue", mat=res_blue)
cv2.imshow(winname="res_green", mat=res_green)
cv2.imshow(winname="res_red", mat=res_red)
cv2.imshow(winname="res_yellow", mat=res_yellow)

cv2.waitKey()
cv2.destroyAllWindows()
