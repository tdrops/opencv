"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-21] 투명 배경 PNG 파일을 이용한 합성
"""
import cv2
import numpy as np

back = cv2.imread(filename="../img/girl.jpg")
logo = cv2.imread(filename="../img/opencv_logo.png", flags=cv2.IMREAD_UNCHANGED)

h, w = logo.shape[:2]
roi = back[10:10 + h, 10:10 + w]

_, mask = cv2.threshold(src=logo[:, :, 3], thresh=127, maxval=255, type=cv2.THRESH_BINARY)
not_mask = cv2.bitwise_not(src=mask)

logo = cv2.cvtColor(src=logo, code=cv2.COLOR_BGRA2BGR)
logo_masked = cv2.bitwise_and(src1=logo, src2=logo, mask=mask)
roi_not_masked = cv2.bitwise_and(src1=roi, src2=roi, mask=not_mask)

back[10:10 + h, 10:10 + w] = logo_masked + roi_not_masked

cv2.imshow(winname="mask", mat=back)
cv2.waitKey()
cv2.destroyAllWindows()
