import cv2
from matplotlib import pyplot as plt
import numpy as np
import pytesseract
import imutils

path = r'C:\Users\Saske\Desktop\proiect\poze\image3.jpg'
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
plt.show()
