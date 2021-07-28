"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 8-24] BackgroundSubtractorMOG로 배경 제거
"""
import cv2
import numpy as np

cap = cv2.VideoCapture("../img/walking.avi")
fps = cap.get(propId=cv2.CAP_PROP_FPS)
delay = int(1000 / fps)

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    fgmask = fgbg.apply(frame)
    cv2.imshow(winname="fgmask", mat=fgmask)
    # cv2.imshow(winname="background", mat=fgbg.getBackgroundImage())  # getBackgroundImage
    if cv2.waitKey(delay=delay) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()
