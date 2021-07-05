"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-25] 그레이 스케일 1채널 히스토그램
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread(filename="../img/mountain.jpg", flags=cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[256], ranges=[0,256])

plt.plot(hist)
plt.show()
