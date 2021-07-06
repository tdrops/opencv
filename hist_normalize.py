"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-27] 히스토그램 정규화
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(filename="../img/abnormal.jpg", flags=cv2.IMREAD_GRAYSCALE)

img_min = img.min()
img_max = img.max()

img_f = img.astype(np.float32)
img_norm = np.uint8((img_f - img_f.min()) * 255 / (img_f.max()-img_f.min()))
img_norm = img_norm.astype(np.uint8)

img_norm2 = cv2.normalize(src=img, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

hist = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[255], ranges=[0,255])
hist_norm = cv2.calcHist(images=[img_norm], channels=[0], mask=None, histSize=[255], ranges=[0,255])
hist_norm2 = cv2.calcHist(images=[img_norm2], channels=[0], mask=None, histSize=[255], ranges=[0,255])

cv2.imshow(winname="img:img_new", mat=np.hstack((img, img_norm, img_norm2)))

plt.subplot(1,3,1)
plt.plot(hist)
plt.subplot(1,3,2)
plt.plot(hist_norm)
plt.subplot(1,3,3)
plt.plot(hist_norm2)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
