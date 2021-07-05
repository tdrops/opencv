"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-26] 컬러 히스토그램
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread(filename="../img/mountain.jpg")
cv2.imshow(winname="img", mat=img)

channels = cv2.split(m=img)
colors = ('b', 'g', 'r')
for (ch, color) in zip(channels, colors):
    hist = cv2.calcHist(images=[ch], channels=[0], mask=None, histSize=[256], ranges=[0,256])
    plt.plot(hist, color=color)

plt.show()
