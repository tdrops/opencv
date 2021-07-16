"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 8-5] 시-토마시 코너 검출
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/house.jpg")
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(image=gray, maxCorners=80, qualityLevel=0.01, minDistance=10)
corners = np.int32(corners)

for corner in corners:
    x, y = corner[0]
    cv2.circle(img=img, center=(x, y), radius=5, color=(0, 0, 255), thickness=1, lineType=cv2.LINE_AA)

cv2.imshow(winname="corners", mat=img)
cv2.waitKey()
cv2.destroyAllWindows()
