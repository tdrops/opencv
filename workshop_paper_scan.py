"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 7-18] 문서 스캐너
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/paper.jpg")
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(src=gray, ksize=(3, 3), sigmaX=0)
edge = cv2.Canny(image=blur, threshold1=75, threshold2=200)

im, contours, hierarchy = cv2.findContours(image=edge, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
ctr = contours[0]
approx = cv2.approxPolyDP(curve=ctr, epsilon=cv2.arcLength(curve=ctr, closed=True) * 0.01, closed=True)
src = np.float32([approx[0][0], approx[1][0], approx[2][0], approx[3][0]])

x, y, w, h = cv2.boundingRect(points=approx)
dst = np.float32([[[0, 0]], [[0, 0 + h - 1]], [[0 + w - 1, h - 1]], [[w - 1, 0]]])
M = cv2.getPerspectiveTransform(src=src, dst=dst)

img2 = cv2.warpPerspective(src=img, M=M, dsize=(w, h))

cv2.imshow(winname="img", mat=img)
cv2.imshow(winname="img2", mat=img2)
cv2.waitKey()
cv2.destroyAllWindows()
