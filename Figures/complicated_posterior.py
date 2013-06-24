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

estimate1 = np.trapz(x*y, x=x)
F = np.cumsum(y)
F /= F[-1]
distance = np.abs(F - 0.5)
estimate2 = x[distance == np.min(distance)]
estimate3 = x[y == np.max(y)]
plt.plot(x, y, 'k', linewidth=2)
plt.axvline(estimate1, linewidth=2, color='b', label='Posterior Mean')
plt.axvline(estimate2, linewidth=2, color='r', label='Posterior Median')
plt.axvline(estimate3, linewidth=2, color='g', label='Posterior Mode')
plt.xlabel('Distance to a Strange Astronomical Object')
plt.ylabel('Posterior Probability Density')
plt.legend()
plt.savefig('estimates.pdf', bbox_inches='tight')
plt.show()

print((estimate1, estimate2, estimate3))

