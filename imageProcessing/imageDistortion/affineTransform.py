import cv2
import numpy as np
from matplotlib import pyplot as plt

file_name = '.jpg'
img = cv2.imread(file_name)
rows, cols = img.shape[:2]

# 변환 전 후 각 3개 좌표 생성
pts1 = np.float32([[100, 50], [200, 50], [100, 200]])
pts2 = np.float32([[80, 70], [210, 60], [250, 120]])

# 변환 전 좌표 이미지에 표시
cv2.circle(img, (100,50), 5, (255,0), -1)
cv2.circle(img, (200,50), 5, (0,255,0), -1)
cv2.circle(img, (100,200), 5, (0,0,255), -1)

# 짝지은 3개 좌표로 변환 행렬 계산
mtrx = cv2.getAffineTransform(pts1, pts2)

# 어핀 변환 적용
dst = cv2.warpAffine(img, mtrx, (int(cols*1.5), rows))

# 결과 출력
cv2.imshow('origin',img)
cv2.imshow('affin', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
