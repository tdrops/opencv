"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

kmeans 로 임이의 가까운 것 으로 묶음
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


a = np.random.randint(low=0, high=150, size=(25,2))
b = np.random.randint(low=128, high=255, size=(25,2))

data = np.vstack((a,b)).astype(dtype=np.float32)


criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, label, center = cv2.kmeans(data=data, K=2, bestLabels=None, criteria=criteria, attempts=10, flags=cv2.KMEANS_RANDOM_CENTERS)

red = data[label.ravel()==0]
blue = data[label.ravel()==1]

plt.scatter(x=red[:,0], y=red[:,1], c="r")
plt.scatter(x=blue[:,0], y=blue[:,1], c="b")

plt.scatter(x=center[0,0], y=center[0,1], s=100, c="r", marker="s")
plt.scatter(x=center[1,0], y=center[1,1], s=100, c="b", marker="s")

plt.show()
