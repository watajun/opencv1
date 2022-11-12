import cv2

# print(cv2.__version__)

img = cv2.imread("image/cat.jpeg")
print(img.shape)

# サイズ変更　（縦／横）
resize_img = cv2.resize(img, dsize=(432 // 2, 768 // 2))
cv2.imwrite("image/resize_cat.jpeg", resize_img)

# cv2.putText(
    # img,
    # text="CAT !!!",
    # org=(100, 250),
    # fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    # fontScale=5,
    # color=(255, 255, 0),
    # thickness=3,
# )

cv2.imshow("Image", img)

cv2.waitKey(5000)

# 新しく画像作成
cv2.imwrite("image/new_cat.jpeg", img)
