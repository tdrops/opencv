"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 6-1] 평균 필터를 생성해서 블러 적용
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/girl.jpg")

kernel = np.ones(shape=(5,5))/(5*5)
blured = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)

cv2.imshow(winname="origin", mat=img)
cv2.imshow(winname="blured", mat=blured)
cv2.waitKey()
cv2.destroyAllWindows()
