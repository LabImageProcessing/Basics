# ROI(관심영역) 실습
# 지정한 roi 원본 이미지에 복제해 출력, roi만 따로 출력

import cv2
import numpy as np

img = cv2.imread('../starbucks_summer.png')

x = 25
y = 143
w = 236
h = 236  # roi 좌표
roi = img[y:y + h, x:x + w]  # roi 지정
img_roi = roi.copy()  # roi 배열 복제

img[y:y + h, x + w:x + w + w] = roi  # 새로운 좌표에 roi 추가, 음료 2개 만들기
cv2.rectangle(img, (x, y), (x + w + w, y + h), (170, 140, 255), 3)  # 2개의 음료 영역에 사각형 표시

cv2.imshow("img", img)  # 원본 이미지 출력
cv2.imshow("roi", img_roi)  # roi만 따로 출력

cv2.waitKey(0)
cv2.destroyAllWindows()
