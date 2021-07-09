"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 5-7] 원근 변환
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/fish.jpg")
rows, cols = img.shape[:2]

pts1 = np.float32([[0, 0], [0, rows], [cols, 0], [cols, rows]])
pts2 = np.float32([[100, 50], [10, rows - 50], [cols - 100, 50], [cols - 10, rows - 50]])

cv2.circle(img=img, center=(0, 0), radius=10, color=(255, 0, 0), thickness=-1)
cv2.circle(img=img, center=(0, rows), radius=10, color=(0, 255, 0), thickness=-1)
cv2.circle(img=img, center=(cols, 0), radius=10, color=(0, 0, 255), thickness=-1)
cv2.circle(img=img, center=(cols, rows), radius=10, color=(0, 255, 255), thickness=-1)

mtrx = cv2.getPerspectiveTransform(src=pts1, dst=pts2)
result = cv2.warpPerspective(src=img, M=mtrx, dsize=(cols,rows))

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="result", mat=result)
cv2.waitKey()
cv2.destroyAllWindows()
