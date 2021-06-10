import cv2
import numpy as np
import matplotlib.pylab as plt


img = cv2.imread(filename="./img/man_face.jpg")
h,w = img.shape[:2]
cv2.imshow(winname="original", mat=img)


x1 = 0
y1 = 0
x2 = 0
y2 = 0


def onMouse(event, x, y, flags, param):
    global x1, y1, x2, y2, img, h, w
    if event == cv2.EVENT_LBUTTONDOWN:
        x1 = x
        y1 = y
    elif event == cv2.EVENT_LBUTTONUP:
        x2 = x
        y2 = y
        left = x - 50
        if left < 0:
            left = 0

        right = x + 50
        if right > w - 1:
            right = w - 1

        top = y - 50
        if top < 0:
            top = 0

        bottom = y + 50
        if bottom > h -1:
            bottom = h - 1

        pts1 = np.float32([[x1,y1],[left,top],[left,bottom]])
        pts2 = np.float32([[x2,y2],[left,top],[left,bottom]])
        tri_affine(img, pts1=pts1, pts2=pts2)

        pts1 = np.float32([[x1,y1],[left,bottom],[right,bottom]])
        pts2 = np.float32([[x2,y2],[left,bottom],[right,bottom]])
        tri_affine(img, pts1=pts1, pts2=pts2)

        pts1 = np.float32([[x1,y1],[right,bottom],[right,top]])
        pts2 = np.float32([[x2,y2],[right,bottom],[right,top]])
        tri_affine(img, pts1=pts1, pts2=pts2)

        pts1 = np.float32([[x1,y1],[right,top],[left,top]])
        pts2 = np.float32([[x2,y2],[right,top],[left,top]])
        tri_affine(img, pts1=pts1, pts2=pts2)

        cv2.imshow(winname="original", mat=img)


def tri_affine(img, pts1, pts2):
    x1,y1,w1,h1 = cv2.boundingRect(points=pts1)  # 위 삼각형의 최소,최대 x,y로 사각형 구하기
    x2,y2,w2,h2 = cv2.boundingRect(points=pts2)

    roi1 = img[y1:y1+h1,x1:x1+w1]  # 변경할 영역 잘라냄
    roi2 = img[y2:y2+h2,x2:x2+w2]

    pts1_0 = np.float32([[pts1[0,0]-x1,pts1[0,1]-y1],[pts1[1,0]-x1,pts1[1,1]-y1],[pts1[2,0]-x1,pts1[2,1]-y1]])  # 변경 대응점을 roi 기준으로 변경
    pts2_0 = np.float32([[pts2[0,0]-x2,pts2[0,1]-y2],[pts2[1,0]-x2,pts2[1,1]-y2],[pts2[2,0]-x2,pts2[2,1]-y2]])

    matrix = cv2.getAffineTransform(src=pts1_0, dst=pts2_0)  # 대응 행렬 구함
    warped = cv2.warpAffine(src=roi1, M=matrix, dsize=(w2,h2))  # roi1에 행렬 반영

    mask = np.zeros(shape=(h2,w2), dtype=np.uint8)  # roi2 크기로 마스크 만듬
    mask = cv2.fillConvexPoly(img=mask, points=np.int32(pts2_0), color=(255,255,255))  # 변경후 대응점 모양으로 잘라내기 위한 마스크

    warped_masked = cv2.bitwise_and(src1=warped, src2=warped, mask=mask)  # 변경된 값을 마스크 모양대로 잘라냄
    roi2_not_mask = cv2.bitwise_and(src1=roi2, src2=roi2, mask=cv2.bitwise_not(src=mask))  # roi2를 마스크 외부 값만 잘라냄

    roi2_not_mask = roi2_not_mask + warped_masked  # 이미지 2개를 합침
    img[y2:y2+h2,x2:x2+w2] = roi2_not_mask  # 합친 이미지를 roi2영역에 반영

    return img

cv2.setMouseCallback(window_name="original", on_mouse=onMouse)

cv2.waitKey()
cv2.destroyAllWindows()
