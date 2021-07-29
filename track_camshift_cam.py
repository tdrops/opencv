"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 8-29] CamShift 객체 추적 - 실행 결과 오류 있음
"""
import cv2
import numpy as np

roi_hist = None
win_name = "CamShift Tracking"
termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

cap = cv2.VideoCapture(0)
cap.set(propId=cv2.CAP_PROP_FRAME_WIDTH, value=640)
cap.set(propId=cv2.CAP_PROP_FRAME_HEIGHT, value=480)
while cap.isOpened():
    ret, frame = cap.read()
    img_draw = frame.copy()

    if roi_hist is not None:
        hsv = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2HSV)

        dst = cv2.calcBackProject(images=[hsv], channels=[0], hist=roi_hist, ranges=[0, 180], scale=1)

        ret, (x, y, w, h) = cv2.CamShift(probImage=dst, window=(x, y, w, h), criteria=termination)

        cv2.rectangle(img=img_draw, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)
        result = np.hstack((img_draw, cv2.cvtColor(src=dst, code=cv2.COLOR_GRAY2BGR)))
    else:
        cv2.putText(img=img_draw, text="Hit the space to set target to track", org=(10, 30),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 255), thickness=1,
                    lineType=cv2.LINE_AA)
        result = img_draw

    cv2.imshow(winname=win_name, mat=result)
    key = cv2.waitKey(delay=1) & 0xff
    if key == 27:
        break
    elif key == ord(" "):
        x, y, w, h = cv2.selectROI(windowName=win_name, img=frame, showCrosshair=False)
        if w and h:
            roi = frame[y:y + h, x:x + w]
            roi = cv2.cvtColor(src=roi, code=cv2.COLOR_BGR2HSV)
            mask = None
            roi_hist = cv2.calcHist(images=[roi], channels=[0], mask=mask, histSize=[180], ranges=[0, 180])
            cv2.normalize(src=roi_hist, dst=roi_hist, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
        else:
            roi_hist = None

else:
    print("no camera")

cap.release()
cv2.destroyAllWindows()
