"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 3-10] 여러 이미지 동시 출력
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


img1 = cv2.imread(filename="../img/model.jpg")
img2 = cv2.imread(filename="../img/model2.jpg")
img3 = cv2.imread(filename="../img/model3.jpg")

plt.subplot(1,3,1)
plt.imshow(img1[:,:,(2,1,0)])

plt.subplot(1,3,2)
plt.imshow(img2[:,:,::-1])

plt.subplot(1,3,3)
plt.imshow(img3[:,:,::-1])

plt.show()
