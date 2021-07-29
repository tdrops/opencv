"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 8-26] calcOpticalFlowPyLK 추적
"""
import cv2
import numpy as np

cap = cv2.VideoCapture("../img/walking.avi")
fps = cap.get(propId=cv2.CAP_PROP_FPS)
delay = int(1000 / fps)

color = np.random.randint(low=0, high=255, size=(200, 3))
lines = None
prevImg = None

termcriteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    img_draw = frame.copy()
    gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)

    if prevImg is None:
        prevImg = gray
        lines = np.zeros_like(frame)
        prevPt = cv2.goodFeaturesToTrack(image=prevImg, maxCorners=200, qualityLevel=0.01, minDistance=10)
    else:
        nextImg = gray

        nextPt, status, err = cv2.calcOpticalFlowPyrLK(prevImg=prevImg, nextImg=nextImg, prevPts=prevPt, nextPts=None,
                                                       criteria=termcriteria)

        prevMv = prevPt[status == 1]
        nextMv = nextPt[status == 1]
        for i, (p, n) in enumerate(zip(prevMv, nextMv)):
            px, py = p.ravel()
            nx, ny = n.ravel()

            cv2.line(img=lines, pt1=(px, py), pt2=(nx, ny), color=color[i].tolist(), thickness=2)
            cv2.circle(img_draw, center=(nx, ny), radius=2, color=color[i].tolist(), thickness=-1)

        img_draw = cv2.add(src1=img_draw, src2=lines)
        prevImg = nextImg
        prevPt = nextMv.reshape(-1, 1, 2)

    cv2.imshow(winname="result", mat=img_draw)
    key = cv2.waitKey(delay=delay)
    if key == 27:
        break
    elif key == 8:
        prevImg = None

cv2.destroyAllWindows()
cap.release()
