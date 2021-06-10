import cv2
import numpy as np
import matplotlib.pylab as plt


img = cv2.imread(filename="./img/man_face.jpg")
cv2.imshow(winname="original", mat=img)


def tri_affine_sub(img_copy, pt1, pt2, pt3, pt3_move):
    pts1 = np.float32([pt1, pt2, pt3])  # 변경전 대응점
    pts2 = np.float32([pt1, pt2, pt3_move])  # 변경후 대응점

    x1, y1, w1, h1 = cv2.boundingRect(points=pts1)  # 위 삼각형의 최소,최대 x,y로 사각형 구하기
    x2, y2, w2, h2 = cv2.boundingRect(points=pts2)

    roi1 = img_copy[y1:y1 + h1, x1:x1 + w1]  # 변경할 영역 잘라냄

    pts1_0 = np.float32([[pts1[0, 0] - x1, pts1[0, 1] - y1], [pts1[1, 0] - x1, pts1[1, 1] - y1],
                         [pts1[2, 0] - x1, pts1[2, 1] - y1]])  # 변경 대응점을 roi 기준으로 변경
    pts2_0 = np.float32(
        [[pts2[0, 0] - x2, pts2[0, 1] - y2], [pts2[1, 0] - x2, pts2[1, 1] - y2], [pts2[2, 0] - x2, pts2[2, 1] - y2]])

    matrix = cv2.getAffineTransform(src=pts1_0, dst=pts2_0)  # 대응 행렬 구함
    warped = cv2.warpAffine(src=roi1, M=matrix, dsize=(w2, h2))  # roi1에 행렬 반영

    mask = np.zeros(shape=(h2, w2), dtype=np.uint8)  # roi2 크기로 마스크 만듬
    mask = cv2.fillPoly(img=mask, pts=[np.int32(pts2_0)], color=(255, 255, 255))

    warped_masked = cv2.bitwise_and(src1=warped, src2=warped, mask=mask)  # 변경된 값을 마스크 모양대로 잘라냄
    return warped_masked, x2, y2, w2, h2


def tri_affine(img, x1, y1, x2, y2):
    left = x1 - 50
    if left < 0:
        left = 0
    right = x1 + 50
    if right > 100:
        right = 100
    top = y1 - 50
    if top < 0:
        top = 0
    bottom = y1 + 50
    if bottom > 100:
        bottom = 100

    w = right - left + 1
    h = bottom - top + 1

    lt = [left, top]
    rt = [right, top]
    lb = [left, bottom]
    rb = [right, bottom]

    center = [x1, y1]
    center_move = [x2, y2]

    img_t = np.zeros(shape=(h, w, 3), dtype=np.uint8)
    img_l = np.zeros(shape=(h, w, 3), dtype=np.uint8)
    img_r = np.zeros(shape=(h, w, 3), dtype=np.uint8)
    img_b = np.zeros(shape=(h, w, 3), dtype=np.uint8)

    result_t, x2_t, y2_t, w2_t, h2_t = tri_affine_sub(img_copy=img.copy(), pt1=lt, pt2=rt, pt3=center,
                                                      pt3_move=center_move)
    result_l, x2_l, y2_l, w2_l, h2_l = tri_affine_sub(img_copy=img.copy(), pt1=lt, pt2=lb, pt3=center,
                                                      pt3_move=center_move)
    result_r, x2_r, y2_r, w2_r, h2_r = tri_affine_sub(img_copy=img.copy(), pt1=rt, pt2=rb, pt3=center,
                                                      pt3_move=center_move)
    result_b, x2_b, y2_b, w2_b, h2_b = tri_affine_sub(img_copy=img.copy(), pt1=lb, pt2=rb, pt3=center,
                                                      pt3_move=center_move)

    img_t[y2_t:y2_t + h2_t, x2_t:x2_t + w2_t] = result_t
    img_l[y2_l:y2_l + h2_l, x2_l:x2_l + w2_l] = result_l
    img_r[y2_r:y2_r + h2_r, x2_r:x2_r + w2_r] = result_r
    img_b[y2_b:y2_b + h2_b, x2_b:x2_b + w2_b] = result_b

    img_result = img_t + img_l + img_r + img_b

    return img_result


x1 = 0
y1 = 0
x2 = 0
y2 = 0



def onMouse(event, x, y, flags, param):
    draw = img.copy()
    global x1, y1, x2, y2
    if event == cv2.EVENT_MOUSEMOVE:
        cv2.rectangle(img=draw, pt1=(x-50,y-50), pt2=(x+50,y+50), color=(0,255,0), thickness=1)
        cv2.imshow(winname="original", mat=draw)
    elif event == cv2.EVENT_LBUTTONDOWN:
        x1 = x
        y1 = y
    elif event == cv2.EVENT_LBUTTONUP:
        x2 = x
        y2 = y

        draw[y1:y1+101,x1:x1+101] = tri_affine(img=draw[y1-50:y1+50+1,x1-50:x1+50+1], x1=50,y1=50,x2=50+(x2-x1),y2=50+(y2-y1))
        cv2.imshow(winname="original", mat=draw)


cv2.setMouseCallback(window_name="original", on_mouse=onMouse)

cv2.waitKey()
cv2.destroyAllWindows()
