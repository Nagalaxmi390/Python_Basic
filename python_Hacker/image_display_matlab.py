#background elemination for apple
import matplotlib.pyplot as plt
import matplotlib.image as im
img = im.imread('Desktop/apple.jpg')#image reading
plt.imshow(img)
plt.xlim((0,255))
plt.ylim((255,0))
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.title('Naga apple fruit')