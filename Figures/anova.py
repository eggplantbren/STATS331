import numpy as np
import scipy.misc
import matplotlib.pyplot as plt

plt.rc("font", size=16, family="serif", serif="Computer Sans")
plt.rc("text", usetex=True)

chains = np.loadtxt("../Code/Anova/chains.txt")

plt.plot(chains[:,0], 'b')
plt.xlabel('Iteration')
plt.ylabel('$\\mu_1$ (grams)')
plt.title('Trace Plot')
plt.savefig('trace_starlings.pdf', bbox_inches='tight')
plt.show()

plt.hist(chains[:,4], 100, alpha=0.2)
plt.xlabel('$\\log$(diversity)')
plt.ylabel('Number')
plt.title('Marginal Posterior')
plt.savefig('diversity.pdf', bbox_inches='tight')
plt.show()

