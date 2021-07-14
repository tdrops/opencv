"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 7-11] 허프 원 검출 
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/coins_spread1.jpg")

gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(src=gray, ksize=(3, 3), sigmaX=0)

circles = cv2.HoughCircles(image=blur, method=cv2.HOUGH_GRADIENT, dp=1.5, minDist=30, circles=None, param1=200)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(img=img, center=(i[0], i[1]), radius=i[2], color=(0, 255, 0), thickness=2)
        cv2.circle(img=img, center=(i[0], i[1]), radius=2, color=(0, 0, 255), thickness=5)

cv2.imshow(winname="hough circle", mat=img)
cv2.waitKey()
cv2.destroyAllWindows()
