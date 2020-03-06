
# coding: utf-8

# In[ ]:


from scipy import signal
import matplotlib.pyplot as plt
from matplotlib import image as im
from scipy import misc
ascent = im.imread('Desktop/naga.jpg')
scharr = im.imread('Desktop/naga.jpg')
b = ascent[:,:, 0]
g = ascent[:,:, 1]
r = ascent[:,:, 2]
ac= 0.21 * r + 0.72 * g + 0.07 * b
a= scharr[:,:, 0]
c = scharr[:,:, 1]
d= scharr[:,:, 2]
sc = 0.21 * a + 0.72 * c + 0.07 * d
grad = signal.convolve2d(ac, sc, boundary='symm', mode='same',fillvalue=0)
plt.imshow(grad)


# In[ ]:


from scipy import signal
import matplotlib.pyplot as plt
from matplotlib import image as im
import numpy as np
kh = np.array([[0, 8, 0], [0, -16, 0], [0, -8, 0]], dtype = np.float)
kv = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype = np.float)
image= im.imread('Desktop/graps.jpg')
b = image[:,:, 0]
g = image[:,:, 1]
r = image[:,:, 2]
gr= 0.21 * r + 0.72 * g + 0.07 * b
plt.gray()
conv=signal.convolve2d(gr,kv,boundary='symm',mode='same',fillvalue=0)
conh=signal.convolve2d(gr,kh,boundary='symm',mode='same',fillvalue=0)
con=abs(conv)
con1=abs(conh)
plt.subplot(1,4,1)
plt.imshow(image)
plt.title('original')
plt.subplot(1,4,2)
plt.imshow(gr)
plt.title('grayimage')
plt.subplot(1,4,3)
plt.imshow(con)
plt.title('verticalsobel')
plt.subplot(1,4,4)
plt.imshow(conh)
plt.title('kernal kh')


# In[32]:


plt.imshow(con)

