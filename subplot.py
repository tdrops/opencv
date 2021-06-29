"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 3-8] subplot
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(10)

plt.subplot(2,2,1)
plt.plot(x, x**2)

plt.subplot(2,2,2)
plt.plot(x, x*5)

plt.subplot(223)
plt.plot(x, np.sin(x))

plt.subplot(224)
plt.plot(x, np.cos(x))

plt.show()
