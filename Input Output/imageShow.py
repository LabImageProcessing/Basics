# 이미지 출력 실습

import cv2

img_file = ".jpg"  # 표시할 이미지 경로를 변수에 저장
img = cv2.imread(img_file)  # 이미지를 읽어서 img 변수에 할당

if img is not None:  # 이미지가 있다면 하위 코드 수행
  cv2.imshow('IMG', img)  # 읽은 이미지를 화면에 표시
  cv2.waitKey()  # 키가 입력될 때 까지 대기
  cv2.destroyAllWindows()  # 창 모두 닫기
else:  # 이미지가 없다면 하위 코드 수행
    print('No image file.')  
