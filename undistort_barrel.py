"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

cv2.undistort 를 이용한 사진 왜곡 
"""

import cv2
import numpy as np
import matplotlib.pylab as plt

img = np.full(shape=(300, 400, 3), fill_value=255, dtype=np.uint8)
h, w = img.shape[:2]  # 높이, 폭 구하기

img[::10, :, :] = 0  # 매 10 픽셀마다 검은색 선 긋기
img[:, ::10, :] = 0

fx = 10
fy = 10
cx = w / 2
cy = h / 2
cameraMatrix = np.float32([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])  # 카메라 행렬

# distCoeffs = ( 0.001 , 0, 0, 0)
distCoeffs = (-0.0005, 0, 0, 0)  # 왜곡 계수 지정

result = cv2.undistort(src=img, cameraMatrix=cameraMatrix, distCoeffs=distCoeffs)  # 왜곡 적용

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="result", mat=result)

cv2.waitKey()
cv2.destroyAllWindows()
