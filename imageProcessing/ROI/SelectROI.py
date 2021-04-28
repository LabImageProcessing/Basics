# ROI 실습
# selectROI로 관심영역 지정 및 표시, 저장

import cv2
import numpy as np

img = cv2.imread('.jpg')
img_resize = cv2.resize(img, dsize=(500, 500), interpolation=cv2.INTER_AREA)  # 이미지 크기 조절

x, y, w, h = cv2.selectROI('img', img_resize, False)
if w and h:
    roi = img_resize[y:y + h, x:x + w]
    cv2.imshow('cropped', roi)  # ROI 지정 영역을 새창으로 표시
    cv2.imwrite('./cropped2.jpg', roi)  # ROI 영역 파일로 저장

cv2.waitKey(0)
cv2.destroyAllWindows()
