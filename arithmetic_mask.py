"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

mask 와 누적 할당 연산
"""
import cv2
import numpy as np


a = np.array([[1,2]], dtype=np.uint8)
b = np.array([[10,20]], dtype=np.uint8)
mask = np.array([[1,0]], dtype=np.uint8)

c1 = cv2.add(src1=a, src2=b, dst=None, mask=mask)
print(c1)
c2 = cv2.add(src1=a, src2=b, dst=b, mask=mask)
print(c2)
