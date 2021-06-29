"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 3-3] plot 그리기
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


a = np.array([2, 6, 7, 3, 12, 8, 4, 5])
plt.plot(a)
plt.show()
