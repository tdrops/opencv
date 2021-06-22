"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

가까운 점의 색 맞추기
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


trainData = np.random.randint(low=0, high=100, size=(25, 2)).astype(np.float32)
labels = np.random.randint(low=0, high=2, size=(25,1))

red = trainData[labels.ravel()==0]
blue = trainData[labels.ravel()==1]

plt.scatter(x=red[:,0], y=red[:,1], s=80, c="r", marker="^")
plt.scatter(x=blue[:,0], y=blue[:,1], s=80, c="b", marker="s")

newcommer = np.random.randint(low=0, high=100, size=(1, 2)).astype(np.float32)
plt.scatter(x=newcommer[:,0], y=newcommer[:,1], s=80, c="g", marker="o")

knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, labels)

ret, results, neighbors, dist = knn.findNearest(newcommer, 3)

print(f"ret:{ret}, results:{results}, neighbors:{neighbors}, dist:{dist}")

plt.annotate("red" if ret==0.0 else "blue", xy=newcommer[0], xytext=(newcommer[0]+1))

plt.show()
