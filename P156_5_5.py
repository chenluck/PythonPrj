import matplotlib.pyplot as plt
import numpy as np
t=np.arange(-1,2,.01)
s=np.sin(2*np.pi*t)
plt.plot(t,s)
plt.axis('equal')
plt.show()
