"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 3-1] NumPy 배열로 체크무늬 그레이 스케일 이미지 생성
"""
import cv2
import numpy as np


img = np.zeros(shape=(120,120), dtype=np.uint8)
img[25:35,:] = 45
img[55:65,:] = 115
img[85:95,:] = 160
img[:,35:45] = 205
img[:,75:85] = 255
cv2.imshow(winname="img", mat=img)
cv2.waitKey()
cv2.destroyAllWindows()
