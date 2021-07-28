"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

코딩정리하고 요약요약요약요약요약요약요약요약요약요약요약요약요약요약요약요약요약요약요약요약
"""
import cv2
import numpy as np

cap = cv2.VideoCapture("../img/walking.avi")
fps = cap.get(propId=cv2.CAP_PROP_FPS)
delay = int(1000 / fps)

fgbg = cv2.createBackgroundSubtractorMOG2()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    fgmask = fgbg.apply(frame)

    cv2.imshow(winname="frame", mat=frame)
    cv2.imshow(winname="fgmask", mat=fgmask)

    if cv2.waitKey(delay) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()
