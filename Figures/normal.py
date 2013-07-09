import numpy as np
import scipy.misc
import matplotlib.pyplot as plt

plt.rc("font", size=16, family="serif", serif="Computer Sans")
plt.rc("text", usetex=True)

theta = np.linspace(-10., 10., 101)
post = np.exp(-0.5*(theta - 1.)**2)
post /= post.sum()

plt.plot(theta, post, 'bo-', markersize=5)
plt.xlabel('Theta')
plt.ylabel('Posterior Probability')
plt.savefig('normal.pdf', bbox_inches='tight')
plt.show()

