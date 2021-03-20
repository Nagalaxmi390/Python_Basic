from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.image as im
import numpy as np
n=im.imread("Desktop/apple.jpg")
plt.imshow(n,cmap=plt.cm.gray)
type(n)#numpy.ndarrray
n.shape#(x,y,z)dementional properties
n.dtype#dtype('unit8')referes to 8 bit images
n.tofile('naa.raw') # Create raw file
n_from_raw = np.fromfile('naa.raw', dtype=np.uint8)#reading of the file in raw array format
n_from_raw.shape=n.shape#shape of the raw file #converting to actual shape of the image
n_memmap= np.memmap('naa.raw', dtype=np.uint8, shape=n.shape)#create a memory to read in array bye format as a sub parts to decrease the complexcity
i = np.random.randint(0, 256, 10000).reshape((100, 100))#it will create the randomnumber in the range(0,256)of 100 cols and 100 rows
