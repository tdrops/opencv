"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

탬플릿 매칭
"""
import cv2
import numpy as np

img = cv2.imread(filename="./img/figures.jpg")
cv2.imshow(winname="original", mat=img)
templ = cv2.imread(filename="./img/taekwonv1.jpg")
cv2.imshow(winname="template", mat=templ)
h, w = templ.shape[:2]

methods = ['cv2.TM_SQDIFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_CCOEFF_NORMED']

for i, method_name in enumerate(methods):
    draw = img.copy()
    method = eval(method_name)
    result = cv2.matchTemplate(image=img, templ=templ, method=method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(src=result)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
        match_val = min_val
    else:
        top_left = max_loc
        match_val = max_val

    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img=draw, pt1=top_left, pt2=bottom_right, color=(0, 0, 255), thickness=1)
    cv2.putText(img=draw, text=f"{match_val}", org=top_left, fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1,
                color=(0, 255, 0), thickness=1)
    cv2.imshow(winname=method_name, mat=draw)

cv2.waitKey()
cv2.destroyAllWindows()
