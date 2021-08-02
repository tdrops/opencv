"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 9-4] k-means 로 MNIST 손글씨 숫자 군집화
"""
import cv2
import numpy as np

import matplotlib.pyplot as plt
import mnist

data, _ = mnist.getData()

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

ret, label, center = cv2.kmeans(data=data, K=10, bestLabels=None, criteria=criteria, attempts=10,
                                flags=cv2.KMEANS_RANDOM_CENTERS)

for i in range(10):
    cent_img = center[i].reshape(20, 20).astype(np.uint8)
    plt.subplot(2, 5, i + 1)
    plt.imshow(X=cent_img, cmap="gray")
    plt.xticks([])
    plt.yticks([])

plt.show()
