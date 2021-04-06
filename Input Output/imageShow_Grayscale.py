import cv2

img_file = "../.jpg"  # 이미지 경로
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  #그레이 스케일로 읽기

if img is not None:  # 이미지가 존재한다면
    cv2.imshow('IMG', img)  # 이미지 띄우기
    cv2.waitKey()  # 잠시 대기
    cv2.destroyAllWindows()  
else:  # 이미지가 존재하지 않으면
    print('No image file.') 
