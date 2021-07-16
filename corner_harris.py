"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 8-4] 해리스 코너 검출
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/house.jpg")
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

corner = cv2.cornerHarris(src=gray, blockSize=2, ksize=3, k=0.04)
coord = np.where(corner > corner.max() * 0.1)
coord = np.stack((coord[1], coord[0]), axis=1)

for x, y in coord:
    cv2.circle(img=img, center=(x, y), radius=5, color=(0, 0, 255), thickness=1, lineType=cv2.LINE_AA)

corner_norm = cv2.normalize(src=corner, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
corner_num = cv2.cvtColor(src=corner_norm, code=cv2.COLOR_GRAY2BGR)

cv2.imshow(winname="corner/original", mat=np.hstack((corner_num, img)))
cv2.waitKey()
cv2.destroyAllWindows()
