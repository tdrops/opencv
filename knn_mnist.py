"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 9-7] knn 으로 MNIST 손글씨 숫자 학습
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import mnist

train, train_labels = mnist.getTrain()
test, test_labels = mnist.getTest()

knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

for k in range(1, 11):
    ret, result, neighbors, distance = knn.findNearest(test, k=k)

    correct = np.sum(result == test_labels)
    accuracy = correct * 100.0 / result.size
    print("K:%d, Accuracy : %.2f%%(%d%d)" %(k, accuracy, correct, result.size))








