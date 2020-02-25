import numpy as np
import sys
import cv2
from matplotlib import pyplot as plt

imgori = cv2.imread('Hermione.Granger.full.1623639.jpg', -1) # import original image
plt.hist(imgori.ravel(), 256, [0,256])
plt.show() # show histogram
cv2.imshow('original', imgori) # show image
img = cv2.imread('Hermione.Granger.full.1623639.jpg', 0) # import original image
np.set_printoptions(threshold=sys.maxsize)
cv2.imshow('image', img) # show image
plt.hist(img.ravel(), 256, [0,256])
plt.show() # show histogram
width, length = img.shape

def countX(X, img, width, length):
    y=0
    for i in range(width):
        for j in range(length):
            if img[i][j]==X:
            	y+=1
    return y;

def processImage(img, firstLimit, secondLimit, imgWidth, imgLength):
    for i in range(width):
        for j in range(length):
            if img[i][j]>firstLimit and img[i][j]<=secondLimit:
            	img[i][j] = secondLimit

temp1 = countX(0, img, width, length)
indeks = 0
temp2 = countX(1, img, width, length)
for i in range(2, 256):
	#print(temp1, temp2)
    if abs(temp2-temp1) > 200 : # interval 200 / standard deviasi
        processImage(img, indeks, i, width, length)
        temp1 = temp2
        indeks = i
        #print("a")
        temp2 = countX(i+1, img, width, length)

cv2.imshow('image', img) # show image
cv2.imwrite("result.jpg",img) #save image
cv2.imshow('result',img) # show result image
plt.hist(img.ravel(), 256, [0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()