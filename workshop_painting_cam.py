"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

스케치 효과 카메라
"""



import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        img_gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
        img_gray = cv2.GaussianBlur(src=img_gray, ksize=(9,9), sigmaX=0)
        edges = cv2.Laplacian(src=img_gray, ddepth=-1, dst=None, ksize=5)
        ret, sketch = cv2.threshold(src=edges, thresh=70, maxval=255, type=cv2.THRESH_BINARY_INV)

        kernel = cv2.getStructuringElement(shape=cv2.MORPH_CROSS, ksize=(3,3))
        sketch = cv2.erode(src=sketch, kernel=kernel)
        sketch = cv2.medianBlur(src=sketch, ksize=5)

        img_sketch = cv2.cvtColor(src=sketch, code=cv2.COLOR_GRAY2BGR)

        img_paint = cv2.blur(src=frame, ksize=(10,10))
        img_paint = cv2.bitwise_and(src1=img_sketch, src2=img_paint)

        cv2.imshow(winname="cam", mat=np.hstack([img_sketch, img_paint]))

        if cv2.waitKey(1) & 0xff == 27:
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()
