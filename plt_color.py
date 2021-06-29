"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 3-5] plot 의 색 지정
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(10)
y = x ** 2
plt.plot(x, y, 'r')
plt.show()
