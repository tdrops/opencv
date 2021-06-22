"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

필기체 숫자를 10가지로 분류하고 중앙 값을 표시
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import mnist


data, _ = mnist.getData()

criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, label, center = cv2.kmeans(data=data, K=10, bestLabels=None, criteria=criteria, attempts=10, flags=cv2.KMEANS_RANDOM_CENTERS)

for i in range(10):
    cent_img = center[i].reshape(20,20).astype(np.uint8)
    plt.subplot(2,5, i+1)
    plt.imshow(X=cent_img, cmap="gray")
    plt.xticks([])
    plt.yticks([])
plt.show()
