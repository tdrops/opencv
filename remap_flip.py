"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 5-10] 변환 행렬과 리매핑으로 영상 뒤집기
"""
import cv2
import numpy as np
import time

img = cv2.imread(filename="../img/girl.jpg")
rows, cols = img.shape[:2]

st = time.time()
mflip = np.float32([[-1, 0, cols - 1], [0, -1, rows - 1]])
fliped1 = cv2.warpAffine(src=img, M=mflip, dsize=(cols, rows))
print(f"{time.time() - st}")

st2 = time.time()
mapy, mapx = np.indices(dimensions=(rows, cols), dtype=np.float32)
mapx = cols - 1 - mapx
mapy = rows - 1 - mapy
flipped2 = cv2.remap(src=img, map1=mapx, map2=mapy, interpolation=cv2.INTER_LINEAR)
print(f"{time.time() - st}")

cv2.imshow(winname="origin", mat=img)
cv2.imshow(winname="fliped1", mat=fliped1)
cv2.imshow(winname="flipped2", mat=flipped2)
cv2.waitKey()
cv2.destroyAllWindows()
