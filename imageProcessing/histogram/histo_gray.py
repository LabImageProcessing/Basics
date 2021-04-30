# 회색조 1채널 히스토그램

import cv2
import numpy as np
import matplotlib.pylab as plt

# 이미지 그레이 스케일로 읽기 및 출력
img = cv2.imread('../sunset.jpg', cv2.IMREAD_GRAYSCALE)  # 원하는 이미지, 경로
cv2.imshow('img', img)

# 히스토그램 계산 및 그리기
hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)

print("hist.shape:", hist.shape)  # 히스토그램의 shape (256,1)
print("hist.sum():", hist.sum(), "img.shape:",img.shape) # 히스토그램 총 합계와 이미지의 크기
plt.show()
