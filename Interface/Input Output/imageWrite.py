    import cv2

    img_file = '../.jpg'  # 이미지 파일 경로
    save_file = '../.jpg'  # 수정 후 저장할 파일 경로

    img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  # 원본 이미지를 grayscale 수행 후 img 변수에 저장
    cv2.imshow(img_file, img)  # img 변수 출력(grayscale한 이미지)
    cv2.imwrite(save_file, img)  # 파일로 저장
    cv2.waitKey()  # 잠시 대기
    cv2.destroyAllWindows()
