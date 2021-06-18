"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

cornerHarris - 코너 찾기
"""
import cv2
import numpy as np


img = cv2.imread(filename="./img/house.jpg")
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

corner = cv2.cornerHarris(src=gray, blockSize=2,ksize=3,k=0.04)
coords = np.where(corner > corner.max()*0.1)
coords = np.stack((coords[1],coords[0]), axis=-1)

for coord in coords:
    cv2.circle(img=img, center=(coord[0],coord[1]), radius=1, color=(0,0,255), thickness=1)

corner_nom = cv2.normalize(src=corner, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
corner_nom = cv2.cvtColor(src=corner_nom, code=cv2.COLOR_GRAY2BGR)

cv2.imshow(winname="original", mat=np.hstack((corner_nom,img)) )

cv2.waitKey()
cv2.destroyAllWindows()
