"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 5-16] 포토샵 리퀴파이 도구 풀이 결과
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/man_face.jpg")
cv2.imshow(winname="draw", mat=img)

x1 = 0
y1 = 0


def onMouse(event, x, y, flags, param):
    global x1, y1
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = img.copy()
        cv2.rectangle(img=draw, pt1=(x - 50, y - 50), pt2=(x + 50, y + 50), color=(0, 255, 0), thickness=1)
        x1 = x
        y1 = y
        cv2.imshow(winname="draw", mat=draw)
    elif event == cv2.EVENT_LBUTTONUP:
        x2 = x
        y2 = y

        dx = x1 - 50
        dy = y1 - 50
        roi = img[y1 - 50:y1 + 50, x1 - 50:x1 + 50]
        out = roi.copy()

        offset1 = np.float32([[x1 - dx, y1 - dy], [x1 - 50 - dx, y1 - 50 - dy], [x1 + 50 - dx, y1 - 50 - dy]])
        offset2 = np.float32([[x - dx, y - dy], [x1 - 50 - dx, y1 - 50 - dy], [x1 + 50 - dx, y1 - 50 - dy]])
        m = cv2.getAffineTransform(src=offset1, dst=offset2)
        # warped = cv2.warpAffine(src=roi, M=m, dsize=(100, 100), dst=None, flags=cv2.INTER_LINEAR,
        #                         borderMode=cv2.BORDER_REFLECT_101)
        warped = cv2.warpAffine(src=roi, M=m, dsize=(100, 100))
        mask = np.full(shape=(100, 100), fill_value=0, dtype=np.uint8)
        cv2.fillConvexPoly(img=mask, points=np.int32(offset2), color=255)
        mask_not = cv2.bitwise_not(src=mask)
        result = cv2.bitwise_and(src1=warped, src2=warped, mask=mask)
        out = cv2.bitwise_and(src1=out, src2=out, mask=mask_not)
        out = out + result

        offset1 = np.float32([[x1 - dx, y1 - dy], [x1 - 50 - dx, y1 + 50 - dy], [x1 + 50 - dx, y1 + 50 - dy]])
        offset2 = np.float32([[x - dx, y - dy], [x1 - 50 - dx, y1 + 50 - dy], [x1 + 50 - dx, y1 + 50 - dy]])
        m = cv2.getAffineTransform(src=offset1, dst=offset2)
        # warped = cv2.warpAffine(src=roi, M=m, dsize=(100, 100), dst=None, flags=cv2.INTER_LINEAR,
        #                         borderMode=cv2.BORDER_REFLECT_101)
        warped = cv2.warpAffine(src=roi, M=m, dsize=(100, 100))
        mask = np.full(shape=(100, 100), fill_value=0, dtype=np.uint8)
        cv2.fillConvexPoly(img=mask, points=np.int32(offset2), color=255)
        mask_not = cv2.bitwise_not(src=mask)
        result = cv2.bitwise_and(src1=warped, src2=warped, mask=mask)
        out = cv2.bitwise_and(src1=out, src2=out, mask=mask_not)
        out = out + result

        offset1 = np.float32([[x1 - dx, y1 - dy], [x1 - 50 - dx, y1 - 50 - dy], [x1 - 50 - dx, y1 + 50 - dy]])
        offset2 = np.float32([[x - dx, y - dy], [x1 - 50 - dx, y1 - 50 - dy], [x1 - 50 - dx, y1 + 50 - dy]])
        m = cv2.getAffineTransform(src=offset1, dst=offset2)
        # warped = cv2.warpAffine(src=roi, M=m, dsize=(100, 100), dst=None, flags=cv2.INTER_LINEAR,
        #                         borderMode=cv2.BORDER_REFLECT_101)
        warped = cv2.warpAffine(src=roi, M=m, dsize=(100, 100))
        mask = np.full(shape=(100, 100), fill_value=0, dtype=np.uint8)
        cv2.fillConvexPoly(img=mask, points=np.int32(offset2), color=255)
        mask_not = cv2.bitwise_not(src=mask)
        result = cv2.bitwise_and(src1=warped, src2=warped, mask=mask)
        out = cv2.bitwise_and(src1=out, src2=out, mask=mask_not)
        out = out + result

        offset1 = np.float32([[x1 - dx, y1 - dy], [x1 + 50 - dx, y1 - 50 - dy], [x1 + 50 - dx, y1 + 50 - dy]])
        offset2 = np.float32([[x - dx, y - dy], [x1 + 50 - dx, y1 - 50 - dy], [x1 + 50 - dx, y1 + 50 - dy]])
        m = cv2.getAffineTransform(src=offset1, dst=offset2)
        # warped = cv2.warpAffine(src=roi, M=m, dsize=(100, 100), dst=None, flags=cv2.INTER_LINEAR,
        #                         borderMode=cv2.BORDER_REFLECT_101)
        warped = cv2.warpAffine(src=roi, M=m, dsize=(100, 100))
        mask = np.full(shape=(100, 100), fill_value=0, dtype=np.uint8)
        cv2.fillConvexPoly(img=mask, points=np.int32(offset2), color=255)
        mask_not = cv2.bitwise_not(src=mask)
        result = cv2.bitwise_and(src1=warped, src2=warped, mask=mask)
        out = cv2.bitwise_and(src1=out, src2=out, mask=mask_not)
        out = out + result

        img[y1 - 50:y1 + 50, x1 - 50:x1 + 50] = out

        cv2.imshow(winname="draw", mat=img)


cv2.setMouseCallback(window_name="draw", on_mouse=onMouse)

cv2.waitKey()
cv2.destroyAllWindows()
