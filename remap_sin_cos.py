"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 5-11] 삼각함수를 이용한 비선형 리매핑
"""
import cv2
import numpy as np

l = 20
amp = 15


img = cv2.imread(filename="../img/taekwonv1.jpg")
cols, rows = img.shape[:2]

mapy, mapx = np.indices(dimensions=(cols, rows), dtype=np.float32)

sinx = mapx + amp * np.sin(mapy/l)
cosy = mapy + amp * np.cos(mapx/l)

img_sinx = cv2.remap(src=img, map1=sinx, map2=mapy, interpolation=cv2.INTER_LINEAR)
img_cosy = cv2.remap(src=img, map1=mapx, map2=cosy, interpolation=cv2.INTER_LINEAR)

img_both = cv2.remap(src=img, map1=sinx, map2=cosy, interpolation=cv2.INTER_LINEAR, dst=None, borderMode=cv2.BORDER_REPLICATE)

cv2.imshow(winname="origin", mat=img)
cv2.imshow(winname="img_sinx", mat=img_sinx)
cv2.imshow(winname="img_cosy", mat=img_cosy)
cv2.imshow(winname="img_both", mat=img_both)
cv2.waitKey()
cv2.destroyAllWindows()
