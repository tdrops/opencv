"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

blur boxFilter 함수로 촛점 흐리기
"""


import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread(filename="./img/taekwonv1.jpg")
img2 = cv2.blur(src=img, ksize=(10, 10))
img3 = cv2.boxFilter(src=img, ddepth=-1, ksize=(10,10))
cv2.imshow(winname="blur", mat=np.hstack([img, img2, img3]))

cv2.waitKey()
cv2.destroyAllWindows()
