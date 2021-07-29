"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 8-27] calcOpticalFlowFarneback 추적
"""
import cv2
import numpy as np


def drawFlow(img, flow, step=16):
    h, w = img.shape[:2]

    idx_y, idx_x = np.mgrid[step / 2:h:step, step / 2:w:step].astype(np.int)
    indices = np.stack((idx_x, idx_y), axis=-1).reshape(-1, 2)

    for x, y in indices:
        cv2.circle(img=img, center=(x, y), radius=1, color=(0, 255, 0), thickness=-1)

        dx, dy = flow[y, x].astype(np.int)

        cv2.line(img=img, pt1=(x, y), pt2=(x + dx, y + dy), color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)


prev = None

cap = cv2.VideoCapture("../img/walking.avi")
fps = cap.get(propId=cv2.CAP_PROP_FPS)
delay = int(1000 / fps)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)

    if prev is None:
        prev = gray
    else:
        flow = cv2.calcOpticalFlowFarneback(prev=prev, next=gray, flow=None, pyr_scale=0.5, levels=3, winsize=15,
                                            iterations=3, poly_n=5, poly_sigma=1.1,
                                            flags=cv2.OPTFLOW_FARNEBACK_GAUSSIAN)
        drawFlow(img=frame, flow=flow)

        prev = gray

    cv2.imshow(winname="result", mat=frame)
    if cv2.waitKey(delay=delay) == 27:
        break

cap.release()
cv2.destroyAllWindows()
