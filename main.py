# Ejemplo de código para el ambiente virtual rnap
import numpy as np
import matplotlib.pyplot as plt

a = np.array([[0, 255, 255, 255, 0], [0, 255, 0, 0, 0], [0, 255, 0, 0, 0], [0, 255, 0, 0, 0], [0, 255, 255, 255, 0]]).astype(np.uint8)

a2 = 255-a

plt.figure()
plt.subplot(2, 1, 1)
plt.imshow(a, cmap ='gray', vmin=0, vmax=255)

plt.subplot(2, 1, 2)
plt.imshow(a2, cmap ='gray', vmin=0, vmax=255)
plt.show()