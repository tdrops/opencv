"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 7-10] 확률 허프 변환으로 선 검출
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/sudoku.jpg")
img2 = img.copy()

img_gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(image=img_gray, threshold1=50, threshold2=200)

lines = cv2.HoughLinesP(image=edges, rho=1, theta=np.pi/180, threshold=10, lines=None, minLineLength=20, maxLineGap=2)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img=img2, pt1=(x1,y1), pt2=(x2,y2), color=(0,255,0), thickness=1)

cv2.imshow(winname="hough", mat=np.hstack((img,img2)))
cv2.waitKey()
cv2.destroyAllWindows()


