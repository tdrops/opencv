"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 3-2] NumPy 배열로 체크무의 BGR 스케일 이미지 생성
"""
import cv2
import numpy as np


img = np.zeros(shape=(120,120,3), dtype=np.uint8)
img[25:35,:] = [255,0,0]
img[55:65,:] = [0,255,0]
img[85:95,:] = [0,0,255]
img[:,35:45] = [255,255,0]
img[:,75:85] = [255,0,255]
cv2.imshow(winname="img", mat=img)
cv2.waitKey()
cv2.destroyAllWindows()
