"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 9-6] k-NN 영화 장류 분류
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

trainData = np.random.randint(low=0, high=100, size=(25, 2)).astype(np.float32)
responses = (trainData[:, 0] > trainData[:, 1]).astype(np.float32)

action = trainData[responses.ravel() == 0]
ramantic = trainData[responses.ravel() == 1]
plt.scatter(x=action[:, 0], y=action[:, 1], s=80, c="b", marker="^", label="action")
plt.scatter(x=ramantic[:, 0], y=ramantic[:, 1], s=80, c="r", marker="o", label="ramantic")

newcomer = np.random.randint(low=0, high=100, size=(1, 2)).astype(np.float32)
plt.scatter(x=newcomer[:, 0], y=newcomer[:, 1], s=200, c="g", marker="s", label="new")

knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)

ret, results, neighbors, dist = knn.findNearest(newcomer, 3)
print('ret:%s, result:%s, negibours:%s, distance:%s' % (ret, results, neighbors, dist))

anno_x, anno_y = newcomer.ravel()
label = "action" if results == 0.0 else "ramantic"
plt.annotate(label, xy=(anno_x + 1, anno_y + 1), xytext=(anno_x + 5, anno_y + 10), arrowprops={'color': 'black'})
plt.xlabel('kiss')
plt.ylabel('kick')
plt.legend(loc="upper right")
plt.show()
