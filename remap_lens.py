"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 5-12] 볼록/오목 렌즈 효과
"""
import cv2
import numpy as np

img = cv2.imread("../img/taekwonv1.jpg")
rows, cols = img.shape[:2]

# exp = 0.5
exp = 1.5
scale = 1

mapy, mapx = np.indices(dimensions=(rows, cols), dtype=np.float32)

mapx = 2 * mapx / (cols - 1) - 1
mapy = 2 * mapy / (rows - 1) - 1

r, theta = cv2.cartToPolar(mapx, mapy)

r[r < scale] = r[r < scale] ** exp

mapx, mapy = cv2.polarToCart(magnitude=r, angle=theta)

mapx = ((mapx + 1)*cols-1)/2
mapy = ((mapy + 1)*rows-1)/2

distorted = cv2.remap(src=img, map1=mapx, map2=mapy, interpolation=cv2.INTER_LINEAR)

cv2.imshow(winname="origin", mat=img)
cv2.imshow(winname="distorted", mat=distorted)
cv2.waitKey()
cv2.destroyAllWindows()
