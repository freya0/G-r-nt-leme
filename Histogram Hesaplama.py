import cv2
import numpy as np


foto = cv2.imread("sincap.jpg")
cv2.imshow("sincap",foto)
cv2.waitKey()

B = foto[:,:,0]
G = foto[:,:,1]
R = foto[:,:,2]

from matplotlib import pyplot as plt
import matplotlib.image as mpimg
imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
plt.imshow(imgGray,cmap='gray')
plt.show()

Hist = np.zeros(256, dtype=int)
[h, w] = np.shape(imgGray)
for v in range(h):
    for u in range(w):
        i = int(imgGray[v, u])
        Hist[i] += 1

print(np.sum(Hist))
plt.plot(Hist)
plt.show()
