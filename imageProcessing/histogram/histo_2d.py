# 2D 히스토그램

import cv2
import matplotlib.pylab as plt

plt.style.use('classic')  # 컬러 스타일을 1.x 스타일로 사용
img = cv2.imread('../sunset.jpg')

plt.subplot(131)
hist = cv2.calcHist([img], [0,1], None, [32,32], [0,256,0,256])
p = plt.imshow(hist)                                           
plt.title('Blue and Green')                                    
plt.colorbar(p)                                                

plt.subplot(132)
hist = cv2.calcHist([img], [1,2], None, [32,32], [0,256,0,256])
p = plt.imshow(hist)
plt.title('Green and Red')
plt.colorbar(p)

plt.subplot(133)
hist = cv2.calcHist([img], [0,2], None, [32,32], [0,256,0,256])
p = plt.imshow(hist)
plt.title('Blue and Red')
plt.colorbar(p)

plt.show()
