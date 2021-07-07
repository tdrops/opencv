"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-31] 2D 히스토그램
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('classic')
img = cv2.imread(filename="../img/mountain.jpg")

plt.subplot(131)
hist = cv2.calcHist(images=[img], channels=[0, 1], mask=None, histSize=[32, 32], ranges=[0, 256, 0, 256])
p = plt.imshow(hist)
plt.title("x:Blue y:Green")
plt.colorbar(mappable=p)

plt.subplot(132)
hist = cv2.calcHist(images=[img], channels=[1, 2], mask=None, histSize=[32, 32], ranges=[0, 256, 0, 256])
p = plt.imshow(hist)
plt.title("x:Green y:Red")
plt.colorbar(mappable=p)

plt.subplot(133)
hist = cv2.calcHist(images=[img], channels=[0, 2], mask=None, histSize=[32, 32], ranges=[0, 256, 0, 256])
p = plt.imshow(hist)
plt.title("x:Blue y:Red")
plt.colorbar(mappable=p)

plt.show()
