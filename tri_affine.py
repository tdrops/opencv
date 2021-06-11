import cv2
import numpy as np
import matplotlib.pylab as plt


img = cv2.imread(filename="./img/man_face.jpg")
cv2.imshow(winname="original", mat=img)

is_drag = False

x1 = 0
y1 = 0
x2 = 0
y2 = 0


def t_affine_sub(img, pts1, pts2):
    h, w = img.shape[:2]
    matrix = cv2.getAffineTransform(src=pts1, dst=pts2)  # 대응점으로 행렬 구함
    warped = cv2.warpAffine(src=img, M=matrix, dsize=(w, h))  # 원본이미지에 행렬 적용
    mask = np.zeros_like(a=img, dtype=np.uint8)
    cv2.fillPoly(img=mask, pts=[np.int32(pts2)], color=(255, 255, 255))  # 두번째 삼각형 모양의 마스크 생성
    warped_masked = cv2.bitwise_and(src1=warped, src2=mask)  # 변형한 이미지를 두번째 삼각형 모양으로 잘라냄

    return warped_masked


def t_affine(img, x1, y1, x2, y2):
    h, w = img.shape[:2]

    left = x1 - 50
    if left < 0:
        left = 0
    top = y1 - 50
    if top < 0:
        top = 0
    right = x1 + 50
    # if right > w - 1:
    #     right = w - 1
    bottom = y1 + 50
    # if bottom > h - 1:
    #     bottom = h - 1

    lt = [left-left, top-top]
    rt = [right-left, top-top]
    lb = [left-left, bottom-top]
    rb = [right-left, bottom-top]

    pts_u_1 = np.float32([[x1-left, y1-top], lt, rt])
    pts_u_2 = np.float32([[x2-left, y2-top], lt, rt])

    pts_d_1 = np.float32([[x1-left, y1-top], lb, rb])
    pts_d_2 = np.float32([[x2-left, y2-top], lb, rb])

    pts_l_1 = np.float32([[x1-left, y1-top], lt, lb])
    pts_l_2 = np.float32([[x2-left, y2-top], lt, lb])

    pts_r_1 = np.float32([[x1-left, y1-top], rt, rb])
    pts_r_2 = np.float32([[x2-left, y2-top], rt, rb])

    draw = img.copy()
    return t_affine_sub(img=draw, pts1=pts_u_1, pts2=pts_u_2) \
           + t_affine_sub(img=draw, pts1=pts_d_1, pts2=pts_d_2) \
           + t_affine_sub(img=draw, pts1=pts_l_1, pts2=pts_l_2) \
           + t_affine_sub(img=draw, pts1=pts_r_1, pts2=pts_r_2)


def onMouse(event, x, y, flags, param):
    global img, is_drag, x1, y1, x2, y2
    if event == cv2.EVENT_MOUSEMOVE:
        if not is_drag:
            draw = img.copy()
            cv2.rectangle(img=draw, pt1=(x - 50, y - 50), pt2=(x + 50, y + 50), color=(0, 255, 0), thickness=1)
            cv2.imshow(winname="original", mat=draw)
    elif event == cv2.EVENT_LBUTTONDOWN:
        is_drag = True
        x1 = x
        y1 = y
    elif event == cv2.EVENT_LBUTTONUP:
        is_drag = False
        x2 = x
        y2 = y

        h, w = img.shape[:2]

        left = x1 - 50
        if left < 0:
            left = 0
        top = y1 - 50
        if top < 0:
            top = 0
        right = x1 + 50
        if right > w - 1:
            right = w - 1
        bottom = y1 + 50
        if bottom > h - 1:
            bottom = h - 1

        img[top:bottom + 1, left:right + 1] = t_affine(img=img[top:bottom + 1, left:right + 1].copy(), x1=x1, y1=y1,
                                                       x2=x2, y2=y2)


cv2.setMouseCallback(window_name="original", on_mouse=onMouse)

cv2.waitKey()
cv2.destroyAllWindows()
