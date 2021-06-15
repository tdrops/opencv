"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

컨투어 단순화
"""



import cv2
import numpy as np


img = cv2.imread(filename="./img/bad_rect.png")
img2 = img.copy()

img_gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
ret,img_gray = cv2.threshold(src=img_gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

temp,contours,hierarchy = cv2.findContours(image=img_gray, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
contour = contours[0]
epsilon = cv2.arcLength(curve=contour, closed=True) * 0.05
approx = cv2.approxPolyDP(curve=contour, epsilon=epsilon, closed=True)

cv2.drawContours(image=img, contours=[contour], contourIdx=-1, color=(0,255,0), thickness=1)
cv2.drawContours(image=img2, contours=[approx], contourIdx=-1, color=(0,255,0), thickness=1)

cv2.imshow(winname="img", mat=img)
cv2.imshow(winname="img2", mat=img2)

cv2.waitKey()
cv2.destroyAllWindows()
