import numpy as np
import matplotlib.pyplot as plt

black=np.ones((50,50))
white=np.zeros((50,50))

up=np.hstack((black,white))
down=np.hstack((white,black))

img=np.vstack((up,down))


plt.figure()
plt.imshow(img,cmap="gray")
plt.show()