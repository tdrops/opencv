"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 5-17] 왜곡 거울 카메라
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            h, w = img.shape[:2]
            img2 = img[:, ::-1].copy()
            img3 = img[::-1, :].copy()
            img2 = np.hstack((img[:, :w // 2], img2[:, w // 2:]))
            img3 = np.vstack((img[:h // 2, :], img3[h // 2:, :]))

            mapy, mapx = np.indices(dimensions=(h, w), dtype=np.float32)
            sinx = mapx + 15 * np.sin(mapy / 20)
            cosy = mapy + 15 * np.cos(mapx / 20)
            img4 = cv2.remap(src=img, map1=sinx, map2=cosy, interpolation=cv2.INTER_LINEAR, dst=None,
                             borderMode=cv2.BORDER_REPLICATE)

            mapy, mapx = np.indices(dimensions=(h, w), dtype=np.float32)
            mapx = 2 * mapx / (w - 1) - 1
            mapy = 2 * mapy / (h - 1) - 1
            r, theta = cv2.cartToPolar(x=mapx, y=mapy)
            r[r < 1] = r[r < 1] ** 2.0
            mapx, mapy = cv2.polarToCart(magnitude=r, angle=theta)
            mapx = (mapx + 1) * (w - 1) / 2
            mapy = (mapy + 1) * (h - 1) / 2
            img5 = cv2.remap(src=img, map1=mapx, map2=mapy, interpolation=cv2.INTER_LINEAR)

            mapy, mapx = np.indices(dimensions=(h, w), dtype=np.float32)
            mapx = 2 * mapx / (w - 1) - 1
            mapy = 2 * mapy / (h - 1) - 1
            r, theta = cv2.cartToPolar(x=mapx, y=mapy)
            r[r < 1] = r[r < 1] ** 0.5
            mapx, mapy = cv2.polarToCart(magnitude=r, angle=theta)
            mapx = (mapx + 1) * (w - 1) / 2
            mapy = (mapy + 1) * (h - 1) / 2
            img6 = cv2.remap(src=img, map1=mapx, map2=mapy, interpolation=cv2.INTER_LINEAR)

            cv2.imshow(winname="cam", mat=np.vstack((np.hstack((img, img2, img3)), np.hstack((img4, img5, img6)))))
            if cv2.waitKey(1) & 0xff == 27:
                break
else:
    print("cam open error")
    pass

cap.release()
cv2.destroyAllWindows()
