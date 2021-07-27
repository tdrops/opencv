"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 8-23] 카메라로 객체 매칭
"""
import cv2
import numpy as np

img1 = None
win_name = "Camera Matching"
MIN_MATCH = 10

detector = cv2.ORB_create(nfeatures=1000)

index_params = dict(algorithm=6,
                    table_number=6,
                    key_size=12,
                    multi_probe_level=1)

search_params = dict(checks=32)

matcher = cv2.FlannBasedMatcher(index_params, search_params)

cap = cv2.VideoCapture(0)
cap.set(propId=cv2.CAP_PROP_FRAME_WIDTH, value=640)
cap.set(propId=cv2.CAP_PROP_FRAME_HEIGHT, value=480)

while cap.isOpened():
    ret, frame = cap.read()
    if img1 is None:
        res = frame
    else:
        img2 = frame
        gray1 = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2GRAY)

        kp1, desc1 = detector.detectAndCompute(gray1, None)
        kp2, desc2 = detector.detectAndCompute(gray2, None)

        matches = matcher.knnMatch(queryDescriptors=desc1, trainDescriptors=desc2, k=2)

        ratio = 0.75
        good_matches = [m[0] for m in matches if len(m) == 2 and m[0].distance < m[1].distance * ratio]

        matchesMask = np.zeros(shape=len(good_matches)).tolist()

        if len(good_matches) > MIN_MATCH:
            src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches])
            dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches])

            mtrx, mask = cv2.findHomography(srcPoints=src_pts, dstPoints=dst_pts, method=cv2.RANSAC,
                                            ransacReprojThreshold=5.0)

            if mask.sum() > MIN_MATCH:
                matchesMask = mask.ravel().tolist()

                h, w = img1.shape[:2]
                pts = np.float32([[[0, 0]], [[0, h - 1]], [[w - 1, h - 1]], [[w - 1, 0]]])
                dst = cv2.perspectiveTransform(src=pts, m=mtrx)
                img2 = cv2.polylines(img=img2, pts=[np.int32(dst)], isClosed=True, color=255, thickness=3,
                                     lineType=cv2.LINE_AA)

        res = cv2.drawMatches(img1=img1, keypoints1=kp1, img2=img2, keypoints2=kp2, matches1to2=good_matches,
                              outImg=None, matchesMask=matchesMask, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

    cv2.imshow(winname=win_name, mat=res)
    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord(" "):
        x, y, w, h = cv2.selectROI(windowName=win_name, img=frame, showCrosshair=False)
        if w and h:
            img1 = frame[y:y + h, x:x + w]

else:
    print("can't open camera")
cap.release()
cv2.destroyAllWindows()
