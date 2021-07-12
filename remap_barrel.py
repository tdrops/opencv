"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 5-13] 방사 왜곡 효과
"""
import cv2
import numpy as np

# k1, k2, k3 = 0.5, 0.2, 0.2
k1, k2, k3 = -0.3, 0, 0

img = cv2.imread(filename="../img/girl.jpg")
rows, cols = img.shape[:2]

mapy, mapx = np.indices(dimensions=(rows, cols), dtype=np.float32)

mapx = 2 * mapx / (cols - 1) - 1
mapy = 2 * mapy / (rows - 1) - 1

r, theta = cv2.cartToPolar(x=mapx, y=mapy)

ru = r * (1 + k1 * r ** 2 + k2 * r ** 4 + k3 * r ** 6)

mapx, mapy = cv2.polarToCart(magnitude=ru, angle=theta)

mapx = (mapx + 1) * (cols - 1) / 2
mapy = (mapy + 1) * (rows - 1) / 2

distorted = cv2.remap(src=img, map1=mapx, map2=mapy, interpolation=cv2.INTER_LINEAR)

cv2.imshow(winname="origin", mat=img)
cv2.imshow(winname="distorted", mat=distorted)
cv2.waitKey()
cv2.destroyAllWindows()
