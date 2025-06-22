import numpy as np
import matplotlib.pyplot as plt
img = plt.imread("road.jpg")
img = img.copy()
plt.figure()
plt.imshow(img, cmap="gray")
plt.show()

plt.figure()
plt.imshow(img, cmap="gray",alpha=0.5)
plt.show()
width=img.shape
width=width[0]
quarterwidth=int(width/4)
plt.imshow(img[:,1*quarterwidth:2*quarterwidth,:])
plt.show()

rotated=np.rot90(img)
plt.imshow(rotated)
plt.show()

mirrored=np.flip(img)
plt.imshow(mirrored)
plt.show()