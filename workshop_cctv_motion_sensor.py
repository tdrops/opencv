"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-35] 모션 감지 CCTV 풀이
"""
import cv2
import numpy as np


THRESH = 25
MIN_DIFF = 5


cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, a = cap.read()
    ret, b = cap.read()
    while True:
        ret, c = cap.read()
        draw = c.copy()
        if ret:
            a_gray = cv2.cvtColor(src=a, code=cv2.COLOR_BGR2GRAY)
            b_gray = cv2.cvtColor(src=b, code=cv2.COLOR_BGR2GRAY)
            c_gray = cv2.cvtColor(src=c, code=cv2.COLOR_BGR2GRAY)

            diff1 = cv2.absdiff(src1=a_gray, src2=b_gray)
            diff2 = cv2.absdiff(src1=b_gray, src2=c_gray)

            _, th1 = cv2.threshold(src=diff1, thresh=THRESH, maxval=255, type=cv2.THRESH_BINARY)
            _, th2 = cv2.threshold(src=diff2, thresh=THRESH, maxval=255, type=cv2.THRESH_BINARY)

            diff = cv2.bitwise_and(src1=th1, src2=th2, dst=None)

            k = cv2.getStructuringElement(shape=cv2.MORPH_CROSS, ksize=(3,3))
            diff = cv2.morphologyEx(src=diff, op=cv2.MORPH_OPEN, kernel=k)

            count = cv2.countNonZero(src=diff)

            if count > MIN_DIFF:
                nzero = np.nonzero(diff)
                cv2.rectangle(img=draw, pt1=(min(nzero[1]),min(nzero[0])), pt2=(max(nzero[1]),max(nzero[0])), color=(0,255,0), thickness=1)
                cv2.putText(img=draw, text="Motion Detected", org=(10,30), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(0,255,0))

            cv2.imshow(winname="cam", mat=np.hstack((draw,cv2.cvtColor(src=diff, code=cv2.COLOR_GRAY2BGR))))

            if cv2.waitKey(1) & 0xff == 27:
                break
            a = b
            b = c
        else:
            break
else:
    print("cam open error")

cap.release()
cv2.destroyAllWindows()
