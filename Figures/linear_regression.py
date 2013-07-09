import numpy as np
import scipy.misc
import matplotlib.pyplot as plt

plt.rc("font", size=16, family="serif", serif="Computer Sans")
plt.rc("text", usetex=True)

data = np.loadtxt('../Data/road.txt')

plt.plot(data[:,0], data[:,1], 'bo', markersize=5)
plt.xlabel('Age (years)')
plt.ylabel('Distance (metres)')
plt.axis([0., 100., 0., 800.])
plt.savefig('road.pdf', bbox_inches='tight')
plt.show()

