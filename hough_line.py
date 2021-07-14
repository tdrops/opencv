"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 7-8] 허프 선 검출
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/sudoku.jpg")
img2 = img.copy()
h, w = img.shape[:2]

img_gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(image=img_gray, threshold1=100, threshold2=200)

lines = cv2.HoughLines(image=edges, rho=1, theta=np.pi/180, threshold=130)

for line in lines:
    r, theta = line[0]
    tx, ty = np.cos(theta), np.sin(theta)
    x0, y0 = tx * r, ty * r
    cv2.circle(img=img2, center=(abs(x0), abs(y0)), radius=3, color=(0,0,255), thickness=-1)

    x1, y1 = int(x0+w*(-ty)), int(y0+h*tx)
    x2, y2 = int(x0-w*(-ty)), int(y0-h*tx)

    cv2.line(img=img2, pt1=(x1,y1), pt2=(x2,y2), color=(0,255,0), thickness=1)

cv2.imshow(winname="hough line", mat=np.hstack((img,img2)))
cv2.waitKey()
cv2.destroyAllWindows()
