"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 8-30] Tracker APIs
"""
import cv2
import numpy as np

trackers = [cv2.TrackerBoosting_create,
            cv2.TrackerMIL_create,
            cv2.TrackerKCF_create,
            cv2.TrackerTLD_create,
            cv2.TrackerMedianFlow_create,
            cv2.TrackerGOTURN_create,
            cv2.TrackerCSRT_create,
            cv2.TrackerMOSSE_create]
trackerIdx = 0
tracker = None
isFirst = True

# video_src = 0
video_src = "../img/highway.mp4"

cap = cv2.VideoCapture(video_src)
fps = cap.get(propId=cv2.CAP_PROP_FPS)
delay = int(1000 / fps)
win_name = "Tracking APIs"

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Cannot read video file")
        break

    img_draw = frame.copy()
    if tracker is None:
        cv2.putText(img=img_draw, text="Press the Space to set ROI", org=(100, 80), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.75, color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
    else:
        ok, bbox = tracker.update(frame)
        (x, y, w, h) = bbox
        if ok:
            cv2.rectangle(img=img_draw, pt1=(int(x), int(y)), pt2=(int(x + w), int(y + h)), color=(0, 255, 0),
                          thickness=2, lineType=1)
        else:
            cv2.putText(img=img_draw, text="Tracking fail", org=(100, 80), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.75, color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA)

    trackerName = tracker.__class__.__name__
    cv2.putText(img=img_draw, text=str(trackerIdx) + ":" + trackerName, org=(100, 20),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.75, color=(0, 255, 0), thickness=2,
                lineType=cv2.LINE_AA)

    cv2.imshow(winname=win_name, mat=img_draw)
    key = cv2.waitKey(1) & 0xff

    if key == ord(' ') or (video_src != 0 and isFirst):
        isFirst = False
        roi = cv2.selectROI(windowName=win_name, img=frame, showCrosshair=False)
        if roi[2] and roi[3]:
            tracker = trackers[trackerIdx]()
            isInit = tracker.init(frame, roi)
    elif key in range(48, 56):
        trackerIdx = key - 48
        if bbox is not None:
            tracker = trackers[trackerIdx]()
            isInit = tracker.init(frame, bbox)
    elif key == 27:
        break

else:
    print("Could not open video")
cap.release()
cv2.destroyAllWindows()
