import matplotlib.pyplot as plt
import numpy as np
plt.style.use("ggplot")#we can use "dark_background",or "presentation"
fig = plt.figure()
data = im.imread('Desktop/apple.jpg')
plt.imshow(data)
plt.title('my random fig')
plt.colorbar()  
plt.savefig('temp2.png', facecolor="black", edgecolor="none")
plt.show()