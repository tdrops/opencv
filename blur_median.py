"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

medianBlur 를 사용한 노이즈 제거
"""


import cv2
import numpy as np


img = cv2.imread(filename="./img/salt_pepper_noise.jpg")

img2 = cv2.medianBlur(src=img, ksize=5)

cv2.imshow(winname="median blur", mat=np.hstack([img,img2]))

cv2.waitKey()
cv2.destroyAllWindows()
