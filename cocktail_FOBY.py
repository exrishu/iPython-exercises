import matplotlib.pyplot as plt
import numpy as np


t = np.arange(0., 12., .2)
print(t)
plt.plot(t, t, 'r:', t, t**2, 'b:', t, t**3, 'g:')
plt.show()
