"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-30] CLAHE 적용
"""
import cv2
import numpy as np

img = cv2.imread("../img/bright.jpg")
img_yuv = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2YUV)

img_eq = img_yuv.copy()
img_eq[:, :, 0] = cv2.equalizeHist(src=img_eq[:, :, 0])
img_eq = cv2.cvtColor(src=img_eq, code=cv2.COLOR_YUV2BGR)

img_clahe = img_yuv.copy()
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
img_clahe[:, :, 0] = clahe.apply(img_clahe[:, :, 0])
img_clahe = cv2.cvtColor(src=img_clahe, code=cv2.COLOR_YUV2BGR)

cv2.imshow(winname="img:img_eq:img_clahe", mat=np.hstack((img, img_eq, img_clahe)))
cv2.waitKey()
cv2.destroyAllWindows()
