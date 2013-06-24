import numpy as np
import scipy.misc
import matplotlib.pyplot as plt

plt.rc("font", size=16, family="serif", serif="Computer Sans")
plt.rc("text", usetex=True)

N = 5
x = np.arange(0, N + 1)

theta = np.array([0.3, 0.5, 0.8])
colors = ['b', 'r', 'g']

i = 0
for th in theta:
	p = scipy.misc.comb(N, x)*th**x*(1. - th)**(N - x)
	p /= p.sum()
	plt.plot(x, p, 'o-', color=colors[i], markersize=10,
		label='$\\theta = {val}$'.format(val=th))
	i += 1

plt.xlabel('Possible Data $x$')
plt.ylabel('Probability')
plt.ylim([-0.1, 1.])
plt.xlim([-0.5, 5.5])
plt.legend(numpoints=1, loc='upper center')
plt.savefig('binomial.pdf', bbox_inches='tight')
plt.show()

x = 2
theta = np.linspace(0., 1., 101)
p = theta**x*(1. - theta)**(N - x)
p /= np.trapz(p, x=theta)
plt.plot(theta, np.ones(p.shape), 'g--', linewidth=2, label='Prior $p(\\theta)$')
plt.plot(theta, p, 'b', linewidth=2, label='Posterior $p(\\theta|x)$')
plt.xlabel('Possible Values $\\theta$')
plt.ylabel('Probability Density')
plt.legend()
plt.savefig('bus_inference.pdf', bbox_inches='tight')
plt.show()

