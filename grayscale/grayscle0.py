import cv2

img = cv2.imread('20191125-103516.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imwrite('gray.jpg',gray)