"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 9-2] 16 컬러 군집화
"""
import cv2
import numpy as np

K = 16
img = cv2.imread(filename="../img/taekwonv1.jpg")

data = img.reshape((-1,3)).astype(np.float32)

criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

ret, label, center = cv2.kmeans(data=data, K=K, bestLabels=None, criteria=criteria, attempts=10, flags=cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)
print(center)

res = center[label.flatten()]

res = res.reshape(img.shape)

cv2.imshow(winname="original/result", mat=np.hstack((img,res)))
cv2.waitKey()
cv2.destroyAllWindows()
