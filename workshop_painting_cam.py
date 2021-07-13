"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 6-21] 스케치 효과 카메라 풀이
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    if ret:
        img_gray = cv2.cvtColor(src=img,code=cv2.COLOR_BGR2GRAY)
        sketch = cv2.GaussianBlur(src=img_gray, ksize=(9,9), sigmaX=0)
        sketch = cv2.Laplacian(src=sketch, ddepth=-1, ksize=5)
        _, sketch = cv2.threshold(src=sketch, thresh=70, maxval=255, type=cv2.THRESH_BINARY_INV)

        kernel = cv2.getStructuringElement(shape=cv2.MORPH_CROSS, ksize=(3,3))
        sketch = cv2.erode(src=sketch, kernel=kernel)

        sketch = cv2.medianBlur(src=sketch, ksize=5)
        sketch = cv2.cvtColor(src=sketch, code=cv2.COLOR_GRAY2BGR)

        # sketch = cv2.bitwise_not(src=sketch)

        blur = cv2.blur(src=img, ksize=(10,10))
        blur2 = cv2.bitwise_and(src1=blur, src2=sketch)

        cv2.imshow(winname="cam", mat=np.hstack((sketch,blur2)))
        if cv2.waitKey(1) & 0xff == 27:
            break
    else:
        pass

cap.release()
cv2.destroyAllWindows()
