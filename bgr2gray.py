"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-5] BGR 을 그레이 스케일로 변환
"""
import cv2
import numpy as np


img = cv2.imread(filename="../img/girl.jpg")

img2 = img.astype(np.uint16)
r,g,b = cv2.split(m=img2)
gray1 = ((r+g+b)/3).astype(np.uint8)

gray2 = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

cv2.imshow(winname="img", mat=img)
cv2.imshow(winname="gray1", mat=gray1)
cv2.imshow(winname="gray2", mat=gray2)

cv2.waitKey()
cv2.destroyAllWindows()
