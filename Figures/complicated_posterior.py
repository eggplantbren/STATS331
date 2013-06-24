import numpy as np
import numpy.random as rng
import matplotlib.pyplot as plt

plt.rc("font", size=16, family="serif", serif="Computer Sans")
plt.rc("text", usetex=True)

x = np.linspace(1., 10., 101)
y = np.exp(-0.5*((x - 5.)/0.5)**2)
y += 0.1*np.exp(-0.5*((x - 7.)/0.3)**2)
y += 0.1*np.logical_and(x > 3., x < 3.7)
y -= 0.2*np.logical_and(x > 5., x < 5.7)
y /= np.trapz(y, x=x)

plt.plot(x, y, 'k', linewidth=2)
plt.xlabel('Distance to a Strange Astronomical Object')
plt.ylabel('Posterior Probability Density')
plt.savefig('complicated_posterior.pdf', bbox_inches='tight')
plt.show()


