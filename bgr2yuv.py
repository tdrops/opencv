"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-8] BGR 에서 YUV 로 변환
"""
import cv2
import numpy as np


dark = np.array([[[0,0,0]]], dtype=np.uint8)
middle = np.array([[[127,127,127]]], dtype=np.uint8)
bright = np.array([[[255,255,255]]], dtype=np.uint8)

dark_yuv = cv2.cvtColor(src=dark, code=cv2.COLOR_BGR2YUV)
middle_yuv = cv2.cvtColor(src=middle, code=cv2.COLOR_BGR2YUV)
bright_yuv = cv2.cvtColor(src=bright, code=cv2.COLOR_BGR2YUV)

print(f"dark_yuv:{dark_yuv}")
print(f"middle_yuv:{middle_yuv}")
print(f"bright_yuv:{bright_yuv}")
