"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

컨투어를 감싸는 도형 그리기
"""



import cv2
import numpy as np


img = cv2.imread(filename="./img/lightning.png")
img_gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(src=img_gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)
img2,contours,hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
contr = contours[0]
x,y,w,h = cv2.boundingRect(points=contr)
cv2.rectangle(img=img, pt1=(x,y), pt2=(x+w,y+h), color=(0,0,0), thickness=1)
rect = cv2.minAreaRect(points=contr)
box = cv2.boxPoints(box=rect)
box = np.int0(box)
cv2.drawContours(image=img, contours=[box], contourIdx=-1, color=(0,255,0))

(x,y),r = cv2.minEnclosingCircle(points=contr)
cv2.circle(img=img, center=(int(x),int(y)), radius=int(r), color=(255,0,0), thickness=1)


ret,tri = cv2.minEnclosingTriangle(points=contr)
cv2.polylines(img=img, pts=[np.int32(tri)], isClosed=True, color=(255,0,255), thickness=1)

ellipse = cv2.fitEllipse(points=contr)
cv2.ellipse(img, ellipse, (0,255,255), 1)

(vx,vy,x,y) = cv2.fitLine(points=contr, distType=cv2.DIST_L2, param=0, reps=0.01, aeps=0.01)
cols,rows = img.shape[:2]
cv2.line(img=img, pt1=(0,0-x*(vy/vx)+y), pt2=(cols-1, (cols-x)*(vy/vx)+y), color=(0,0,255), thickness=1)

cv2.imshow(winname="original", mat=img)

cv2.waitKey()
cv2.destroyAllWindows()
