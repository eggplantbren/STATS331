import numpy as np
import numpy.random as rng
import matplotlib.pyplot as plt

plt.rc("font", size=16, family="serif", serif="Computer Sans")
plt.rc("text", usetex=True)

rng.seed(123)

[x, y] = np.meshgrid(np.linspace(-5., 5., 101), np.linspace(-5., 5., 101))
y = y[::-1, :]

plt.figure(figsize=(12, 12))

plt.subplot(2,2,1)
plt.imshow(-np.exp(-0.5*x**2 - 0.5*(y - x)**2/0.5**2), interpolation='nearest',
			cmap='gray', extent=[-5, 5, -5, 5])
plt.title('Joint Posterior Distribution')
plt.xlabel('$a$')
plt.ylabel('$b$')

plt.subplot(2,2,2, aspect='equal')
xx = rng.randn(500)
yy = xx + 0.5*rng.randn(500)
plt.plot(xx, yy, 'ko', markersize=2, alpha=0.2)
plt.title('Joint Posterior Distribution')
plt.gca().set_xticks([-4, -2, 0, 2, 4])
plt.gca().set_yticks([-4, -2, 0, 2, 4])
plt.xlim([-5, 5])
plt.ylim([-5, 5])
plt.xlabel('$a$', fontsize=20)
plt.ylabel('$b$', fontsize=20)

plt.subplot(2,2,3)
x = x[0, :]
plt.plot(x, np.exp(-0.5*x**2)/np.sqrt(2*np.pi), 'k', linewidth=2)
plt.xlim([-5, 5])
plt.ylim([0, 0.45])
plt.xlabel('$a$', fontsize=20)
plt.ylabel('Probability Density')
plt.gca().set_yticks([0, 0.2, 0.4])
plt.title('Marginal Posterior Distribution')

plt.subplot(2,2,4)
plt.hist(xx, 30, alpha=0.5)
plt.xlim([-5, 5])
plt.title('Marginal Posterior Distribution')
plt.xlabel('$a$', fontsize=20)
plt.ylabel('Number of Samples')
plt.gca().set_yticks([0, 10, 20, 30, 40, 50])
#plt.savefig('marginalisation.pdf', bbox_inches='tight')
plt.show()

