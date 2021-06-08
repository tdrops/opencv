import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread(filename="./img/girl.jpg")
h, w = img.shape[:2]

mapy, mapx = np.indices(dimensions=(h, w), dtype=np.float32)

mapx = 2 * mapx / (w - 1) - 1
mapy = 2 * mapy / (h - 1) - 1

r, theta = cv2.cartToPolar(x=mapx, y=mapy)

k1, k2, k3 = 0.5, 0.2, 0.0
# k1, k2, k3 = -0.3, 0, 0
r = r * (1 + k1 * r ** 2 + k2 * r ** 4 + k3 * r ** 6)

mapx, mapy = cv2.polarToCart(magnitude=r, angle=theta)

mapx = (mapx + 1) * (w - 1) / 2
mapy = (mapy + 1) * (h - 1) / 2

result = cv2.remap(src=img, map1=mapx, map2=mapy, interpolation=cv2.INTER_LINEAR)
cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="result", mat=result)
cv2.waitKey()
cv2.destroyAllWindows()
