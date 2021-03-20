from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.image as im
import numpy as np
n=im.imread("Desktop/apple.jpg")
b = image[:,:, 0]
g = image[:,:, 1]
r = image[:,:, 2]
gray_image = 0.21 * r + 0.72 * g + 0.07 * b
plt.subplot(1,2,1)
plt.imshow(image)
plt.subplot(1,2,2)
plt.imshow(gray_image, cmap='gray')