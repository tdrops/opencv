"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 8-32] 책 표지 검색기
"""
import glob

import cv2
import numpy as np

ratio = 0.7
MIN_MATCH = 10

detector = cv2.ORB_create()

index_params = dict(
    algorithm=6,
    table_number=6,
    key_size=12,
    multi_prove_level=1
)

search_params = dict(checks=32)
matcher = cv2.FlannBasedMatcher(index_params, search_params)


def search(img):
    gray1 = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    kp1, desc1 = detector.detectAndCompute(gray1, None)

    results = {}

    cover_paths = glob.glob("../img/books/*.*")
    for cover_path in cover_paths:
        cover = cv2.imread(filename=cover_path)
        cv2.imshow(winname="Searching...", mat=cover)
        cv2.waitKey(delay=1)
        gray2 = cv2.cvtColor(src=cover, code=cv2.COLOR_BGR2GRAY)
        kp2, desc2 = detector.detectAndCompute(gray2, None)
        matches = matcher.knnMatch(queryDescriptors=desc1, trainDescriptors=desc2, k=2)

        good_matches = [m[0] for m in matches if len(m) == 2 and m[0].distance < m[1].distance * ratio]

        if len(good_matches) > MIN_MATCH:
            src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches])
            dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches])

            mtrx, mask = cv2.findHomography(srcPoints=src_pts, dstPoints=dst_pts, method=cv2.RANSAC,
                                            ransacReprojThreshold=5.0)

            accuracy = float(mask.sum()) / mask.size
            results[cover_path] = accuracy
    cv2.destroyWindow(winname="Searching...")
    if len(results) > 0:
        results = sorted([(v, k) for (k, v) in results.items() if v > 0], reverse=True)

    return results


cap = cv2.VideoCapture(0)
qImg = None
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("No Frame")
        break
    h, w = frame.shape[:2]

    left = w // 3
    right = (w // 3) * 2
    top = (h // 2) - (h // 3)
    bottom = (h // 2) + (h // 3)
    cv2.rectangle(img=frame, pt1=(left, top), pt2=(right, bottom), color=(255, 255, 255), thickness=3)

    flip = cv2.flip(src=frame, flipCode=1)
    cv2.imshow(winname="Book Searcher", mat=flip)
    key = cv2.waitKey(delay=1)
    if key == ord(" "):
        qImg = frame[top:bottom, left:right]
        cv2.imshow(winname="query", mat=qImg)
        break
    elif key == 27:
        break

else:
    print("No Camera!!")

cap.release()

if qImg is not None:
    gray = cv2.cvtColor(src=qImg, code=cv2.COLOR_BGR2GRAY)
    results = search(qImg)
    if len(results) == 0:
        print("No matched book cover found.")
    else:
        for (i, (accuracy, cover_path)) in enumerate(results):
            print(i, cover_path, accuracy)
            if i == 0:
                cover = cv2.imread(cover_path)
                cv2.putText(img=cover, text=f"Accuracy:{accuracy * 100}", org=(10, 100),
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0), thickness=2,
                            lineType=cv2.LINE_AA)
    cv2.imshow(winname="Result", mat=cover)
cv2.waitKey()
cv2.destroyAllWindows()
