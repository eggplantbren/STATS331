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


chains = np.loadtxt('../Code/Regression/chains.txt')
plt.figure(figsize=(8, 8))
plt.subplot(3,1,1)
plt.plot(chains[:,0])
plt.title('Trace Plots')
plt.ylabel('beta0')
plt.subplot(3,1,2)
plt.plot(chains[:,1])
plt.ylabel('beta1')
plt.subplot(3,1,3)
plt.plot(chains[:,2])
plt.ylabel('sigma')
plt.xlabel('Iteration')
plt.savefig('road_trace.pdf', bbox_inches='tight')
plt.show()

chains = np.loadtxt('../Code/Regression/chains.txt')
plt.figure(figsize=(8, 12))
plt.subplot(3,1,1)
plt.hist(chains[:,0], 20, alpha=0.5)
plt.xlabel('beta0')
plt.title('Histograms (marginal posteriors)')
plt.subplot(3,1,2)
plt.hist(chains[:,1], 20, alpha=0.5)
plt.xlabel('beta1')
plt.subplot(3,1,3)
plt.hist(chains[:,2], 20, alpha=0.5)
plt.xlabel('sigma')
plt.savefig('road_hist.pdf', bbox_inches='tight')
plt.show()
