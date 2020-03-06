from scipy import ndimage
from matplotlib import image as im
import matplotlib.pyplot as plt
import numpy as np
image=im.imread('Desktop/horse.jpg')
r=image[:,:,0]
g=image[:,:,1]
b=image[:,:,2]
grey_scale=0.21 * r + 0.72 * g + 0.07 * b
plt.gray()
edge_horizont=ndimage.sobel(grey_scale, 0)
edge_vertical=ndimage.sobel(grey_scale, 1)
magnitude=np.hypot(edge_horizont, edge_vertical)
plt.subplot(1,3,1)
plt.imshow(image)
plt.title('oringal image')
plt.subplot(1,3,2)
plt.imshow(grey_scale)
plt.title("greyimage")
plt.subplot(1,3,3)
plt.imshow(magnitude)
plt.title('edge detected image')