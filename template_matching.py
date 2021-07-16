"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 8-3] 템플릿 매칭으로 객체 위치 검출
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/figures.jpg")
template = cv2.imread(filename="../img/taekwonv1.jpg")
th, tw = template.shape[:2]
cv2.imshow(winname="tamplate", mat=template)

methods = ["cv2.TM_CCOEFF_NORMED", "cv2.TM_CCORR_NORMED", "cv2.TM_SQDIFF_NORMED"]

for i, method_name in enumerate(methods):
    img_draw = img.copy()
    method = eval(method_name)

    res = cv2.matchTemplate(image=img, templ=template, method=method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(src=res)
    print(method_name, min_val, max_val, min_loc, max_loc)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
        match_val = min_val
    else:
        top_left = max_loc
        match_val = max_val

    bottom_right = (top_left[0] + tw, top_left[1] + th)
    cv2.rectangle(img=img_draw, pt1=top_left, pt2=bottom_right, color=(0, 0, 255), thickness=2)
    cv2.putText(img=img_draw, text=str(match_val), org=top_left, fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1,
                color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)
    cv2.imshow(winname=method_name, mat=img_draw)

cv2.waitKey()
cv2.destroyAllWindows()
