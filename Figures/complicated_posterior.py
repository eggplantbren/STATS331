import numpy as np
import numpy.random as rng
import matplotlib.pyplot as plt

plt.rc("font", size=16, family="serif", serif="Computer Sans")
plt.rc("text", usetex=True)

x = np.linspace(0., 10., 1001)
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

# 95% credible interval = [3.31, 7.056]
plt.plot(x, y, 'k', linewidth=2)
inside = np.logical_and(x >= 3.31, x <= 7.056)
plt.fill_between(x[inside], y[inside], y2=0, color='k', alpha=0.2)
plt.fill_between(x, y, y2=0, where=(x >= 7.056), color='y', alpha=0.2)
plt.fill_between(x, y, y2=0, where=(x <= 3.31), color='y', alpha=0.2)
plt.ylim(0)
plt.gca().text(4.6, 0.1, '95\%', fontsize=16)
plt.gca().text(3.08, 0.05, '2.5\%', fontsize=12, rotation='vertical')
plt.gca().text(7.07, 0.04, '2.5\%', fontsize=12, rotation='vertical')
plt.xlabel('Distance to a Strange Astronomical Object')
plt.ylabel('Posterior Probability Density')
plt.savefig('credible_interval.pdf', bbox_inches='tight')
plt.show()

