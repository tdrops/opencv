"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

변경된 내용만 골라내기
"""
import cv2
import numpy as np


cap = cv2.VideoCapture("./img/walking.avi")
if cap.isOpened():
    fps = cap.get(propId=cv2.CAP_PROP_FPS)
    delay = int(1000/fps)

    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
    # fgbg = cv2.createBackgroundSubtractorMOG2()
    # fgbg = cv2.bgsegm.createBackgroundSubtractorCNT()
    # fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
    # fgbg = cv2.bgsegm.createBackgroundSubtractorGSOC()
    # fgbg = cv2.bgsegm.createBackgroundSubtractorLSBP()
    # fgbg = cv2.createBackgroundSubtractorKNN()
    while True:
        ret, frame = cap.read()
        if ret:
            fgmask = fgbg.apply(frame)
            cv2.imshow(winname="frame", mat=frame)
            cv2.imshow(winname="fgmask", mat=fgmask)
            result = cv2.bitwise_and(src1=frame, src2=frame, mask=fgmask)
            cv2.imshow(winname="result", mat=result)
        else:
            break
        if cv2.waitKey(delay) & 0xff == 27:
            break
else:
    print("video open error")
cap.release()
