import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.size": 14,
})


# Geometric distribution plot
x = np.arange(11)
p = 0.7**x
p = p/np.sum(p)

plt.bar(x, p)
plt.xlabel("$x$")
plt.ylabel("Probability")
plt.title("A discrete probability distribution")
plt.savefig("images/geometric.pdf", bbox_inches="tight")

plt.clf()
x = np.linspace(-5.0, 5.0, 1001)
plt.plot(x, np.exp(-0.5*x**2)/np.sqrt(2.0*np.pi))
plt.xlabel("$x$")
plt.ylabel("Probability Density")
plt.title("A continuous probability distribution")
plt.savefig("images/normal.pdf", bbox_inches="tight")


