"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 3-6] 다양한 스타일 지정
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(10)
f1 = x * 5
f2 = x ** 2
f3 = x ** 2 + x * 2

plt.plot(x, 'r--')
plt.plot(f1, 'g.')
plt.plot(f2, 'bv')
plt.plot(f3, 'ks')
plt.show()
