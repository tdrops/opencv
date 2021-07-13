"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 6-15] 열림과 닫힘 연산으로 노이즈 제거
"""
import cv2
import numpy as np

img1 = cv2.imread(filename="../img/morph_dot.png", flags=cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(filename="../img/morph_hole.png", flags=cv2.IMREAD_GRAYSCALE)

k = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(5,5))

opening = cv2.morphologyEx(src=img1, op=cv2.MORPH_OPEN, kernel=k)
closing = cv2.morphologyEx(src=img2, op=cv2.MORPH_CLOSE, kernel=k)

cv2.imshow(winname="img1/open/img2/close", mat=np.vstack((np.hstack((img1,opening)),
                                                          np.hstack((img2,closing)))))
cv2.waitKey()
cv2.destroyAllWindows()
