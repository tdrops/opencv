"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 3-8] plot 으로 이미지 출력
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread(filename="../img/girl.jpg")
plt.imshow(img)
plt.show()
