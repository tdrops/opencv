"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 9-9] SVM 난수 분류
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


a = np.random.randint(low=0, high=158, size=(25,2))

b = np.random.randint(low=98, high=255, size=(25,2))

trainData = np.vstack((a,b)).astype(np.float32)

responses = np.zeros(shape=(50,1), dtype=np.int32)

responses[25:] = 1

red = trainData[responses.ravel()==0]
plt.scatter(x=red[:,0], y=red[:,1], s=80, c="r", marker="^")

blue = trainData[responses.ravel()==1]
plt.scatter(x=blue[:,0], y=blue[:,1], s=80, c="b", marker="s")

newcomer = np.random.randint(low=0, high=255, size=(1,2)).astype(np.float32)
plt.scatter(x=newcomer[:,0], y=newcomer[:,1], s=80, c="g", marker="o")

svm = cv2.ml.SVM_create()
svm.trainAuto(trainData, cv2.ml.ROW_SAMPLE, responses)

svm.save("./svm_random.xml")

svm2 = cv2.ml.SVM_load("./svm_random.xml")

ret, results = svm2.predict(newcomer)

plt.annotate("red" if results[0]==0 else "blue", xy=newcomer[0], xytext=newcomer[0]+1)

plt.show()







