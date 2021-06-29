"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 3-4] y = x**2 그래프 그리기
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(10)
y = x ** 2
plt.plot(x, y)
plt.show()
