import numpy as np
import scipy.misc
import matplotlib.pyplot as plt

plt.rc("font", size=16, family="serif", serif="Computer Sans")
plt.rc("text", usetex=True)

theta = np.loadtxt('jags_example.txt')

plt.figure(figsize=(8, 7))
plt.subplot(2,1,1)
plt.plot(theta[0:500], linewidth=1)
plt.xlabel('Iteration')
plt.ylabel('theta')

plt.subplot(2,1,2)
plt.hist(theta, 100, alpha=0.5)
plt.xlabel('theta')
plt.ylabel('Frequency')

#plt.savefig('jags_example.pdf', bbox_inches='tight')
plt.show()

