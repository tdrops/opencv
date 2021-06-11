"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

filter2D 이미지 촛점 흐리기
"""


import cv2
import numpy as np

img = cv2.imread(filename="./img/girl.jpg")

kernel = np.full(shape=(5,5), fill_value=1/(5*5), dtype=np.float32)
# kernel = np.ones(shape=(5,5))/5**2

img2 = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="blur", mat=img2)

cv2.waitKey()
cv2.destroyAllWindows()
