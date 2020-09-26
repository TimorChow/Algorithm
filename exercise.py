from PIL import Image
import cv2

img = cv2.imread("1.png")
height, width, c = img.shape

for i in range(height):
    for j in range(width):
        r, g, b = img[i, j]
        # if (b > g and b > r):  # 对蓝色进行判断
        #     b = 127
        #     g = 127
        #     r = 127
        # if (b == 126 and g == 123 and r == 255):
        #     b = 127
        #     g = 127
        #     r = 257
        if (r!=255 and  b!=255 and g!=255):
            # r = r
            b = b-40
        img[i, j] = (r, g, b)

cv2.imshow('a', img)
cv2.waitKey(0)

