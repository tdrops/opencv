"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 5-2] 행렬을 이용한 확대와 축소
"""
import cv2
import numpy as np


img = cv2.imread(filename="../img/fish.jpg")
h,w = img.shape[:2]
m_small = np.float32([[0.5,0,0],[0,0.5,0]])
m_big = np.float32([[2,0,0],[0,2,0]])
result1 = cv2.warpAffine(src=img, M=m_small, dsize=(w,h))
result2 = cv2.warpAffine(src=img, M=m_big, dsize=(w*2,h*2))
result3 = cv2.warpAffine(src=img, M=m_small, dsize=(w,h), dst=None, flags=cv2.INTER_AREA)
result4 = cv2.warpAffine(src=img, M=m_big, dsize=(w*2,h*2), dst=None, flags=cv2.INTER_CUBIC)

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="result1", mat=result1)
cv2.imshow(winname="result2", mat=result2)
cv2.imshow(winname="result3", mat=result3)
cv2.imshow(winname="result4", mat=result4)
cv2.waitKey()
cv2.destroyAllWindows()
