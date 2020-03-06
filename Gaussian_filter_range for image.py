from scipy import ndimage
from matplotlib import image as im
import matplotlib.pyplot as plt
import numpy as np
image=im.imread('Desktop/naga.jpg')
im = ndimage.gaussian_filter(image, 0)#here instead of 0 we can have any value 0,1,2,3 we can obsorve the changes
plt.sublot(1,2,1)
plt.imshow(image)
plt.title("original")
plt.subplot(1,2,2)
plt.imshow(im)
plt.title("Gaussina_filter output")