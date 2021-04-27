# ROI(관심영역) 실습
# 좌표 직접 지정

import cv2
import numpy as np

img = cv2.imread('../starbucks_summer.png')  # 각자 이미지 경로 설정

x = 25
y = 143
w = 236
h = 236  # roi 좌표
roi = img[y:y + h, x:x + w]  # roi 지정

print(roi.shape)
cv2.rectangle(roi, (0, 0), (h - 1, w - 1), (170, 140, 255), 3)  # roi 전체에 사각형 그리기
cv2.imshow("img", img)

key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()
