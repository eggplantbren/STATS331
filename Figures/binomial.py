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
theta = np.linspace(0., 1., 1001)
p = theta**x*(1. - theta)**(N - x)
p /= np.trapz(p, x=theta)
plt.plot(theta, np.ones(p.shape), 'g--', linewidth=2, label='Prior $p(\\theta)$')
plt.plot(theta, p, 'b', linewidth=2, label='Posterior $p(\\theta|x)$')
plt.xlabel('Possible Values $\\theta$')
plt.ylabel('Probability Density')
plt.legend()
plt.savefig('bus_inference.pdf', bbox_inches='tight')
plt.show()

prior1 = np.ones(theta.shape)
prior2 = (theta + 0.001)**(-0.5)*(1. - theta + 0.001)**(-0.5); prior2 /= np.trapz(prior2, x=theta)
prior3 = theta**100*(1. - theta)**100; prior3 /= np.trapz(prior3, x=theta)
post1 = prior1*theta**x*(1. - theta)**(N - x); post1 /= np.trapz(post1, x=theta)
post2 = prior2*theta**x*(1. - theta)**(N - x); post2 /= np.trapz(post2, x=theta)
post3 = prior3*theta**x*(1. - theta)**(N - x); post3 /= np.trapz(post3, x=theta)
plt.plot(theta, prior1, 'b--', linewidth=2)
plt.plot(theta, prior2, 'r--', linewidth=2)
plt.plot(theta, prior3, 'g--', linewidth=2)
plt.plot(theta, post1, 'b', linewidth=2)
plt.plot(theta, post2, 'r', linewidth=2)
plt.plot(theta, post3, 'g', linewidth=2)
plt.xlabel('Possible Values $\\theta$')
plt.title('Three Priors, Three Posteriors')
plt.ylabel('Probability Density')
plt.savefig('three_priors.pdf', bbox_inches='tight')
plt.show()

N = 1000
x = 500
prior1 = np.ones(theta.shape)
prior2 = (theta + 0.001)**(-0.5)*(1. - theta + 0.001)**(-0.5); prior2 /= np.trapz(prior2, x=theta)
prior3 = theta**100*(1. - theta)**100; prior3 /= np.trapz(prior3, x=theta)
post1 = prior1*theta**x*(1. - theta)**(N - x); post1 /= np.trapz(post1, x=theta)
post2 = prior2*theta**x*(1. - theta)**(N - x); post2 /= np.trapz(post2, x=theta)
post3 = prior3*theta**x*(1. - theta)**(N - x); post3 /= np.trapz(post3, x=theta)
plt.plot(theta, prior1, 'b--', linewidth=2)
plt.plot(theta, prior2, 'r--', linewidth=2)
plt.plot(theta, prior3, 'g--', linewidth=2)
plt.plot(theta, post1, 'b', linewidth=2, alpha=0.5)
plt.plot(theta, post2, 'r', linewidth=2, alpha=0.5)
plt.plot(theta, post3, 'g', linewidth=2, alpha=0.5)
plt.xlabel('Possible Values $\\theta$')
plt.ylabel('Probability Density')
plt.title('Lots of Data')
plt.xlim([0.4, 0.6])
plt.savefig('lots_of_data.pdf', bbox_inches='tight')
plt.show()
